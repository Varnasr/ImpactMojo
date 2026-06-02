/* ImpactMojo — Daily Spotlight
   Deterministic, date-seeded rotation so a fully static site can feature a
   different item every day (testimonial / deep dive / game / case study…)
   without any backend. Same item for everyone on a given calendar day. */
(function (global) {
  function dayIndex() {
    var n = new Date();
    return Math.floor(Date.UTC(n.getFullYear(), n.getMonth(), n.getDate()) / 86400000);
  }
  function pick(arr) { return (arr && arr.length) ? arr[dayIndex() % arr.length] : null; }
  function shuffle(arr) {            // deterministic per-day order
    var a = arr.slice(), seed = dayIndex() % 233280 || 1;
    function rnd() { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }
    for (var i = a.length - 1; i > 0; i--) { var j = Math.floor(rnd() * (i + 1)); var t = a[i]; a[i] = a[j]; a[j] = t; }
    return a;
  }
  global.IMXSpotlight = { dayIndex: dayIndex, pick: pick, shuffle: shuffle };
})(window);
