/* ImpactMojo — Service Worker
   ---------------------------------------------------------------------------
   Goal: real offline support WITHOUT the stale-file serving that forced the
   previous service worker to be retired.

   Strategy
   - Navigations / HTML  → network-first. Always fresh when online; falls back
     to a cached copy (or /offline.html) only when the network fails. This is
     what prevents the "stale page" bug that killed the old SW.
   - Static assets (CSS/JS/img/font/json, same-origin + known CDNs)
                         → stale-while-revalidate. Served instantly from cache
     but refreshed in the background, so a cached asset is at most one load old.
   - On activate, every cache that is not the current version is deleted, so a
     deploy can never leave stale files behind. User-downloaded course caches
     (impactmojo-course-*) are preserved across versions.
   - On-demand course download (postMessage 'CACHE_COURSE') and background sync
     of queued progress ('sync-progress') back the js/offline.js module.

   Bump VERSION on a deploy that changes cached static assets to force a clean
   purge. Even without a bump, HTML is always network-first and assets
   self-heal via revalidation, so staleness is bounded. */

'use strict';

const VERSION = 'v10-2026-08-19';
const RUNTIME = 'im-runtime-' + VERSION;
const OFFLINE_URL = '/offline.html';
const COURSE_PREFIX = 'impactmojo-course-';

// Flagship course id → entry URL (mirrors FLAGSHIP_COURSES in js/offline.js).
// Per-course URL lists: entry page + lexicon; shared assets appended in cacheCourse.
const COURSE_URLS = {
  causal: ['/courses/causal/', '/courses/causal/lexicon.html'],
  dataviz: ['/courses/dataviz/', '/courses/dataviz/lexicon.html'],
  devai: ['/courses/devai/', '/courses/devai/lexicon.html'],
  devecon: ['/courses/devecon/', '/courses/devecon/lexicon.html'],
  gandhi: ['/courses/gandhi/', '/courses/gandhi/lexicon.html'],
  gender: ['/courses/gender/', '/courses/gender/lexicon.html'],
  intervention: ['/courses/intervention/', '/courses/intervention/lexicon.html'],
  law: ['/courses/law/', '/courses/law/lexicon.html'],
  livelihoods: ['/courses/livelihoods/', '/courses/livelihoods/lexicon.html'],
  media: ['/courses/media/', '/courses/media/lexicon.html'],
  mel: ['/courses/mel/', '/courses/mel/lexicon.html'],
  "nothing-about-us": ['/courses/nothing-about-us/', '/courses/nothing-about-us/lexicon.html'],
  "nvc-rj": ['/courses/nvc-rj/', '/courses/nvc-rj/lexicon.html'],
  poa: ['/courses/poa/', '/courses/poa/lexicon.html'],
  powerBI: ['/courses/powerBI/powerbi.html', '/courses/powerBI/lexicon.html'],
  pubchoice: ['/courses/pubchoice/', '/courses/pubchoice/lexicon.html'],
  pubpol: ['/courses/pubpol/', '/courses/pubpol/lexicon.html'],
  sel: ['/courses/sel/', '/courses/sel/lexicon.html'],
};

const STATIC_RE = /\.(?:css|js|mjs|png|jpe?g|gif|svg|webp|ico|woff2?|ttf|eot|json)$/i;
// Fonts are self-hosted under /assets/fonts/ (same-origin, matched by STATIC_RE);
// only the Sargam icon CDN remains cross-origin cacheable.
const CDN_RE = /(?:cdn\.jsdelivr\.net)/;

// ── Install: precache only the offline fallback, then take over. ──
self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(RUNTIME)
      .then((cache) => cache.add(OFFLINE_URL))
      .catch(() => {})
      .then(() => self.skipWaiting())
  );
});

// ── Activate: drop old versioned caches (keep downloaded courses), claim clients. ──
self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys()
      .then((keys) => Promise.all(keys.map((key) => {
        if (key === RUNTIME) return null;
        if (key.startsWith(COURSE_PREFIX)) return null; // user downloads persist
        return caches.delete(key);
      })))
      .then(() => self.clients.claim())
  );
});

// ── Fetch routing. ──
self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return; // never touch POST/PUT/etc.

  let url;
  try { url = new URL(req.url); } catch (e) { return; }
  if (!url.protocol.startsWith('http')) return; // skip chrome-extension:, etc.

  // Always go straight to the network for backend / dynamic endpoints.
  if (url.hostname.includes('supabase') ||
      url.hostname.includes('instantdb') ||
      url.pathname.startsWith('/.netlify/') ||
      url.hostname.includes('google-analytics') ||
      url.hostname.includes('googletagmanager') ||
      url.hostname.includes('gtag')) {
    return;
  }

  const isHTML = req.mode === 'navigate' ||
    (req.headers.get('accept') || '').includes('text/html');

  if (isHTML) {
    event.respondWith(networkFirst(req));
    return;
  }

  const sameOrigin = url.origin === self.location.origin;
  if ((sameOrigin && STATIC_RE.test(url.pathname)) || CDN_RE.test(url.hostname)) {
    event.respondWith(staleWhileRevalidate(req));
  }
  // Everything else falls through to the network (browser default).
});

// Network-first: fresh online, cached (or offline page) when the network fails.
function networkFirst(req) {
  return fetch(req)
    .then((res) => {
      if (res && res.ok) {
        const copy = res.clone();
        caches.open(RUNTIME).then((c) => c.put(req, copy)).catch(() => {});
      }
      return res;
    })
    .catch(() => caches.match(req).then((cached) => cached || caches.match(OFFLINE_URL)));
}

// Stale-while-revalidate: serve cache, refresh in the background.
function staleWhileRevalidate(req) {
  return caches.open(RUNTIME).then((cache) =>
    cache.match(req).then((cached) => {
      const network = fetch(req)
        .then((res) => {
          if (res && (res.ok || res.type === 'opaque')) cache.put(req, res.clone());
          return res;
        })
        .catch(() => cached);
      return cached || network;
    })
  );
}

// ── Messages from the page (js/offline.js). ──
self.addEventListener('message', (event) => {
  const data = event.data || {};
  if (data.type === 'SKIP_WAITING') {
    self.skipWaiting();
  } else if (data.type === 'CACHE_COURSE' && data.courseId) {
    event.waitUntil(cacheCourse(data.courseId));
  }
});

function postAll(message) {
  return self.clients.matchAll().then((clients) => {
    clients.forEach((client) => client.postMessage(message));
  });
}

// Download a course's entry page for offline reading. Shared CSS/JS are picked
// up by stale-while-revalidate while the user browses online, and caches.match
// in networkFirst searches every cache (including this one) when offline.
const COURSE_SHARED_ASSETS = ["/js/course-loader.js", "/js/course-progress.js", "/js/site-chrome.js", "/js/theme.js", "/js/config.js", "/js/offline.js", "/css/fonts.css"];

function cacheCourse(courseId) {
  const base = COURSE_URLS[courseId];
  if (!base) {
    return postAll({ type: 'COURSE_CACHE_ERROR', courseId: courseId, error: 'Unknown course' });
  }
  return caches.open(COURSE_PREFIX + courseId).then((cache) => {
    const courseUrls = Array.isArray(base) ? base : [base];
    const urls = courseUrls.concat(COURSE_SHARED_ASSETS, [OFFLINE_URL]);
    let completed = 0;
    return urls.reduce((chain, u) => chain.then(() =>
      fetch(u, { cache: 'reload' })
        .then((res) => { if (res && res.ok) return cache.put(u, res.clone()); })
        .catch(() => {})
        .then(() => {
          completed++;
          return postAll({
            type: 'COURSE_CACHE_PROGRESS',
            courseId: courseId,
            completed: completed,
            total: urls.length,
            progress: Math.round((completed / urls.length) * 100)
          });
        })
    ), Promise.resolve())
      .then(() => postAll({ type: 'COURSE_CACHE_COMPLETE', courseId: courseId }))
      .catch((err) => postAll({ type: 'COURSE_CACHE_ERROR', courseId: courseId, error: String(err) }));
  });
}

// ── Web push: show a notification, and focus/open on click. ──
self.addEventListener('push', (event) => {
  let data = {};
  try { data = event.data ? event.data.json() : {}; }
  catch (e) { data = { title: 'ImpactMojo', body: event.data ? event.data.text() : '' }; }

  const title = data.title || 'ImpactMojo';
  const options = {
    body: data.body || '',
    icon: '/assets/images/android-chrome-192x192.png',
    badge: '/assets/images/favicon-32x32.png',
    data: { link: data.link || '/' },
    tag: data.tag || undefined,
    renotify: !!data.tag
  };
  event.waitUntil(self.registration.showNotification(title, options));
});

self.addEventListener('notificationclick', (event) => {
  event.notification.close();
  const link = (event.notification.data && event.notification.data.link) || '/';
  const target = new URL(link, self.location.origin).href;
  event.waitUntil(
    self.clients.matchAll({ type: 'window', includeUncontrolled: true }).then((clients) => {
      for (const client of clients) {
        if (client.url === target && 'focus' in client) return client.focus();
      }
      return self.clients.openWindow ? self.clients.openWindow(target) : undefined;
    })
  );
});

// ── Background sync: replay progress POSTs queued by js/offline.js. ──
self.addEventListener('sync', (event) => {
  if (event.tag === 'sync-progress') {
    event.waitUntil(replayQueuedProgress());
  }
});

function idbOpen() {
  return new Promise((resolve, reject) => {
    const r = indexedDB.open('ImpactMojoOffline', 1);
    r.onupgradeneeded = () => {
      const db = r.result;
      if (!db.objectStoreNames.contains('pendingSync')) {
        db.createObjectStore('pendingSync', { keyPath: 'id', autoIncrement: true });
      }
    };
    r.onsuccess = () => resolve(r.result);
    r.onerror = () => reject(r.error);
  });
}

function idbGetAll(db) {
  return new Promise((resolve, reject) => {
    const tx = db.transaction('pendingSync', 'readonly');
    const req = tx.objectStore('pendingSync').getAll();
    req.onsuccess = () => resolve(req.result || []);
    req.onerror = () => reject(req.error);
  });
}

function idbDelete(db, id) {
  return new Promise((resolve) => {
    const tx = db.transaction('pendingSync', 'readwrite');
    tx.objectStore('pendingSync').delete(id);
    tx.oncomplete = () => resolve();
    tx.onerror = () => resolve();
  });
}

function replayQueuedProgress() {
  return idbOpen().then((db) =>
    idbGetAll(db).then((items) =>
      items.reduce((chain, item) => chain.then(() =>
        fetch(item.url, {
          method: item.method || 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(item.data)
        })
          .then((res) => { if (res && res.ok) return idbDelete(db, item.id); })
          .catch(() => {}) // keep queued for the next sync
      ), Promise.resolve())
    )
  );
}
