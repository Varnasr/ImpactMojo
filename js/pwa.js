// ImpactMojo — Service Worker registration
// Registers /service-worker.js for offline support. The SW itself is
// network-first for HTML and stale-while-revalidate for assets, so this never
// reintroduces the stale-file problem that the old "unregister" stub fixed.
// When a new SW is installed while an old one controls the page, we ask it to
// activate immediately so users always run the latest version.
(function () {
  'use strict';
  if (!('serviceWorker' in navigator)) return;

  window.addEventListener('load', function () {
    navigator.serviceWorker.register('/service-worker.js').then(function (reg) {
      reg.addEventListener('updatefound', function () {
        var incoming = reg.installing;
        if (!incoming) return;
        incoming.addEventListener('statechange', function () {
          // A new SW finished installing and an old one is still in control —
          // tell it to skip waiting so the fresh version takes over promptly.
          if (incoming.state === 'installed' && navigator.serviceWorker.controller) {
            incoming.postMessage({ type: 'SKIP_WAITING' });
          }
        });
      });
    }).catch(function (err) {
      if (window.console) console.warn('ImpactMojo SW registration failed:', err);
    });
  });
})();
