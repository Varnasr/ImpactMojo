/**
 * Shared Netlify Forms submitter.
 *
 * Three bugs this exists to prevent, all of which shipped:
 *
 * 1. `fetch()` resolves on 404 and 500. Every handler on the site did
 *    `.then(showSuccess).catch(showError)`, so a rejected submission showed
 *    "received" and only a dropped connection showed an error.
 *
 * 2. `new URLSearchParams(new FormData(f))` silently discards File objects, so
 *    a form could carry a file input and still upload nothing.
 *
 * 3. A submission that fails had nowhere to go, so the text was simply lost.
 *
 * Netlify's spam filter is a separate problem this cannot solve: a submission
 * Akismet classifies as spam is still accepted with a 200, so it looks
 * identical to a delivered one from the browser. Anything that must not be
 * lost needs a second, non-Forms path -- see netlify/functions/challenge-submit.
 */
(function (global) {
  'use strict';

  var QUEUE_KEY = 'impactmojo-failed-submissions';

  function hasFile(formData) {
    var found = false;
    formData.forEach(function (v) {
      if (typeof File !== 'undefined' && v instanceof File && v.size > 0) found = true;
    });
    return found;
  }

  function readQueue() {
    try { return JSON.parse(localStorage.getItem(QUEUE_KEY)) || []; }
    catch (e) { return []; }
  }

  function queueFailure(formName, formData) {
    // Files cannot be revived from localStorage, so only the text is kept --
    // enough for the submitter to recover their work, not a full replay.
    var plain = {};
    formData.forEach(function (v, k) { if (typeof v === 'string') plain[k] = v; });
    try {
      var q = readQueue();
      q.push({ form: formName, data: plain, failedAt: new Date().toISOString() });
      localStorage.setItem(QUEUE_KEY, JSON.stringify(q.slice(-20)));
    } catch (e) { /* private mode or quota -- the thrown error still surfaces */ }
  }

  function post(formData, multipart) {
    // Netlify accepts multipart only when the form declares a file input; for
    // everything else urlencoded is smaller and avoids a boundary round-trip.
    return multipart
      ? fetch('/', { method: 'POST', body: formData })
      : fetch('/', {
          method: 'POST',
          headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
          body: new URLSearchParams(formData).toString()
        });
  }

  /**
   * Submit a FormData to Netlify Forms.
   * Resolves only on a 2xx. Rejects with an Error carrying `.status` (absent
   * for a network failure) after one retry.
   */
  function submitForm(formData, options) {
    var opts = options || {};
    var formName = formData.get('form-name') || opts.formName || 'unknown';
    var multipart = opts.multipart !== undefined ? opts.multipart : hasFile(formData);

    function attempt(retriesLeft) {
      return post(formData, multipart).then(function (res) {
        if (res.ok) return res;
        // A 4xx will not change on retry; only a 5xx is worth a second attempt.
        if (res.status >= 500 && retriesLeft > 0) {
          return new Promise(function (r) { setTimeout(r, 1200); }).then(function () {
            return attempt(retriesLeft - 1);
          });
        }
        var err = new Error('Submission rejected (HTTP ' + res.status + ')');
        err.status = res.status;
        throw err;
      }, function (networkErr) {
        if (retriesLeft > 0) {
          return new Promise(function (r) { setTimeout(r, 1200); }).then(function () {
            return attempt(retriesLeft - 1);
          });
        }
        throw networkErr;
      });
    }

    return attempt(1).catch(function (err) {
      queueFailure(formName, formData);
      throw err;
    });
  }

  function submitFormElement(form, options) {
    var fd = new FormData(form);
    if (!fd.get('form-name')) fd.append('form-name', form.getAttribute('name') || '');
    return submitForm(fd, options);
  }

  global.imxSubmitForm = submitForm;
  global.imxSubmitFormElement = submitFormElement;
  global.imxFailedSubmissions = readQueue;
})(window);
