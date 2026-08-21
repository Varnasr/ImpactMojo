/* Studio submissions — give a Studio export an identity, so it can be marked.
 *
 * The Studios already export. What they export is the working state and nothing
 * else: logframe-builder writes JSON.stringify(state), most others write plain
 * text. An instructor who collects thirty of those files has thirty documents
 * and no way to say which student produced which, when, or from which Studio.
 * That is the whole reason a gradebook CSV did not exist.
 *
 * This wraps any Studio's existing export in a small envelope carrying the
 * student's name, the Studio, the time, and a short digest of the payload. The
 * payload is untouched, so a submission file still opens as the thing the
 * student built and can still be re-imported by the Studio that made it.
 *
 * Deliberately not an accounts feature. There is no login, no roster and no
 * server: the student types their own name and the instructor reads the files
 * they were sent. The digest detects accidental corruption in transit, not
 * dishonesty -- a student who wants to edit their own submission can, and any
 * scheme that claimed otherwise on a static site would be lying.
 */
(function () {
  'use strict';

  var VERSION = 1;
  var KEY = 'im-studio-student';   // remembered per browser, per-viewer only

  /* A short, stable digest. Not cryptographic: it exists so a file truncated by
   * a mail client or mangled by a copy-paste is caught before it reaches a
   * gradebook, where a silently-wrong row is worse than a missing one. */
  function digest(str) {
    var h1 = 0x811c9dc5, h2 = 0x01000193;
    for (var i = 0; i < str.length; i++) {
      var c = str.charCodeAt(i);
      h1 = ((h1 ^ c) * 0x01000193) >>> 0;
      h2 = ((h2 + c) * 31 + (h2 << 3)) >>> 0;
    }
    return (h1.toString(36) + h2.toString(36)).slice(0, 12);
  }

  function remembered() {
    try { return JSON.parse(localStorage.getItem(KEY) || '{}'); } catch (e) { return {}; }
  }
  function remember(who) {
    try { localStorage.setItem(KEY, JSON.stringify(who)); } catch (e) { /* private window */ }
  }

  /* Build the envelope. `payload` may be a string or any JSON-serialisable value;
   * it is stored as given so the Studio can re-import its own export unchanged. */
  function build(opts) {
    var who = opts.student || remembered();
    var payloadText = typeof opts.payload === 'string'
      ? opts.payload : JSON.stringify(opts.payload);
    return {
      impactmojo_submission: VERSION,
      studio: opts.studio,                       // machine id, e.g. "logframe-builder"
      studio_title: opts.studioTitle || opts.studio,
      student_name: (who.name || '').trim(),
      student_id: (who.id || '').trim(),
      course: (who.course || '').trim(),
      submitted_at: new Date().toISOString(),
      payload_type: typeof opts.payload === 'string' ? 'text' : 'json',
      payload: opts.payload,
      digest: digest(payloadText)
    };
  }

  /* Verify a parsed submission. Returns {ok, reason}. Used by the collector. */
  function verify(sub) {
    if (!sub || sub.impactmojo_submission !== VERSION) {
      return { ok: false, reason: 'not an ImpactMojo submission file' };
    }
    if (!sub.studio) return { ok: false, reason: 'no studio recorded' };
    var text = sub.payload_type === 'text' ? sub.payload : JSON.stringify(sub.payload);
    if (sub.digest && digest(text) !== sub.digest) {
      return { ok: false, reason: 'payload does not match its digest — the file may be truncated' };
    }
    return { ok: true };
  }

  function downloadBlob(name, text, mime) {
    var blob = new Blob([text], { type: mime || 'application/json' });
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url; a.download = name;
    document.body.appendChild(a); a.click();
    document.body.removeChild(a);
    setTimeout(function () { URL.revokeObjectURL(url); }, 2000);
  }

  function slugify(s) {
    return String(s || 'submission').toLowerCase()
      .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '') || 'submission';
  }

  /* Ask for the student's details in one small dialog.
   *
   * An earlier version used three sequential window.prompt() calls. That works
   * but is poor: three native modals in a row, no way to correct the first after
   * seeing the third, and no validation until the end. This injects a single
   * form instead, styled minimally so it sits acceptably in any Studio without
   * needing that Studio's stylesheet. */
  function ask(prefill) {
    return new Promise(function (resolve) {
      var back = document.createElement('div');
      back.setAttribute('role', 'dialog');
      back.setAttribute('aria-modal', 'true');
      back.setAttribute('aria-label', 'Submit for marking');
      back.style.cssText = 'position:fixed;inset:0;z-index:99999;background:rgba(0,0,0,.45);' +
        'display:flex;align-items:center;justify-content:center;padding:1rem';
      var dark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
      var bg = dark ? '#161b22' : '#fff', fg = dark ? '#e6edf3' : '#111', bd = dark ? '#2b323b' : '#cbd2da';
      back.innerHTML =
        '<form style="background:' + bg + ';color:' + fg + ';border-radius:12px;padding:1.25rem;' +
        'max-width:26rem;width:100%;font:inherit;box-shadow:0 10px 40px rgba(0,0,0,.3)">' +
        '<h2 style="margin:0 0 .3rem;font-size:1.1rem">Submit for marking</h2>' +
        '<p style="margin:0 0 1rem;font-size:.9rem;opacity:.75;line-height:1.5">' +
        'This downloads a file with your name on it, which you send to your instructor. ' +
        'Your work stays on this device otherwise.</p>' +
        '<label style="display:block;font-size:.88rem;font-weight:600;margin-bottom:.25rem">Your name</label>' +
        '<input name="nm" required style="width:100%;padding:.55rem;border:1px solid ' + bd + ';border-radius:8px;' +
        'background:transparent;color:inherit;font:inherit;margin-bottom:.75rem">' +
        '<label style="display:block;font-size:.88rem;font-weight:600;margin-bottom:.25rem">Student or roll number <span style="font-weight:400;opacity:.6">(optional)</span></label>' +
        '<input name="sid" style="width:100%;padding:.55rem;border:1px solid ' + bd + ';border-radius:8px;' +
        'background:transparent;color:inherit;font:inherit;margin-bottom:.75rem">' +
        '<label style="display:block;font-size:.88rem;font-weight:600;margin-bottom:.25rem">Course <span style="font-weight:400;opacity:.6">(optional)</span></label>' +
        '<input name="crs" style="width:100%;padding:.55rem;border:1px solid ' + bd + ';border-radius:8px;' +
        'background:transparent;color:inherit;font:inherit;margin-bottom:1rem">' +
        '<div style="display:flex;gap:.5rem;justify-content:flex-end">' +
        '<button type="button" data-x="cancel" style="padding:.55rem 1rem;border-radius:8px;border:1px solid ' + bd + ';' +
        'background:transparent;color:inherit;font:inherit;cursor:pointer">Cancel</button>' +
        '<button type="submit" style="padding:.55rem 1.1rem;border-radius:8px;border:0;background:#2563EB;' +
        'color:#fff;font:inherit;font-weight:600;cursor:pointer">Download submission</button>' +
        '</div></form>';
      document.body.appendChild(back);
      var form = back.querySelector('form');
      form.nm.value = prefill.name || '';
      form.sid.value = prefill.id || '';
      form.crs.value = prefill.course || '';
      setTimeout(function () { form.nm.focus(); }, 0);

      function close(val) {
        if (back.parentNode) back.parentNode.removeChild(back);
        document.removeEventListener('keydown', onKey, true);
        resolve(val);
      }
      function onKey(e) { if (e.key === 'Escape') { e.preventDefault(); close(null); } }
      document.addEventListener('keydown', onKey, true);
      back.querySelector('[data-x=cancel]').addEventListener('click', function () { close(null); });
      back.addEventListener('mousedown', function (e) { if (e.target === back) close(null); });
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        var n = form.nm.value.trim();
        if (!n) { form.nm.focus(); return; }
        close({ name: n, id: form.sid.value.trim(), course: form.crs.value.trim() });
      });
    });
  }

  /* Collect details, build the envelope, download it. Resolves with the
   * submission object, or null if the student cancelled. */
  function submit(opts) {
    return ask(remembered()).then(function (who) {
      if (!who) return null;
      remember(who);
      var sub = build({ studio: opts.studio, studioTitle: opts.studioTitle,
                        payload: opts.payload, student: who });
      var fname = slugify(who.name) + '--' + slugify(opts.studio) + '.imsub.json';
      downloadBlob(fname, JSON.stringify(sub, null, 2), 'application/json');
      return sub;
    });
  }

  /* Add a "Submit for marking" control next to a Studio's existing export
   * buttons. getPayload() is called at click time so it always reflects current
   * state rather than state at wiring time. */
  function addButton(opts) {
    var host = typeof opts.after === 'string'
      ? document.querySelector(opts.after) : opts.after;
    if (!host || !host.parentNode) return null;
    var b = document.createElement('button');
    b.type = 'button';
    b.className = opts.className || 'btn btn-outline btn-sm';
    b.textContent = opts.label || 'Submit for marking';
    b.title = 'Download a file your instructor can mark, with your name on it';
    b.addEventListener('click', function () {
      submit({ studio: opts.studio, studioTitle: opts.studioTitle,
               payload: opts.getPayload() });
    });
    host.parentNode.insertBefore(b, host.nextSibling);
    return b;
  }

  window.IMStudioSubmit = {
    build: build, verify: verify, submit: submit,
    addButton: addButton, digest: digest, VERSION: VERSION
  };
})();
