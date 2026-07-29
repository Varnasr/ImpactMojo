/* ImpactMojo Law Guides — interactive checklist with localStorage persistence */
(function () {
  'use strict';
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('.lg-checklist').forEach(function (list) {
      var key = 'im-lawguide-' + (list.getAttribute('data-key') || location.pathname);
      var boxes = list.querySelectorAll('.lg-check input[type="checkbox"]');
      var fill = list.querySelector('.lg-checklist-fill');
      var progress = list.querySelector('.lg-checklist-progress');
      var saved = [];
      try { saved = JSON.parse(localStorage.getItem(key) || '[]'); } catch (e) { saved = []; }

      function update() {
        var done = 0;
        var state = [];
        boxes.forEach(function (b, i) {
          if (b.checked) { done++; state.push(i); }
        });
        if (fill) fill.style.width = (boxes.length ? (done / boxes.length) * 100 : 0) + '%';
        if (progress) progress.textContent = done + ' of ' + boxes.length + ' steps done';
        try { localStorage.setItem(key, JSON.stringify(state)); } catch (e) { /* private mode */ }
      }

      boxes.forEach(function (b, i) {
        if (saved.indexOf(i) !== -1) b.checked = true;
        b.addEventListener('change', update);
      });
      update();
    });
  });
})();
