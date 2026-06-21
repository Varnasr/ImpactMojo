// ImpactMojo — Web Push opt-in
// Subscribes the browser to push notifications and stores the subscription via
// the send-push Edge Function. Requires js/auth.js (window.supabaseClient) and
// the service worker registered by js/pwa.js.
//
// Public API (window.ImpactMojoPush):
//   isSupported()            -> boolean
//   getStatus()              -> Promise<'unsupported'|'denied'|'subscribed'|'default'>
//   enable()                 -> Promise<boolean>   request permission + subscribe
//   disable()                -> Promise<boolean>   unsubscribe + remove server-side
(function () {
  'use strict';

  // VAPID public key (safe to expose — it is the application server's public key).
  var VAPID_PUBLIC_KEY = 'BKRYDPRGbwXrK9BPzq--m64S4nci9kWNUlV8zDnheiml1pU7AGm9LBDQRqCsYqmBlkkcCsnQLVCCERsYNVu-bkU';

  var FN_BASE = (window.ImpactMojoConfig && window.ImpactMojoConfig.SUPABASE_URL
    ? window.ImpactMojoConfig.SUPABASE_URL
    : 'https://ddyszmfffyedolkcugld.supabase.co') + '/functions/v1/send-push';

  function isSupported() {
    return 'serviceWorker' in navigator && 'PushManager' in window && 'Notification' in window;
  }

  function urlBase64ToUint8Array(base64String) {
    var padding = '='.repeat((4 - (base64String.length % 4)) % 4);
    var base64 = (base64String + padding).replace(/-/g, '+').replace(/_/g, '/');
    var raw = atob(base64);
    var output = new Uint8Array(raw.length);
    for (var i = 0; i < raw.length; i++) output[i] = raw.charCodeAt(i);
    return output;
  }

  async function getToken() {
    var sb = window.supabaseClient;
    if (!sb) return null;
    try {
      var res = await sb.auth.getSession();
      return res && res.data && res.data.session ? res.data.session.access_token : null;
    } catch (e) { return null; }
  }

  async function callFn(action, body) {
    var token = await getToken();
    if (!token) throw new Error('Not signed in');
    var resp = await fetch(FN_BASE + '/' + action, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token },
      body: JSON.stringify(body || {})
    });
    if (!resp.ok) throw new Error('send-push ' + action + ' failed: ' + resp.status);
    return resp.json();
  }

  async function getStatus() {
    if (!isSupported()) return 'unsupported';
    if (Notification.permission === 'denied') return 'denied';
    try {
      var reg = await navigator.serviceWorker.ready;
      var sub = await reg.pushManager.getSubscription();
      if (sub) return 'subscribed';
    } catch (e) { /* fall through */ }
    return Notification.permission === 'granted' ? 'default' : 'default';
  }

  async function enable() {
    if (!isSupported()) return false;
    var permission = await Notification.requestPermission();
    if (permission !== 'granted') return false;

    var reg = await navigator.serviceWorker.ready;
    var sub = await reg.pushManager.getSubscription();
    if (!sub) {
      sub = await reg.pushManager.subscribe({
        userVisibleOnly: true,
        applicationServerKey: urlBase64ToUint8Array(VAPID_PUBLIC_KEY)
      });
    }
    await callFn('save', {
      subscription: sub.toJSON(),
      user_agent: navigator.userAgent
    });
    return true;
  }

  async function disable() {
    if (!isSupported()) return false;
    try {
      var reg = await navigator.serviceWorker.ready;
      var sub = await reg.pushManager.getSubscription();
      if (sub) {
        await callFn('delete', { endpoint: sub.endpoint }).catch(function () {});
        await sub.unsubscribe();
      }
    } catch (e) { /* best effort */ }
    return true;
  }

  window.ImpactMojoPush = {
    isSupported: isSupported,
    getStatus: getStatus,
    enable: enable,
    disable: disable
  };
})();
