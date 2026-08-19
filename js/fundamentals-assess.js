/* =============================================================================
   ImpactMojo — Fundamentals: the questionnaire that derives a wheel position
   -----------------------------------------------------------------------------
   Writes into the SAME localStorage key the manual marks already used
   ("im-fundamentals-marks", shape {axisId: ring}), so the wheel paints a derived
   position exactly as it painted a marked one, and switching between the two
   loses nothing.

   Nothing here transmits. There is no fetch in this file and there is not meant
   to be one: the answers include caste, sexual orientation, religion and
   disability, and the only defensible place for them is the person's own
   browser. scripts/check-fundamentals-privacy.py enforces that.
   ============================================================================= */
(function () {
  "use strict";

  var Q = window.FUNDAMENTALS_ASSESS;
  var D = window.FUNDAMENTALS;
  if (!Q || !D) return;

  var MARK_KEY = "im-fundamentals-marks";
  var ANSWER_KEY = "im-fundamentals-answers";
  var SKIP = Q.SKIP;

  var state = { answers: {}, open: false };

  function esc(s) {
    return String(s).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }

  function axisById(id) {
    return D.axes.filter(function (a) { return a.id === id; })[0];
  }

  /* --------------------------------------------------------------- storage */
  function loadAnswers() {
    try { state.answers = JSON.parse(localStorage.getItem(ANSWER_KEY) || "{}") || {}; }
    catch (e) { state.answers = {}; }
  }
  function saveAnswers() {
    try { localStorage.setItem(ANSWER_KEY, JSON.stringify(state.answers)); } catch (e) {}
  }

  /* Derived marks replace the manual ones for the axes answered, and leave any
     other axis the person marked by hand untouched. */
  function writeMarks() {
    var marks = {};
    try { marks = JSON.parse(localStorage.getItem(MARK_KEY) || "{}") || {}; } catch (e) { marks = {}; }
    Q.questions.forEach(function (q) {
      var a = state.answers[q.axis];
      if (a === undefined) return;
      if (a === SKIP) delete marks[q.axis];
      else marks[q.axis] = a;
    });
    try { localStorage.setItem(MARK_KEY, JSON.stringify(marks)); } catch (e) {}
    if (typeof window.imxRefreshMarks === "function") window.imxRefreshMarks();
  }

  function answeredCount() {
    return Q.questions.filter(function (q) {
      return state.answers[q.axis] !== undefined && state.answers[q.axis] !== SKIP;
    }).length;
  }

  /* ------------------------------------------------------------ the form */
  function renderForm() {
    var host = document.getElementById("assessBody");
    if (!host) return;

    var h = [];
    h.push('<p class="assess-lede">Twelve questions, each about a category rather than a feeling. ' +
           'Your answers stay in this browser and are sent nowhere. Skip anything you would rather not answer &mdash; ' +
           'a skipped axis simply goes unmarked.</p>');

    Q.questions.forEach(function (q, i) {
      var axis = axisById(q.axis);
      var chosen = state.answers[q.axis];
      h.push('<fieldset class="assess-q">');
      h.push('<legend><span class="aq-n">' + (i + 1) + '</span> ' + esc(q.q) + '</legend>');
      if (q.help) h.push('<p class="aq-help">' + esc(q.help) + '</p>');
      q.options.forEach(function (o, j) {
        var id = "aq-" + q.axis + "-" + j;
        h.push('<label class="aq-opt" for="' + id + '">' +
          '<input type="radio" id="' + id + '" name="aq-' + esc(q.axis) + '" value="' + esc(o.band) + '"' +
          (chosen === o.band ? " checked" : "") + '>' +
          '<span>' + esc(o.label) + '</span></label>');
      });
      var sid = "aq-" + q.axis + "-skip";
      h.push('<label class="aq-opt aq-skip" for="' + sid + '">' +
        '<input type="radio" id="' + sid + '" name="aq-' + esc(q.axis) + '" value="' + SKIP + '"' +
        (chosen === SKIP ? " checked" : "") + '>' +
        '<span>Prefer not to say</span></label>');
      h.push('<p class="aq-axis">Maps to the <b>' + esc(axis ? axis.name : q.axis) + '</b> axis</p>');
      h.push("</fieldset>");
    });

    h.push('<div class="assess-actions">' +
      '<button type="button" class="btn-ghost" id="assessShow">Show me on the wheel</button>' +
      '<button type="button" class="btn-ghost" id="assessReset">Clear my answers</button>' +
      '</div>');

    h.push('<div id="assessResult" hidden></div>');

    host.innerHTML = h.join("");

    host.querySelectorAll('input[type="radio"]').forEach(function (r) {
      r.addEventListener("change", function () {
        var axis = r.getAttribute("name").replace(/^aq-/, "");
        state.answers[axis] = r.value;
        saveAnswers();
      });
    });
    document.getElementById("assessShow").addEventListener("click", reveal);
    document.getElementById("assessReset").addEventListener("click", reset);
  }

  /* --------------------------------------------------------------- reveal */
  /* The reveal shows the band AND the definition that produced it, because the
     point is that a person can see the reasoning and disagree with it. A result
     that only announced a position would be a verdict, which this is not. */
  function reveal() {
    writeMarks();
    var box = document.getElementById("assessResult");
    if (!box) return;

    var rows = [];
    Q.questions.forEach(function (q) {
      var a = state.answers[q.axis];
      if (a === undefined || a === SKIP) return;
      var axis = axisById(q.axis);
      if (!axis || !axis.rings[a]) return;
      rows.push('<li class="ar r-' + esc(a) + '">' +
        '<span class="ar-axis">' + esc(axis.name) + '</span>' +
        '<span class="ar-band">' + esc(D.RING_LABEL[a]) + '</span>' +
        '<span class="ar-def">' + esc(axis.rings[a].groups) + '</span>' +
        '</li>');
    });

    var n = answeredCount();
    /* "Skipped" means the person chose "prefer not to say". Everything else is
       simply unanswered, and conflating the two would put words in their mouth. */
    var skipped = Q.questions.filter(function (q) { return state.answers[q.axis] === SKIP; }).length;
    var untouched = Q.questions.length - n - skipped;

    if (!rows.length) {
      box.innerHTML = '<div class="assess-result"><h4>Nothing to show yet</h4>' +
        '<p>Answer at least one question, or mark a band on the wheel directly.</p></div>';
      box.hidden = false;
      return;
    }

    box.innerHTML =
      '<div class="assess-result">' +
        '<h4>Where the wheel places you &mdash; ' + n + ' of ' + Q.questions.length + ' axes</h4>' +
        '<p>This is the wheel&rsquo;s own definition applied to what you said, and nothing more. ' +
        'It is not a score, the axes do not add up, and the wheel has no opinion about which of them matters most. ' +
        (skipped ? 'You chose not to answer ' + skipped + '. ' : "") +
        (untouched ? (untouched === 1 ? 'One question is still unanswered. ' : untouched + ' are still unanswered. ') : "") +
        (skipped || untouched ? 'Those axes stay unmarked. ' : "") +
        'Everything here is in your browser and was sent nowhere.</p>' +
        '<ul class="assess-rows">' + rows.join("") + '</ul>' +
        '<p class="assess-foot">Disagree with a placement? The definition is printed beside it. ' +
        'You can change an answer above, or click any band on the wheel to override it by hand.</p>' +
      '</div>';
    box.hidden = false;
    box.setAttribute("tabindex", "-1");
    box.focus({ preventScroll: true });
    box.scrollIntoView({ behavior: "smooth", block: "nearest" });
  }

  function reset() {
    state.answers = {};
    saveAnswers();
    var marks = {};
    try { marks = JSON.parse(localStorage.getItem(MARK_KEY) || "{}") || {}; } catch (e) { marks = {}; }
    Q.questions.forEach(function (q) { delete marks[q.axis]; });
    try { localStorage.setItem(MARK_KEY, JSON.stringify(marks)); } catch (e) {}
    if (typeof window.imxRefreshMarks === "function") window.imxRefreshMarks();
    renderForm();
    var box = document.getElementById("assessResult");
    if (box) { box.hidden = true; box.innerHTML = ""; }
  }

  /* ----------------------------------------------------------------- init */
  function init() {
    var toggle = document.getElementById("assessToggle");
    var panel = document.getElementById("assessPanel");
    if (!toggle || !panel) return;

    loadAnswers();
    renderForm();

    toggle.addEventListener("click", function () {
      state.open = !state.open;
      panel.hidden = !state.open;
      toggle.setAttribute("aria-expanded", state.open ? "true" : "false");
      toggle.textContent = state.open ? "Hide the questions" : "Answer twelve questions instead";
      if (state.open) panel.scrollIntoView({ behavior: "smooth", block: "start" });
    });
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", init);
  } else {
    init();
  }
})();
