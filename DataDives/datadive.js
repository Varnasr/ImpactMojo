/* ImpactMojo Data Dives — shared, responsive chart engine.
   Charts are drawn at the container's REAL pixel width (viewBox = clientWidth),
   so 1 SVG unit = 1 CSS px and text stays readable at any screen size instead of
   shrinking. Every chart re-renders on resize and switches to a compact layout on
   narrow screens. All charts ship a hover tooltip; the page supplies a <details>
   data table for the non-visual fallback. */
(function () {
  var SVGNS = "http://www.w3.org/2000/svg";

  // --- shared tooltip ---
  var tip;
  function ensureTip() {
    if (tip) return tip;
    tip = document.createElement('div');
    tip.className = 'dv-tip';
    tip.setAttribute('role', 'status');
    tip.setAttribute('aria-live', 'polite');
    document.body.appendChild(tip);
    window.addEventListener('mousemove', function (e) { if (tip.classList.contains('show')) moveTip(e); });
    return tip;
  }
  function showTip(html, e) { ensureTip(); tip.innerHTML = html; tip.classList.add('show'); moveTip(e); }
  function moveTip(e) {
    var w = tip.offsetWidth, h = tip.offsetHeight;
    var nx = e.clientX + 14, ny = e.clientY + 14;
    if (nx + w > window.innerWidth - 8) nx = e.clientX - w - 14;
    if (ny + h > window.innerHeight - 8) ny = e.clientY - h - 14;
    tip.style.left = nx + 'px'; tip.style.top = ny + 'px';
  }
  function hideTip() { if (tip) tip.classList.remove('show'); }

  function el(tag, attrs, text) {
    var n = document.createElementNS(SVGNS, tag);
    if (attrs) for (var k in attrs) n.setAttribute(k, attrs[k]);
    if (text != null) n.textContent = text;
    return n;
  }
  function svgRoot(W, H) {
    // Inline style beats any global `svg{}` rule from injected site chrome, so the
    // SVG always fills its mount exactly; viewBox = measured px means 1 unit = 1 CSS px.
    return el('svg', { viewBox: '0 0 ' + W + ' ' + H, preserveAspectRatio: 'xMinYMin meet',
      role: 'presentation', style: 'display:block;width:100%;height:auto;overflow:visible' });
  }

  // Gradient + shadow defs, unique per SVG. Stop colours are set in CSS (theme-aware).
  var _uid = 0;
  function addDefs(svg) {
    var id = 'dvg' + (_uid++);
    var defs = el('defs');
    function grad(sfx, x2, y2, stops) {
      var g = el('linearGradient', { id: id + sfx, x1: '0', y1: '0', x2: x2, y2: y2 });
      stops.forEach(function (c) { g.appendChild(el('stop', { offset: c[0], 'class': c[1] })); });
      defs.appendChild(g);
    }
    grad('-a', '1', '0', [['0', 'dv-stop-a0'], ['1', 'dv-stop-a1']]);
    grad('-hl', '1', '0', [['0', 'dv-stop-hl0'], ['1', 'dv-stop-hl1']]);
    grad('-area', '0', '1', [['0', 'dv-stop-area0'], ['1', 'dv-stop-area1']]);
    grad('-areaB', '0', '1', [['0', 'dv-stop-areaB0'], ['1', 'dv-stop-areaB1']]);
    var rgA = el('radialGradient', { id: id + '-dotA', cx: '0.35', cy: '0.3', r: '0.85' });
    rgA.appendChild(el('stop', { offset: '0', 'class': 'dv-stop-dotA0' }));
    rgA.appendChild(el('stop', { offset: '1', 'class': 'dv-stop-dotA1' }));
    defs.appendChild(rgA);
    var rgB = el('radialGradient', { id: id + '-dotB', cx: '0.35', cy: '0.3', r: '0.85' });
    rgB.appendChild(el('stop', { offset: '0', 'class': 'dv-stop-dotB0' }));
    rgB.appendChild(el('stop', { offset: '1', 'class': 'dv-stop-dotB1' }));
    defs.appendChild(rgB);
    svg.appendChild(defs);
    return id;
  }
  function fmt(n) { return (Math.round(n * 100) / 100).toLocaleString('en-IN'); }

  // Re-render on width change (debounced). drawFn(W) returns an <svg>.
  function responsive(mount, drawFn) {
    var last = -1, raf;
    function paint() {
      var W = Math.max(260, Math.floor(mount.getBoundingClientRect().width || mount.clientWidth || 320));
      if (W === last) return;
      last = W;
      mount.textContent = '';
      mount.appendChild(drawFn(W));
    }
    paint();
    if ('ResizeObserver' in window) {
      var ro = new ResizeObserver(function () { cancelAnimationFrame(raf); raf = requestAnimationFrame(paint); });
      ro.observe(mount);
    } else {
      window.addEventListener('resize', function () { cancelAnimationFrame(raf); raf = requestAnimationFrame(paint); });
    }
  }

  function attachTip(node, html) {
    node.style.cursor = 'default';
    node.addEventListener('mousemove', function (e) { showTip(html, e); });
    node.addEventListener('mouseleave', hideTip);
  }

  /* ============ HORIZONTAL BAR CHART ============
     opts: { data:[{label,value,hl?}], max, ticks:[…], avg:{value,label},
             suffix?, tipLabel?, valueFmt?(v) } */
  function barChart(mount, opts) {
    responsive(mount, function (W) {
      var data = opts.data, max = opts.max, suffix = opts.suffix != null ? opts.suffix : '%';
      var vfmt = opts.valueFmt || function (v) { return fmt(v) + suffix; };
      var compact = W < 520;
      var padR = compact ? 14 : 16, padL = compact ? 14 : 16;
      var rowH = compact ? 50 : 40, padTop = 30, padBottom = 30;
      var labelW = compact ? 0 : Math.min(150, Math.max(96, W * 0.22));
      var H = padTop + data.length * rowH + padBottom;
      var x0 = padL + labelW, x1 = W - padR;
      var barH = compact ? 20 : 22;
      var scale = function (v) { return x0 + (v / max) * (x1 - x0); };
      var svg = svgRoot(W, H);
      var gid = addDefs(svg);

      // gridlines + ticks (skip on very narrow compact to reduce clutter)
      (opts.ticks || []).forEach(function (t) {
        var x = scale(t);
        svg.appendChild(el('line', { x1: x, y1: padTop - 6, x2: x, y2: padTop + data.length * rowH, class: 'dv-grid-line' }));
        svg.appendChild(el('text', { x: x, y: padTop + data.length * rowH + 18, 'text-anchor': 'middle', class: 'dv-tick' }, t + suffix));
      });
      svg.appendChild(el('line', { x1: x0, y1: padTop - 6, x2: x0, y2: padTop + data.length * rowH, class: 'dv-axis-line' }));

      data.forEach(function (d, i) {
        var y = padTop + i * rowH;
        var g = el('g', { class: 'dv-bargroup' });
        var by, bw = Math.max(0, scale(d.value) - x0);
        if (compact) {
          // name (left) + value (right) on one line, full-width track below
          by = y + 22;
          g.appendChild(el('text', { x: x0, y: y + 14, 'text-anchor': 'start', class: 'dv-bar-lbl' }, d.label));
          g.appendChild(el('text', { x: x1, y: y + 14, 'text-anchor': 'end', class: 'dv-bar-val' }, vfmt(d.value)));
        } else {
          by = y + (rowH - barH) / 2;
          g.appendChild(el('text', { x: x0 - 10, y: by + 15, 'text-anchor': 'end', class: 'dv-bar-lbl' }, d.label));
        }
        g.appendChild(el('rect', { x: x0, y: by, width: x1 - x0, height: barH, rx: 5, class: 'dv-bar-track' }));
        var bar = el('rect', { x: x0, y: by, width: bw, height: barH, rx: 5, class: 'dv-bar dv-anim-bar' + (d.hl ? ' hl' : '') });
        bar.style.fill = 'url(#' + gid + (d.hl ? '-hl' : '-a') + ')';
        bar.style.animationDelay = (i * 0.06) + 's';
        g.appendChild(bar);
        if (!compact) {
          // value label at bar end — inside (white) if it would overflow the canvas
          var vx = scale(d.value) + 8, anchor = 'start';
          if (vx > x1 - 30) { vx = scale(d.value) - 8; anchor = 'end'; }
          g.appendChild(el('text', { x: vx, y: by + 15, 'text-anchor': anchor, class: 'dv-bar-val' + (vx < scale(d.value) ? ' inside' : '') }, vfmt(d.value)));
        }
        attachTip(g, '<b>' + d.label + '</b><br>' + (opts.tipLabel || 'Value') + ': ' + vfmt(d.value));
        svg.appendChild(g);
      });

      if (opts.avg) {
        var ax = scale(opts.avg.value);
        svg.appendChild(el('line', { x1: ax, y1: padTop - 12, x2: ax, y2: padTop + data.length * rowH + 2, class: 'dv-ref-line' }));
        svg.appendChild(el('text', { x: Math.min(ax, W - 6), y: padTop - 16, 'text-anchor': ax > W * 0.6 ? 'end' : 'middle', class: 'dv-ref-lbl' }, opts.avg.label));
      }
      return svg;
    });
  }

  /* ============ SCATTER ============
     opts: { data:[{label,x,y,anchor?,vpos?}], xMin,xMax,yMax, xTicks,yTicks,
             xTitle, yTitle, xSuffix?, tipX?, tipY? } */
  function scatterChart(mount, opts) {
    responsive(mount, function (W) {
      var compact = W < 520;
      var data = opts.data;
      var H = Math.round(Math.max(300, Math.min(460, W * (compact ? 0.95 : 0.66))));
      var padL = compact ? 44 : 60, padR = 20, padT = 22, padB = 54;
      var xMin = opts.xMin, xMax = opts.xMax, yMin = (opts.yMin != null ? opts.yMin : 0), yMax = opts.yMax;
      var xs = opts.xSuffix != null ? opts.xSuffix : '%';
      var px = function (v) { return padL + (v - xMin) / (xMax - xMin) * (W - padL - padR); };
      var py = function (v) { return H - padB - (v - yMin) / (yMax - yMin) * (H - padT - padB); };
      var svg = svgRoot(W, H);
      var gid = addDefs(svg);

      (opts.yTicks || []).forEach(function (t) {
        var y = py(t);
        svg.appendChild(el('line', { x1: padL, y1: y, x2: W - padR, y2: y, class: 'dv-grid-line' }));
        svg.appendChild(el('text', { x: padL - 8, y: y + 4, 'text-anchor': 'end', class: 'dv-tick' }, t));
      });
      (opts.xTicks || []).forEach(function (t) {
        svg.appendChild(el('text', { x: px(t), y: H - padB + 18, 'text-anchor': 'middle', class: 'dv-tick' }, t + xs));
      });
      svg.appendChild(el('line', { x1: padL, y1: padT, x2: padL, y2: H - padB, class: 'dv-axis-line' }));
      svg.appendChild(el('line', { x1: padL, y1: H - padB, x2: W - padR, y2: H - padB, class: 'dv-axis-line' }));
      // zero baseline (when values cross zero) and optional vertical reference
      if (yMin < 0) svg.appendChild(el('line', { x1: padL, y1: py(0), x2: W - padR, y2: py(0), class: 'dv-axis-line' }));
      if (opts.xRef != null) {
        var rx = px(opts.xRef);
        svg.appendChild(el('line', { x1: rx, y1: padT, x2: rx, y2: H - padB, class: 'dv-ref-line' }));
        if (opts.xRefLabel) svg.appendChild(el('text', { x: rx, y: padT - 6, 'text-anchor': 'middle', class: 'dv-ref-lbl' }, opts.xRefLabel));
      }
      if (opts.xTitle) svg.appendChild(el('text', { x: (padL + W - padR) / 2, y: H - 10, 'text-anchor': 'middle', class: 'dv-axis-title' }, opts.xTitle));
      if (opts.yTitle) {
        var cy = (padT + H - padB) / 2;
        svg.appendChild(el('text', { x: 14, y: cy, 'text-anchor': 'middle', class: 'dv-axis-title', transform: 'rotate(-90 14 ' + cy + ')' }, opts.yTitle));
      }

      var many = data.length > 20;
      data.forEach(function (d) {
        var cx = px(d.x), cy = py(d.y);
        var g = el('g');
        var dot = el('circle', { cx: cx, cy: cy, r: d.big ? 9 : (many ? 6 : 9), class: 'dv-dot dv-anim-dot' + (d.hl ? ' hl' : '') });
        dot.style.fill = 'url(#' + gid + (d.hl ? '-dotB' : '-dotA') + ')';
        g.appendChild(dot);
        if (d.label) {
          var anchor = d.anchor || (d.x > (xMin + xMax) / 2 ? 'end' : 'start');
          var lx = anchor === 'end' ? cx - 12 : cx + 12;
          var nameY = d.vpos === 'down' ? cy + 18 : cy - 16;
          g.appendChild(el('text', { x: lx, y: nameY, 'text-anchor': anchor, class: 'dv-dot-lbl' }, d.label));
          if (d.sub !== false)
            g.appendChild(el('text', { x: lx, y: d.vpos === 'down' ? cy + 31 : cy - 3, 'text-anchor': anchor, class: 'dv-dot-sub' }, fmt(d.x) + xs + ' · ' + fmt(d.y)));
        }
        attachTip(g, '<b>' + (d.name || d.label || '') + '</b><br>' + (opts.tipX || 'x') + ': ' + fmt(d.x) + xs + '<br>' + (opts.tipY || 'y') + ': ' + fmt(d.y));
        svg.appendChild(g);
      });
      return svg;
    });
  }

  /* ============ DUMBBELL (two values per row, connected) ============
     opts: { data:[{label, a, b}], max, aLabel, bLabel, suffix?, ticks?, valueFmt? } */
  function dumbbellChart(mount, opts) {
    responsive(mount, function (W) {
      var data = opts.data, max = opts.max, suffix = opts.suffix != null ? opts.suffix : '';
      var vfmt = opts.valueFmt || function (v) { return fmt(v) + suffix; };
      var compact = W < 520;
      var padR = 16, padL = 16, rowH = compact ? 56 : 44, padTop = 34, padBottom = 30;
      var labelW = compact ? 0 : Math.min(150, Math.max(96, W * 0.22));
      var H = padTop + data.length * rowH + padBottom;
      var x0 = padL + labelW, x1 = W - padR;
      var scale = function (v) { return x0 + (v / max) * (x1 - x0); };
      var svg = svgRoot(W, H);

      (opts.ticks || []).forEach(function (t) {
        var x = scale(t);
        svg.appendChild(el('line', { x1: x, y1: padTop - 6, x2: x, y2: padTop + data.length * rowH, class: 'dv-grid-line' }));
        svg.appendChild(el('text', { x: x, y: padTop + data.length * rowH + 18, 'text-anchor': 'middle', class: 'dv-tick' }, vfmt(t)));
      });

      var gid = addDefs(svg);
      // legend
      var lg = el('g');
      lg.appendChild(el('circle', { cx: x0 + 6, cy: padTop - 18, r: 6, class: 'dv-dumb-a' }));
      lg.appendChild(el('text', { x: x0 + 18, y: padTop - 14, 'text-anchor': 'start', class: 'dv-legend' }, opts.aLabel));
      var bx = x0 + 26 + (opts.aLabel.length * 7);
      lg.appendChild(el('circle', { cx: bx, cy: padTop - 18, r: 6, class: 'dv-dumb-b' }));
      lg.appendChild(el('text', { x: bx + 12, y: padTop - 14, 'text-anchor': 'start', class: 'dv-legend' }, opts.bLabel));
      svg.appendChild(lg);

      data.forEach(function (d, i) {
        var y = padTop + i * rowH, g = el('g');
        var cy;
        if (compact) { cy = y + 30; svg.appendChild(el('text', { x: x0, y: y + 14, 'text-anchor': 'start', class: 'dv-bar-lbl' }, d.label)); }
        else { cy = y + rowH / 2; g.appendChild(el('text', { x: x0 - 10, y: cy + 4, 'text-anchor': 'end', class: 'dv-bar-lbl' }, d.label)); }
        var ax = scale(d.a), bx2 = scale(d.b);
        g.appendChild(el('line', { x1: ax, y1: cy, x2: bx2, y2: cy, pathLength: '1', class: 'dv-dumb-line dv-anim-line' }));
        var da = el('circle', { cx: ax, cy: cy, r: 8, class: 'dv-dumb-a dv-anim-dot' });
        da.style.fill = 'url(#' + gid + '-dotA)';
        var db = el('circle', { cx: bx2, cy: cy, r: 8, class: 'dv-dumb-b dv-anim-dot' });
        db.style.fill = 'url(#' + gid + '-dotB)';
        g.appendChild(da); g.appendChild(db);
        // value labels at the outer ends
        var lo = Math.min(ax, bx2), hi = Math.max(ax, bx2);
        g.appendChild(el('text', { x: lo - 9, y: cy + 4, 'text-anchor': 'end', class: 'dv-dumb-val' }, vfmt(Math.min(d.a, d.b))));
        g.appendChild(el('text', { x: hi + 9, y: cy + 4, 'text-anchor': 'start', class: 'dv-dumb-val' }, vfmt(Math.max(d.a, d.b))));
        attachTip(g, '<b>' + d.label + '</b><br>' + opts.aLabel + ': ' + vfmt(d.a) + '<br>' + opts.bLabel + ': ' + vfmt(d.b));
        svg.appendChild(g);
      });
      return svg;
    });
  }

  /* ============ LINE CHART (1-2 series over an ordered x) ============
     opts: { series:[{name, color?('a'|'b'), points:[{x,y}]}], xLabels:[…],
             yMax, yMin?, yTicks, yFmt?, xTitle?, yTitle? }  (x is category index) */
  function lineChart(mount, opts) {
    responsive(mount, function (W) {
      var compact = W < 520;
      var H = Math.round(Math.max(280, Math.min(420, W * (compact ? 0.8 : 0.56))));
      var padL = compact ? 44 : 56, padR = 18, padT = 24, padB = 46;
      var labels = opts.xLabels, n = labels.length;
      var yMin = opts.yMin || 0, yMax = opts.yMax;
      var yFmt = opts.yFmt || function (v) { return fmt(v); };
      var xAt = function (i) { return padL + (n === 1 ? 0.5 : i / (n - 1)) * (W - padL - padR); };
      var yAt = function (v) { return H - padB - (v - yMin) / (yMax - yMin) * (H - padT - padB); };
      var svg = svgRoot(W, H);
      var gid = addDefs(svg);

      (opts.yTicks || []).forEach(function (t) {
        var y = yAt(t);
        svg.appendChild(el('line', { x1: padL, y1: y, x2: W - padR, y2: y, class: 'dv-grid-line' }));
        svg.appendChild(el('text', { x: padL - 8, y: y + 4, 'text-anchor': 'end', class: 'dv-tick' }, yFmt(t)));
      });
      // x labels (thin on compact)
      var step = compact && n > 5 ? Math.ceil(n / 5) : 1;
      labels.forEach(function (lb, i) {
        if (i % step !== 0 && i !== n - 1) return;
        svg.appendChild(el('text', { x: xAt(i), y: H - padB + 18, 'text-anchor': i === 0 ? 'start' : (i === n - 1 ? 'end' : 'middle'), class: 'dv-tick' }, lb));
      });
      svg.appendChild(el('line', { x1: padL, y1: padT, x2: padL, y2: H - padB, class: 'dv-axis-line' }));
      svg.appendChild(el('line', { x1: padL, y1: H - padB, x2: W - padR, y2: H - padB, class: 'dv-axis-line' }));
      if (opts.yTitle) { var cy = (padT + H - padB) / 2; svg.appendChild(el('text', { x: 13, y: cy, 'text-anchor': 'middle', class: 'dv-axis-title', transform: 'rotate(-90 13 ' + cy + ')' }, opts.yTitle)); }

      opts.series.forEach(function (s, si) {
        var cls = s.color === 'b' ? 'dv-line-b' : 'dv-line-a';
        var lineD = s.points.map(function (p, i) { return (i ? 'L' : 'M') + xAt(p.x) + ' ' + yAt(p.y); }).join(' ');
        if (s.area) {
          var first = s.points[0], last = s.points[s.points.length - 1];
          var areaD = lineD + ' L' + xAt(last.x) + ' ' + yAt(yMin) + ' L' + xAt(first.x) + ' ' + yAt(yMin) + ' Z';
          var ar = el('path', { d: areaD, class: 'dv-area dv-anim-area' });
          ar.style.fill = 'url(#' + gid + (s.color === 'b' ? '-areaB' : '-area') + ')';
          svg.appendChild(ar);
        }
        svg.appendChild(el('path', { d: lineD, fill: 'none', pathLength: '1', class: cls + ' dv-anim-line' }));
        s.points.forEach(function (p) {
          var mk = el('circle', { cx: xAt(p.x), cy: yAt(p.y), r: 5, class: cls + '-dot dv-anim-dot' });
          attachTip(mk, '<b>' + s.name + '</b><br>' + labels[p.x] + ': ' + yFmt(p.y));
          svg.appendChild(mk);
        });
        // direct end-label
        var last = s.points[s.points.length - 1];
        svg.appendChild(el('text', { x: xAt(last.x) - 2, y: yAt(last.y) - 8, 'text-anchor': 'end', class: cls + '-lbl' }, s.name));
      });
      return svg;
    });
  }


  /* ============ SANKEY / FLOW DIAGRAM ============
     A quantity that splits, merges, or gets absorbed. Use it only when the flow is
     the point -- a Sankey is a poor bar chart, and a good bar chart is a poor Sankey.

     opts: {
       nodes: [{ id, label, col, tone?, note? }]   // col = 0-based column index
       links: [{ source, target, value, tone? }]   // tone: 'a' | 'b' | 'in' | 'out'
       unit?: string                                // appended to every value
       valueFmt?: fn(v)                             // overrides unit
       height?: number                              // plot height, default 460
       nodeWidth?: number, gap?: number             // px
       minLabel?: number                            // hide value labels below this share
     }
     Node value is max(inflow, outflow), so a node that only receives or only sends
     is sized by the side that exists. Columns are scaled independently to the same
     plot height; a column carrying less total value gets thinner ribbons, which is
     the honest rendering -- the alternative (scale each column to fill) would make
     unequal totals look equal. */
  function sankeyChart(mount, opts) {
    // A Sankey squeezed below ~460px stops being a Sankey: the ribbons compress
    // into a band and the shape -- which is the entire reason to use this form --
    // is gone. Below that, draw at 460 and let the reader pan, rather than
    // rendering something that technically fits and says nothing.
    // Only a multi-column flow needs the floor; a 2-column chart reads fine
    // at any width and should not be given a pointless scrollbar.
    var maxCol = 0;
    opts.nodes.forEach(function (n) { if (n.col > maxCol) maxCol = n.col; });
    var MINW = (maxCol >= 2) ? (opts.minWidth || 460) : 0;
    mount.classList.add('dv-sankey-scroll');
    responsive(mount, function (W0) {
      var W = Math.max(W0, MINW);
      var inner = W > W0;
      if (inner) mount.classList.add('dv-sankey-panning');
      else mount.classList.remove('dv-sankey-panning');
      var unit = opts.unit || '';
      var vfmt = opts.valueFmt || function (v) { return fmt(v) + unit; };
      var narrow = W < 560;
      var H = opts.height || (narrow ? 520 : 460);
      var NW = opts.nodeWidth || (narrow ? 10 : 14);
      var GAP = opts.gap || 14;
      var padT = 18, padB = 18;
      var labelPad = narrow ? 6 : 10;

      var svg = svgRoot(W, H);
      // svgRoot sets width:100%, which would shrink the drawing back to the
      // container and defeat the floor. Pin the real width when panning.
      if (inner) svg.style.width = W + 'px';
      var byId = {};
      opts.nodes.forEach(function (n) { byId[n.id] = { def: n, in: 0, out: 0 }; });
      opts.links.forEach(function (l) {
        if (!byId[l.source] || !byId[l.target]) return;
        byId[l.source].out += l.value;
        byId[l.target].in += l.value;
      });

      // columns, in declared order within each
      var cols = [];
      opts.nodes.forEach(function (n) {
        (cols[n.col] = cols[n.col] || []).push(byId[n.id]);
      });
      cols.forEach(function (c) {
        c.forEach(function (nd) { nd.value = Math.max(nd.in, nd.out); });
      });

      // one shared value->px scale across all columns, so ribbon thickness is
      // comparable everywhere on the chart
      var maxColTotal = 0;
      cols.forEach(function (c) {
        var t = 0; c.forEach(function (nd) { t += nd.value; });
        if (t > maxColTotal) maxColTotal = t;
      });
      var tallest = 0;
      cols.forEach(function (c) { if (c.length > tallest) tallest = c.length; });
      var avail = H - padT - padB - (tallest - 1) * GAP;
      var vscale = maxColTotal > 0 ? avail / maxColTotal : 1;

      // horizontal placement: reserve room for the outermost labels
      // The outer margins are sized from the LONGEST label actually in the first
      // and last columns. A fixed reserve clips "Current account deficit" and
      // leaves acres of dead space next to "GST". Capped at 38% of width per
      // side so the ribbons never get squeezed out on a narrow screen.
      var nCols = cols.length;
      var charW = narrow ? 5.6 : 6.5;    // ~12px Inter semibold
      var charWv = narrow ? 5.4 : 6.3;   // ~11px JetBrains Mono
      function widest(c) {
        // Measure the VALUE line too: "Total" is 5 characters but "40.5 lakh cr"
        // is 12, and it is the value that gets clipped.
        var m = 0;
        (c || []).forEach(function (nd) {
          var t = String(nd.def.label || nd.def.id).length * charW;
          var v = String(vfmt(nd.value)).length * charWv;
          t = Math.max(t, v);
          if (t > m) m = t;
        });
        return m;
      }
      var capSide = W * 0.38;
      var sideL = Math.min(capSide, widest(cols[0]) + labelPad + 4);
      var sideR = Math.min(capSide, widest(cols[nCols - 1]) + labelPad + 4);
      var innerW = W - sideL - sideR - NW;
      var colX = function (i) { return sideL + (nCols > 1 ? (innerW * i) / (nCols - 1) : 0); };

      // vertical placement: each column centred
      cols.forEach(function (c) {
        var total = 0; c.forEach(function (nd) { total += nd.value * vscale; });
        total += (c.length - 1) * GAP;
        var y = padT + (H - padT - padB - total) / 2;
        c.forEach(function (nd) {
          nd.y0 = y; nd.h = Math.max(1, nd.value * vscale); nd.y1 = y + nd.h;
          y += nd.h + GAP;
          nd.outCur = nd.y0; nd.inCur = nd.y0;
        });
      });

      // ribbons first, so nodes sit on top
      var gLinks = el('g');
      opts.links.forEach(function (l) {
        var s = byId[l.source], t = byId[l.target];
        if (!s || !t) return;
        var sh = l.value * vscale, th = l.value * vscale;
        var x0 = colX(s.def.col) + NW, x1 = colX(t.def.col);
        var y0a = s.outCur, y0b = y0a + sh;
        var y1a = t.inCur, y1b = y1a + th;
        s.outCur += sh; t.inCur += th;
        var xm = (x0 + x1) / 2;
        var d = 'M' + x0 + ',' + y0a +
                ' C' + xm + ',' + y0a + ' ' + xm + ',' + y1a + ' ' + x1 + ',' + y1a +
                ' L' + x1 + ',' + y1b +
                ' C' + xm + ',' + y1b + ' ' + xm + ',' + y0b + ' ' + x0 + ',' + y0b + ' Z';
        var tone = l.tone || s.def.tone || 'a';
        var path = el('path', { d: d, class: 'dv-sankey-link dv-sankey-' + tone });
        attachTip(path, '<b>' + (s.def.label || s.def.id) + ' → ' + (t.def.label || t.def.id) +
                        '</b><br>' + vfmt(l.value));
        gLinks.appendChild(path);
      });
      svg.appendChild(gLinks);

      // nodes + labels
      var minShare = opts.minLabel != null ? opts.minLabel : 0.045;
      cols.forEach(function (c, ci) {
        c.forEach(function (nd) {
          var x = colX(ci);
          var r = el('rect', { x: x, y: nd.y0, width: NW, height: nd.h, rx: 2,
                               class: 'dv-sankey-node dv-sankey-node-' + (nd.def.tone || 'a') });
          attachTip(r, '<b>' + (nd.def.label || nd.def.id) + '</b><br>' + vfmt(nd.value) +
                       (nd.def.note ? '<br><span class="dv-tip-note">' + nd.def.note + '</span>' : ''));
          svg.appendChild(r);

          // First and last columns label into the reserved outer margins, so the
          // text never sits on a ribbon. Middle columns have nowhere clear to go --
          // their labels get a surface-coloured halo (paint-order:stroke) so they
          // stay readable wherever a ribbon runs underneath.
          var isFirst = ci === 0, isLast = ci === nCols - 1;
          var anchor, lx;
          if (isFirst) { anchor = 'end'; lx = x - labelPad; }
          else { anchor = 'start'; lx = x + NW + labelPad; }
          var mid = !isFirst && !isLast;
          var cy = nd.y0 + nd.h / 2;
          var big = nd.h >= 26;

          var g = el('g', { class: 'dv-sankey-lbl-g' });
          g.appendChild(el('text', { x: lx, y: big ? cy - 2 : cy + 4, 'text-anchor': anchor,
                                     class: 'dv-sankey-lbl' + (mid ? ' dv-sankey-halo' : '') },
                           nd.def.label || nd.def.id));
          if (big && nd.value / maxColTotal >= minShare) {
            g.appendChild(el('text', { x: lx, y: cy + 13, 'text-anchor': anchor,
                                       class: 'dv-sankey-val' + (mid ? ' dv-sankey-halo' : '') },
                             vfmt(nd.value)));
          }
          svg.appendChild(g);
        });
      });

      return svg;
    });
  }

  window.DataDive = { barChart: barChart, scatterChart: scatterChart, dumbbellChart: dumbbellChart, lineChart: lineChart, sankeyChart: sankeyChart };
})();
