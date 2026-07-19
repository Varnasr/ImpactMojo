/* Live platform stats — fills any element carrying data-live-stat with a
 * number from the get_public_stats() Supabase RPC (aggregate-only, anon-safe).
 *
 *   <span data-live-stat="practitioners_total" data-suffix="+">13,000+</span>
 *
 * The hardcoded text stays as the no-JS/offline fallback; when the RPC
 * responds, the text is replaced with the live figure. Keys: any top-level
 * numeric field of the RPC response (practitioners_total, registered_learners,
 * certificates_issued, ...). Response is cached in sessionStorage for an hour
 * so navigation doesn't refetch.
 */
(function () {
    'use strict';

    var els = document.querySelectorAll('[data-live-stat]');
    if (!els.length) return;

    var CACHE_KEY = 'im-live-stats';
    var CACHE_MS = 60 * 60 * 1000;

    function fmt(n) {
        try { return Number(n).toLocaleString('en-IN'); }
        catch (e) { return String(n); }
    }

    function apply(stats) {
        els.forEach(function (el) {
            var key = el.getAttribute('data-live-stat');
            var val = stats[key];
            if (typeof val === 'number' && isFinite(val) && val > 0) {
                el.textContent = fmt(val) + (el.getAttribute('data-suffix') || '');
            }
        });
    }

    try {
        var cached = JSON.parse(sessionStorage.getItem(CACHE_KEY) || 'null');
        if (cached && cached.t && (Date.now() - cached.t) < CACHE_MS && cached.v) {
            apply(cached.v);
            return;
        }
    } catch (e) { /* fall through to fetch */ }

    var cfg = window.ImpactMojoConfig;
    if (!cfg || !cfg.SUPABASE_URL || !cfg.SUPABASE_ANON_KEY) return;

    fetch(cfg.SUPABASE_URL + '/rest/v1/rpc/get_public_stats', {
        method: 'POST',
        headers: {
            'apikey': cfg.SUPABASE_ANON_KEY,
            'Authorization': 'Bearer ' + cfg.SUPABASE_ANON_KEY,
            'Content-Type': 'application/json'
        },
        body: '{}'
    }).then(function (r) { return r.ok ? r.json() : null; })
      .then(function (stats) {
          if (!stats) return;
          apply(stats);
          try { sessionStorage.setItem(CACHE_KEY, JSON.stringify({ t: Date.now(), v: stats })); } catch (e) {}
      }).catch(function () { /* fallback text stays */ });
})();
