/* ImpactMojo — canonical theme controller (shared).
   Single source of truth for the System/Light/Dark selector. Replaces the
   per-page inline copy that was duplicated across hundreds of pages.

   Markup contract (unchanged):
     <div class="im-theme-selector">
       <button class="im-theme-btn" data-imtheme="system">…</button>
       <button class="im-theme-btn" data-imtheme="light">…</button>
       <button class="im-theme-btn" data-imtheme="dark">…</button>
     </div>
   Canonical localStorage key: 'im-theme' (values: system | light | dark).
   Applies <html data-theme="light|dark"> + body.light-mode / body.dark-mode. */
(function () {
    function getSystemTheme() {
        return window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light';
    }
    function applyTheme(theme) {
        var resolved = theme === 'system' ? getSystemTheme() : theme;
        document.documentElement.setAttribute('data-theme', resolved);
        // Also handle legacy body classes
        document.body.classList.remove('dark-mode', 'light-mode');
        if (resolved === 'light') document.body.classList.add('light-mode');
        else document.body.classList.add('dark-mode');
    }
    function updateButtons(pref) {
        document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
            btn.classList.toggle('active', btn.getAttribute('data-imtheme') === pref);
        });
    }
    var saved = localStorage.getItem('im-theme') || 'system';
    // Apply immediately before render
    applyTheme(saved);
    document.addEventListener('DOMContentLoaded', function () {
        applyTheme(saved);
        updateButtons(saved);
        document.querySelectorAll('.im-theme-btn').forEach(function (btn) {
            btn.addEventListener('click', function () {
                var t = this.getAttribute('data-imtheme');
                localStorage.setItem('im-theme', t);
                applyTheme(t);
                updateButtons(t);
            });
        });
    });
    // Listen for system theme changes
    window.matchMedia('(prefers-color-scheme: light)').addEventListener('change', function () {
        if ((localStorage.getItem('im-theme') || 'system') === 'system') {
            applyTheme('system');
        }
    });
})();
