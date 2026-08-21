// ImpactMojo Offline Module
// Provides course download, cache checking, and offline/online status indicators
(function () {
  'use strict';

  const COURSE_CACHE_PREFIX = 'impactmojo-course-';

  const FLAGSHIP_COURSES = [
    'gandhi', 'devecon', 'devai', 'dataviz',
    'mel', 'poa', 'media', 'law', 'SEL',
    'gender', 'pubchoice', 'pubpol', 'causal', 'livelihoods', 'powerBI',
    'intervention', 'nothing-about-us', 'nvc-rj', 'esg'
  ];

  // ─── Toast notification helper ───
  function showToast(message, type) {
    type = type || 'info';
    // Remove existing toast if present
    const existing = document.getElementById('impactmojo-offline-toast');
    if (existing) existing.remove();

    const toast = document.createElement('div');
    toast.id = 'impactmojo-offline-toast';
    toast.textContent = message;

    const colors = {
      info: '#2196F3',
      success: '#4CAF50',
      error: '#f44336',
      warning: '#ff9800',
      progress: '#673AB7'
    };

    Object.assign(toast.style, {
      position: 'fixed',
      bottom: '20px',
      left: '50%',
      transform: 'translateX(-50%)',
      background: colors[type] || colors.info,
      color: '#fff',
      padding: '12px 24px',
      borderRadius: '8px',
      fontSize: '14px',
      fontWeight: '500',
      zIndex: '99999',
      boxShadow: '0 4px 12px rgba(0,0,0,0.3)',
      transition: 'opacity 0.3s ease',
      maxWidth: '90vw',
      textAlign: 'center'
    });

    document.body.appendChild(toast);

    // Auto-dismiss after 4 seconds (except progress)
    if (type !== 'progress') {
      setTimeout(function () {
        toast.style.opacity = '0';
        setTimeout(function () { toast.remove(); }, 300);
      }, 4000);
    }
  }

  // ─── Offline/Online status indicator ───
  function createStatusIndicator() {
    const indicator = document.createElement('div');
    indicator.id = 'impactmojo-offline-indicator';
    Object.assign(indicator.style, {
      position: 'fixed',
      top: '10px',
      right: '10px',
      padding: '6px 14px',
      borderRadius: '20px',
      fontSize: '12px',
      fontWeight: '600',
      zIndex: '99998',
      transition: 'opacity 0.3s ease, transform 0.3s ease',
      pointerEvents: 'none'
    });
    document.body.appendChild(indicator);
    return indicator;
  }

  function updateStatusIndicator(online) {
    var indicator = document.getElementById('impactmojo-offline-indicator');
    if (!indicator) indicator = createStatusIndicator();

    if (online) {
      indicator.textContent = 'Online';
      indicator.style.background = '#4CAF50';
      indicator.style.color = '#fff';
      indicator.style.opacity = '1';
      // Fade out after 2 seconds when online
      setTimeout(function () { indicator.style.opacity = '0'; }, 2000);
    } else {
      indicator.textContent = 'Offline';
      indicator.style.background = '#f44336';
      indicator.style.color = '#fff';
      indicator.style.opacity = '1';
    }
  }

  // ─── Initialize online/offline listeners ───
  function initStatusListeners() {
    window.addEventListener('online', function () {
      updateStatusIndicator(true);
      showToast('You are back online', 'success');
    });

    window.addEventListener('offline', function () {
      updateStatusIndicator(false);
      showToast('You are offline. Downloaded courses are still available.', 'warning');
    });

    // Listen for SW messages
    if (navigator.serviceWorker) {
      navigator.serviceWorker.addEventListener('message', function (event) {
        var data = event.data;
        if (!data) return;

        switch (data.type) {
          case 'COURSE_CACHE_PROGRESS':
            showToast('Downloading course: ' + data.progress + '% (' + data.completed + '/' + data.total + ')', 'progress');
            break;
          case 'COURSE_CACHE_COMPLETE':
            showToast('Course "' + data.courseId + '" is now available offline!', 'success');
            break;
          case 'COURSE_CACHE_ERROR':
            showToast('Download failed: ' + (data.error || 'Unknown error'), 'error');
            break;
          case 'OFFLINE_DETECTED':
            updateStatusIndicator(false);
            break;
        }
      });
    }

    // Set initial state
    if (!navigator.onLine) {
      updateStatusIndicator(false);
    }
  }

  // ─── Download a course for offline use ───
  function downloadCourse(courseId) {
    if (!FLAGSHIP_COURSES.includes(courseId)) {
      showToast('Unknown course: ' + courseId, 'error');
      return Promise.reject(new Error('Unknown course ID: ' + courseId));
    }

    if (!navigator.serviceWorker || !navigator.serviceWorker.controller) {
      showToast('Service worker not available. Please reload the page.', 'error');
      return Promise.reject(new Error('Service worker not active'));
    }

    showToast('Starting download for "' + courseId + '"...', 'info');
    navigator.serviceWorker.controller.postMessage({
      type: 'CACHE_COURSE',
      courseId: courseId
    });

    return Promise.resolve(true);
  }

  // ─── Check if a course is cached ───
  function isCourseCached(courseId) {
    if (!('caches' in window)) {
      return Promise.resolve(false);
    }
    var cacheName = COURSE_CACHE_PREFIX + courseId;
    return caches.has(cacheName);
  }

  // ─── Remove a cached course ───
  function removeCourse(courseId) {
    if (!('caches' in window)) {
      return Promise.resolve(false);
    }
    var cacheName = COURSE_CACHE_PREFIX + courseId;
    return caches.delete(cacheName).then(function (deleted) {
      if (deleted) {
        showToast('Course "' + courseId + '" removed from offline storage.', 'info');
      }
      return deleted;
    });
  }

  // ─── List all cached courses ───
  function listCachedCourses() {
    if (!('caches' in window)) {
      return Promise.resolve([]);
    }
    return caches.keys().then(function (names) {
      return names
        .filter(function (n) { return n.startsWith(COURSE_CACHE_PREFIX); })
        .map(function (n) { return n.replace(COURSE_CACHE_PREFIX, ''); });
    });
  }

  // ─── Queue progress data for background sync ───
  function queueProgressSync(url, data) {
    return openDB().then(function (db) {
      return new Promise(function (resolve, reject) {
        var tx = db.transaction('pendingSync', 'readwrite');
        var store = tx.objectStore('pendingSync');
        store.add({ url: url, method: 'POST', data: data, timestamp: Date.now() });
        tx.oncomplete = function () {
          // Request background sync
          if (navigator.serviceWorker && navigator.serviceWorker.ready) {
            navigator.serviceWorker.ready.then(function (reg) {
              if (reg.sync) {
                return reg.sync.register('sync-progress');
              }
            }).catch(function () {
              // Background sync not supported — will retry on next load
            });
          }
          resolve(true);
        };
        tx.onerror = function () { reject(tx.error); };
      });
    });
  }

  function openDB() {
    return new Promise(function (resolve, reject) {
      var request = indexedDB.open('ImpactMojoOffline', 1);
      request.onupgradeneeded = function () {
        var db = request.result;
        if (!db.objectStoreNames.contains('pendingSync')) {
          db.createObjectStore('pendingSync', { keyPath: 'id', autoIncrement: true });
        }
      };
      request.onsuccess = function () { resolve(request.result); };
      request.onerror = function () { reject(request.error); };
    });
  }

  // ─── Initialize on DOM ready ───
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initStatusListeners);
  } else {
    initStatusListeners();
  }

  // ─── Export globally ───
  window.ImpactMojoOffline = {
    downloadCourse: downloadCourse,
    isCourseCached: isCourseCached,
    removeCourse: removeCourse,
    listCachedCourses: listCachedCourses,
    queueProgressSync: queueProgressSync,
    FLAGSHIP_COURSES: FLAGSHIP_COURSES
  };

})();
