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

  /**
   * Durable copy, written straight to the database by /api/form-submit.
   *
   * Netlify accepts a spam-classified submission with a 200, so response.ok
   * cannot detect that one was discarded -- six real event registrations were
   * lost exactly that way. This path is not behind the spam filter.
   */
  function submitDurable(formData) {
    var formName = formData.get('form-name');
    if (!formName) return Promise.reject(new Error('form-name missing'));

    var data = {};
    formData.forEach(function (v, k) {
      // Files are not stored here; the Netlify copy carries the upload.
      if (typeof v === 'string') data[k] = v;
    });

    return fetch('/api/form-submit', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ form_name: formName, data: data })
    }).then(function (res) {
      if (!res.ok) throw new Error('form-submit returned ' + res.status);
      return res;
    });
  }

  /**
   * Send a form down both paths and resolve if EITHER lands. Netlify carries the
   * notification email and any attachment; the endpoint carries the record that
   * cannot be silently dropped. Rejects only when both fail, which is the only
   * case where the submitter has genuinely lost their work.
   */
  function submitBoth(formData, options) {
    var opts = options || {};
    return Promise.allSettled([
      submitForm(formData, opts),
      submitDurable(formData)
    ]).then(function (results) {
      if (results.some(function (r) { return r.status === 'fulfilled'; })) return results;
      throw results[0].reason || results[1].reason || new Error('Submission failed');
    });
  }

  function submitBothFromElement(form, options) {
    var fd = new FormData(form);
    if (!fd.get('form-name')) fd.append('form-name', form.getAttribute('name') || '');
    return submitBoth(fd, options);
  }

  global.imxSubmitForm = submitForm;
  global.imxSubmitFormElement = submitFormElement;
  global.imxSubmitDurable = submitDurable;
  global.imxSubmitBoth = submitBoth;
  global.imxSubmitBothFromElement = submitBothFromElement;
  global.imxFailedSubmissions = readQueue;
})(window);
