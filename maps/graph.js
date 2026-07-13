/* ImpactMojo — tiny self-contained force-directed graph (no dependencies).
   Canvas-rendered, theme-aware, with zoom/pan, node drag, hover highlight,
   and click callbacks. Tuned for up to ~250 nodes (O(n^2) physics is fine
   at that scale). Used by the Content Map and the Funding Map.

   Usage:
     var g = ImpactGraph(canvasEl, {
       nodes: [{ id, label, group, val }...],
       links: [{ source, target, weight }...],
       color: function(node){ return '#...' },   // node fill
       radius: function(node){ return px },       // node radius
       onClick: function(node){},                 // node click
       onBackground: function(){},                // empty-space click
       label: function(node){ return text }       // optional label override
     });
     g.focus(nodeId);  g.reset();  g.destroy();
*/
(function () {
  function ImpactGraph(canvas, opts) {
    var ctx = canvas.getContext('2d');
    var nodes = opts.nodes.map(function (n) { return Object.assign({}, n); });
    var byId = {};
    nodes.forEach(function (n) { byId[n.id] = n; });
    var links = opts.links
      .map(function (l) { return { source: byId[l.source], target: byId[l.target], weight: l.weight || 1 }; })
      .filter(function (l) { return l.source && l.target; });

    // adjacency for hover highlight
    var adj = {};
    nodes.forEach(function (n) { adj[n.id] = {}; });
    links.forEach(function (l) { adj[l.source.id][l.target.id] = 1; adj[l.target.id][l.source.id] = 1; });

    var colorOf = opts.color || function () { return '#2563EB'; };
    var radiusOf = opts.radius || function () { return 6; };
    var labelOf = opts.label || function (n) { return n.label != null ? n.label : n.id; };

    var W = 0, H = 0, DPR = Math.min(window.devicePixelRatio || 1, 2);
    var view = { k: 1, x: 0, y: 0 };            // zoom + pan
    var hovered = null, dragging = null, panning = false;
    var last = { x: 0, y: 0 };
    var alpha = 1, raf = null;

    function size() {
      var r = canvas.getBoundingClientRect();
      W = Math.max(320, r.width); H = Math.max(320, r.height);
      canvas.width = W * DPR; canvas.height = H * DPR;
      ctx.setTransform(DPR, 0, 0, DPR, 0, 0);
    }

    // deterministic seed layout (avoids Math.random for reproducibility)
    (function seed() {
      var n = nodes.length, R = 260;
      nodes.forEach(function (nd, i) {
        var a = (i * 2.399963); // golden-angle spiral
        var rr = R * Math.sqrt((i + 1) / n);
        nd.x = Math.cos(a) * rr; nd.y = Math.sin(a) * rr;
        nd.vx = 0; nd.vy = 0;
      });
    })();

    function tick() {
      var kRep = 900, kSpring = 0.02, kCenter = 0.012, damp = 0.86;
      for (var i = 0; i < nodes.length; i++) {
        var a = nodes[i];
        for (var j = i + 1; j < nodes.length; j++) {
          var b = nodes[j];
          var dx = a.x - b.x, dy = a.y - b.y;
          var d2 = dx * dx + dy * dy + 0.01;
          var d = Math.sqrt(d2);
          var f = kRep / d2;
          var ux = dx / d, uy = dy / d;
          a.vx += ux * f; a.vy += uy * f;
          b.vx -= ux * f; b.vy -= uy * f;
        }
      }
      links.forEach(function (l) {
        var dx = l.target.x - l.source.x, dy = l.target.y - l.source.y;
        var d = Math.sqrt(dx * dx + dy * dy) + 0.01;
        var rest = 60 + 120 / (l.weight);
        var f = kSpring * (d - rest) * Math.min(2, l.weight);
        var ux = dx / d, uy = dy / d;
        l.source.vx += ux * f; l.source.vy += uy * f;
        l.target.vx -= ux * f; l.target.vy -= uy * f;
      });
      nodes.forEach(function (n) {
        n.vx -= n.x * kCenter; n.vy -= n.y * kCenter;
        if (n === dragging) return;
        n.vx *= damp; n.vy *= damp;
        n.x += n.vx * alpha; n.y += n.vy * alpha;
      });
      alpha *= 0.985;
      if (alpha < 0.02) alpha = 0.02;
    }

    function toScreen(n) { return { x: n.x * view.k + view.x + W / 2, y: n.y * view.k + view.y + H / 2 }; }
    function toWorld(px, py) { return { x: (px - W / 2 - view.x) / view.k, y: (py - H / 2 - view.y) / view.k }; }

    function css(v) { return getComputedStyle(document.body).getPropertyValue(v).trim() || v; }

    function draw() {
      ctx.clearRect(0, 0, W, H);
      var linkCol = css('--mp-link');
      // links
      ctx.lineWidth = 1;
      links.forEach(function (l) {
        var s = toScreen(l.source), t = toScreen(l.target);
        var hot = hovered && (l.source === hovered || l.target === hovered);
        ctx.strokeStyle = linkCol;
        ctx.globalAlpha = hovered ? (hot ? 0.85 : 0.06) : Math.min(0.5, 0.14 + l.weight * 0.05);
        ctx.lineWidth = hot ? Math.min(4, 1 + l.weight * 0.6) : Math.min(2.5, 0.6 + l.weight * 0.35);
        ctx.beginPath(); ctx.moveTo(s.x, s.y); ctx.lineTo(t.x, t.y); ctx.stroke();
      });
      ctx.globalAlpha = 1;
      // nodes
      var textCol = css('--mp-text'), stroke = css('--mp-node-stroke');
      nodes.forEach(function (n) {
        var p = toScreen(n), r = radiusOf(n) * Math.sqrt(view.k);
        var dim = hovered && n !== hovered && !adj[hovered.id][n.id];
        ctx.globalAlpha = dim ? 0.2 : 1;
        ctx.beginPath(); ctx.arc(p.x, p.y, r, 0, 6.2832);
        ctx.fillStyle = colorOf(n); ctx.fill();
        ctx.lineWidth = 1.5; ctx.strokeStyle = (n === hovered) ? textCol : stroke; ctx.stroke();
      });
      // labels (larger nodes, or hovered + neighbours)
      ctx.globalAlpha = 1; ctx.textAlign = 'center'; ctx.textBaseline = 'middle';
      nodes.forEach(function (n) {
        var r = radiusOf(n) * Math.sqrt(view.k);
        var show = (r >= 11 && view.k >= 0.7) || n === hovered || (hovered && adj[hovered.id][n.id]);
        if (!show) return;
        var p = toScreen(n);
        var fs = Math.max(10, Math.min(15, r * 0.9));
        ctx.font = '600 ' + fs + "px Inter, system-ui, sans-serif";
        var txt = labelOf(n);
        ctx.lineWidth = 3; ctx.strokeStyle = css('--mp-label-halo');
        ctx.strokeText(txt, p.x, p.y + r + fs * 0.9);
        ctx.fillStyle = textCol;
        ctx.fillText(txt, p.x, p.y + r + fs * 0.9);
      });
    }

    function frame() { tick(); draw(); raf = requestAnimationFrame(frame); }

    function pick(px, py) {
      var best = null, bd = Infinity;
      for (var i = nodes.length - 1; i >= 0; i--) {
        var n = nodes[i], p = toScreen(n), r = radiusOf(n) * Math.sqrt(view.k) + 4;
        var dx = px - p.x, dy = py - p.y, d = dx * dx + dy * dy;
        if (d <= r * r && d < bd) { bd = d; best = n; }
      }
      return best;
    }

    function evtPos(e) {
      var r = canvas.getBoundingClientRect();
      var t = e.touches ? e.touches[0] : e;
      return { x: t.clientX - r.left, y: t.clientY - r.top };
    }

    function onDown(e) {
      var p = evtPos(e); var n = pick(p.x, p.y);
      if (n) { dragging = n; alpha = 0.5; } else { panning = true; }
      last = p;
    }
    function onMove(e) {
      var p = evtPos(e);
      if (dragging) {
        var w = toWorld(p.x, p.y); dragging.x = w.x; dragging.y = w.y; dragging.vx = 0; dragging.vy = 0;
        e.preventDefault && e.preventDefault();
      } else if (panning) {
        view.x += p.x - last.x; view.y += p.y - last.y; last = p;
      } else {
        var n = pick(p.x, p.y);
        if (n !== hovered) { hovered = n; canvas.style.cursor = n ? 'pointer' : 'grab';
          if (opts.onHover) opts.onHover(n); }
      }
    }
    function onUp(e) {
      var p = evtPos(e), moved = Math.abs(p.x - last.x) + Math.abs(p.y - last.y);
      if (dragging && moved < 4 && opts.onClick) opts.onClick(dragging);
      else if (panning && moved < 4) { if (opts.onBackground) opts.onBackground(); }
      dragging = null; panning = false;
    }
    function onWheel(e) {
      e.preventDefault();
      var p = evtPos(e), w = toWorld(p.x, p.y);
      var f = Math.exp(-e.deltaY * 0.0015);
      view.k = Math.max(0.25, Math.min(4, view.k * f));
      // keep cursor point stable
      view.x = p.x - W / 2 - w.x * view.k;
      view.y = p.y - H / 2 - w.y * view.k;
    }

    canvas.addEventListener('mousedown', onDown);
    window.addEventListener('mousemove', onMove);
    window.addEventListener('mouseup', onUp);
    canvas.addEventListener('touchstart', onDown, { passive: true });
    canvas.addEventListener('touchmove', onMove, { passive: false });
    canvas.addEventListener('touchend', onUp);
    canvas.addEventListener('wheel', onWheel, { passive: false });
    canvas.style.cursor = 'grab';

    var ro = ('ResizeObserver' in window) ? new ResizeObserver(size) : null;
    if (ro) ro.observe(canvas); else window.addEventListener('resize', size);
    size(); frame();

    return {
      focus: function (id) {
        var n = byId[id]; if (!n) return;
        hovered = n; view.k = 1.4; view.x = -n.x * view.k; view.y = -n.y * view.k; alpha = 0.4;
        if (opts.onClick) opts.onClick(n);
      },
      reheat: function () { alpha = 0.8; },
      reset: function () { view = { k: 1, x: 0, y: 0 }; hovered = null; alpha = 0.8; },
      setHover: function (id) { hovered = id ? byId[id] : null; },
      nodes: nodes,
      destroy: function () {
        cancelAnimationFrame(raf);
        window.removeEventListener('mousemove', onMove); window.removeEventListener('mouseup', onUp);
        if (ro) ro.disconnect();
      }
    };
  }
  window.ImpactGraph = ImpactGraph;
})();
