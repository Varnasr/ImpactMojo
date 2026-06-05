/* ImpactMojo — canonical theme controller (shared, superset).
   Single source of truth for the System / Light / Dark selector, replacing the
   ~18 inline variants that were duplicated across the site.

   Supports every markup/convention the inline copies used, so it is a safe
   drop-in for all of them:
     • Buttons:  .im-theme-btn[data-imtheme]  AND  .theme-btn[data-theme]
     • CSS hooks (applies ALL — the design system defines them consistently):
         <html data-theme="light|dark">, <html class="dark">,
         <body class="light-mode|dark-mode">
     • Storage: canonical 'im-theme' (values: system|light|dark) with one-shot
       migration from legacy keys, and mirror-writes for back-compat with any
       page still reading a legacy key during the migration.  */
(function () {
    var CANON = 'im-theme';
    var LEGACY = ['impactmojo-theme', 'theme', 'imx_theme'];

    function getSystemTheme() {
        return (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) ? 'dark' : 'light';
    }
    function readPref() {
        try {
            var t = localStorage.getItem(CANON);
            if (t) return t;
            for (var i = 0; i < LEGACY.length; i++) {
                var v = localStorage.getItem(LEGACY[i]);
                if (v) { try { localStorage.setItem(CANON, v); } catch (e) {} return v; }
            }
        } catch (e) {}
        return 'system';
    }
    function writePref(pref) {
        try {
            localStorage.setItem(CANON, pref);
            // mirror to legacy keys so not-yet-migrated pages stay in sync
            for (var i = 0; i < LEGACY.length; i++) localStorage.setItem(LEGACY[i], pref);
        } catch (e) {}
    }
    function applyTheme(pref) {
        var resolved = pref === 'system' ? getSystemTheme() : pref;
        var dark = resolved === 'dark';
        var root = document.documentElement;
        root.setAttribute('data-theme', resolved);
        root.classList.toggle('dark', dark);
        if (document.body) {
            document.body.classList.remove('dark-mode', 'light-mode');
            document.body.classList.add(dark ? 'dark-mode' : 'light-mode');
        }
    }
    function updateButtons(pref) {
        document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-imtheme') === pref);
        });
        document.querySelectorAll('.theme-btn').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-theme') === pref);
        });
    }
    function pick(btn) {
        return btn.getAttribute('data-imtheme') || btn.getAttribute('data-theme');
    }
    function wire() {
        applyTheme(saved);
        updateButtons(saved);
        document.querySelectorAll('.im-theme-btn, .theme-btn').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var t = pick(this);
                if (!t) return;
                writePref(t);
                applyTheme(t);
                updateButtons(t);
            });
        });
    }

    var saved = readPref();
    applyTheme(saved); // apply ASAP (before paint where possible)
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', wire);
    } else {
        wire();
    }
    window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', function () {
        if (readPref() === 'system') applyTheme('system');
    });
})();
