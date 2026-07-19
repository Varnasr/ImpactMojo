/* Verified testimonials — renders quotes from /data/testimonials.json into any
 * <div data-testimonials="premium"> container (the attribute value filters by
 * the entry's `pages` list). While the data file has no entries, containers
 * stay empty and hidden — no fake social proof, ever.
 */
(function () {
    'use strict';

    var mounts = document.querySelectorAll('[data-testimonials]');
    if (!mounts.length) return;

    fetch('/data/testimonials.json')
        .then(function (r) { return r.ok ? r.json() : null; })
        .then(function (data) {
            var list = data && Array.isArray(data.testimonials) ? data.testimonials : [];
            if (!list.length) return;

            mounts.forEach(function (mount) {
                var page = mount.getAttribute('data-testimonials');
                var matches = list.filter(function (t) {
                    return t.quote && t.name && (!t.pages || t.pages.indexOf(page) !== -1);
                });
                if (!matches.length) return;

                var esc = function (s) {
                    return String(s).replace(/[&<>"]/g, function (c) {
                        return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c];
                    });
                };

                var cards = matches.slice(0, 6).map(function (t) {
                    var course = t.course
                        ? (t.courseUrl
                            ? ' · <a href="' + esc(t.courseUrl) + '" style="color:inherit">' + esc(t.course) + '</a>'
                            : ' · ' + esc(t.course))
                        : '';
                    return '<figure class="imx-testimonial" ' + (t.lang && t.lang !== 'en' ? 'lang="' + esc(t.lang) + '"' : '') + '>' +
                        '<blockquote>&ldquo;' + esc(t.quote) + '&rdquo;</blockquote>' +
                        '<figcaption>&mdash; ' + esc(t.name) + (t.role ? ', ' + esc(t.role) : '') + course + '</figcaption>' +
                        '</figure>';
                }).join('');

                mount.innerHTML =
                    '<style>' +
                    '.imx-testimonial-wrap{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:16px;margin:20px 0}' +
                    '.imx-testimonial{margin:0;padding:18px 20px;border:1px solid rgba(128,128,128,0.3);border-radius:12px}' +
                    '.imx-testimonial blockquote{margin:0 0 10px;font-style:italic;line-height:1.55}' +
                    '.imx-testimonial figcaption{font-size:0.85rem;opacity:0.8}' +
                    '</style>' +
                    '<h2 style="font-size:1.25rem;margin:0 0 4px">What learners say</h2>' +
                    '<p style="font-size:0.85rem;opacity:0.75;margin:0 0 12px">Real quotes, shared with permission.</p>' +
                    '<div class="imx-testimonial-wrap">' + cards + '</div>';
                mount.style.display = '';
            });
        })
        .catch(function () { /* leave containers empty */ });
})();
