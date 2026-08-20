#!/usr/bin/env python3
"""Reusable builder for ImpactMojo Deep Dive curated reading lists.

Emits the full DeepDives/<slug>.html in the house style (matches
the-stunting-puzzle.html / the-learning-crisis.html): brand topbar, hero,
curator card, editor's note, numbered sections of annotated reading items,
related-content block, suggested citation, contribute CTA and footer.
Per-dive scripts supply only structured content.
"""
import os, html

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOPBAR = '''<header class="im-topbar" role="banner">
  <div class="im-topbar-left"><a class="im-topbar-home" href="/" aria-label="ImpactMojo home"><img src="/assets/images/ImpactMojo%20Logo.png" alt="ImpactMojo"><span>ImpactMojo</span></a></div>
  <div class="im-topbar-right">
    <a href="/catalog.html" class="im-browse-btn" title="Browse all content"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="7" height="7"/><rect x="14" y="3" width="7" height="7"/><rect x="14" y="14" width="7" height="7"/><rect x="3" y="14" width="7" height="7"/></svg>Browse</a>

    <a class="im-premium-btn" href="/premium.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/></svg>Premium</a>
    <div class="im-theme-selector" role="group" aria-label="Theme">
      <button class="im-theme-btn" data-imtheme="system" aria-label="System theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="2" y="3" width="20" height="14" rx="2"/><line x1="8" y1="21" x2="16" y2="21"/><line x1="12" y1="17" x2="12" y2="21"/></svg></button>
      <button class="im-theme-btn" data-imtheme="light" aria-label="Light theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="5"/><line x1="12" y1="1" x2="12" y2="3"/><line x1="12" y1="21" x2="12" y2="23"/><line x1="4.22" y1="4.22" x2="5.64" y2="5.64"/><line x1="18.36" y1="18.36" x2="19.78" y2="19.78"/><line x1="1" y1="12" x2="3" y2="12"/><line x1="21" y1="12" x2="23" y2="12"/><line x1="4.22" y1="19.78" x2="5.64" y2="18.36"/><line x1="18.36" y1="5.64" x2="19.78" y2="4.22"/></svg></button>
      <button class="im-theme-btn" data-imtheme="dark" aria-label="Dark theme"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"/></svg></button>
    </div>
  </div>
</header>'''

FOOTER = '''<footer class="im-footer" role="contentinfo">
  <div class="im-footer-content">
    <p class="im-footer-made">Made with <svg aria-hidden="true"><use href="#si_Heart"/></svg> by <a href="https://www.pinpointventures.in" rel="noopener noreferrer" target="_blank">PinPoint Ventures</a></p>
    <div class="im-footer-grid">
      <div class="im-footer-section"><h4>About ImpactMojo</h4><ul>
        <li><a href="/about.html">About Us</a></li>
        <li><a href="/contact.html">Contact</a></li>
        <li><a href="https://github.com/ImpactMojo/ImpactMojo" rel="noopener noreferrer" target="_blank">GitHub</a></li>
        <li><a href="/transparency.html">Transparency</a></li>
      </ul></div>
      <div class="im-footer-section"><h4>Legal</h4><ul>
        <li><a href="/privacy-policy.html">Privacy Policy</a></li>
        <li><a href="/terms-of-service.html">Terms of Service</a></li>
        <li><a href="/disclaimer.html">Disclaimer</a></li>
        <li><a href="/data-protection.html">Data Protection</a></li>
      </ul></div>
      <div class="im-footer-section"><h4>Quick Links</h4><ul>
        <li><a href="/catalog.html">All Courses</a></li>
        <li><a href="/DeepDives/">Deep Dives</a></li>
        <li><a href="/BookSummaries/">Book Companions</a></li>
        <li><a href="/premium.html">Premium</a></li>
      </ul></div>
      <div class="im-footer-section"><h4>Resources</h4><ul>
        <li><a href="/handouts.html">Handouts</a></li>
        <li><a href="/blog.html">Blog</a></li>
        <li><a href="/faq.html">FAQ</a></li>
        <li><a href="/sitemap.html">Sitemap</a></li>
      </ul></div>
    </div>
    <div class="im-footer-bottom">
      <p>&copy; 2026 ImpactMojo. All content for educational purposes only.</p>
      <p>Released under <strong>MIT License</strong> | Supported by <a href="https://www.pinpointventures.in" rel="noopener noreferrer" target="_blank">PinPoint Ventures</a></p>
    </div>
  </div>
</footer>'''

SCRIPTS = '''<script src="/DeepDives/dd-shared.js"></script>


<!-- Supabase Auth (deferred, non-blocking) -->
<script defer src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2.49.1"></script>
<script defer src="/js/state-manager.js"></script>
<script defer src="/js/config.js"></script>
<script defer src="/js/auth.js"></script>
<script defer src="/js/translate.js"></script>
<script src="/js/translate-sarvam.js" defer></script>'''

# data-t -> (label, sprite id)
TYPE_ICON = {
    'book': ('Book', 'si_Book'),
    'report': ('Report', 'si_Book'),
    'paper': ('Paper', 'si_Article'),
    'article': ('Article', 'si_Article'),
    'web': ('Web', 'si_Globe_detailed'),
    'dataset': ('Dataset', 'si_Database'),
    'podcast': ('Podcast', 'si_Album'),
    'film': ('Film', 'si_Direction_alt'),
}


def _item(it):
    t = it['type']
    label, icon = TYPE_ICON[t]
    label = it.get('label', label)
    cite = it['cite']
    url = it['url']
    annot = it['annot']
    return (
        '    <article class="dd-item">\n'
        '      <div class="dd-item-head"><span class="dd-type" data-t="%s"><svg aria-hidden="true"><use href="#%s"/></svg>%s</span>'
        '<span class="dd-cite"><a href="%s" target="_blank" rel="noopener">%s</a></span></div>\n'
        '      <p class="dd-annot">%s</p>\n'
        '    </article>' % (t, icon, label, url, cite, annot)
    )


def build(slug, title, topic, tagline, chips, curator, curator_role, curator_bio,
          curator_badge, curator_initials, note_paras, sections, related, citation,
          meta_desc, reading_count):
    head = ('<!DOCTYPE html>\n<html lang="en">\n<head>\n<meta charset="UTF-8">\n'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">\n'
            '<title>' + title + ' — ImpactMojo Deep Dive</title>\n'
            '<meta name="description" content="' + html.escape(meta_desc, quote=True) + '">\n'
            '<link rel="canonical" href="https://www.impactmojo.in/DeepDives/' + slug + '.html">\n'
            '<meta name="robots" content="index, follow">\n'
            '<meta property="og:type" content="article">\n'
            '<meta property="og:title" content="' + title + ' — ImpactMojo Deep Dive">\n'
            '<meta property="og:description" content="' + html.escape(meta_desc, quote=True) + '">\n'
            '<meta property="og:url" content="https://impactmojo.in/DeepDives/' + slug + '.html">\n'
            '<meta property="og:image" content="https://impactmojo.in/assets/images/ImpactMojo%20Logo.png">\n'
            '<meta property="og:site_name" content="ImpactMojo">\n'
            '<meta name="twitter:card" content="summary_large_image">\n'
            '<link rel="icon" href="/assets/images/ImpactMojo%20Logo.png" type="image/png">\n'
            '<link rel="preconnect" href="https://fonts.googleapis.com">\n'
            '<link href="https://fonts.googleapis.com/css2?family=Amaranth:wght@400;700&family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">\n'
            '<script async src="https://www.googletagmanager.com/gtag/js?id=G-JRCMEB9TBW"></script>\n'
            "<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments);}gtag('js',new Date());gtag('config','G-JRCMEB9TBW');</script>\n"
            '<link rel="stylesheet" href="/DeepDives/dd-shared.css">\n'
            '</head>\n<body>\n<a href="#main-content" class="im-skip-link">Skip to content</a>\n\n')

    chip_html = ''.join('    <span class="dd-chip">%s</span>\n' % c for c in chips)
    chip_html += '    <span class="dd-chip dd-chip-teal">%d readings</span>' % reading_count

    notes = ''.join('    <p>%s</p>\n' % p for p in note_paras).rstrip('\n')

    secs = []
    for i, s in enumerate(sections, 1):
        items = '\n\n'.join(_item(it) for it in s['items'])
        secs.append(
            '  <section class="dd-section">\n'
            '    <div class="dd-section-num">Section %02d</div>\n'
            '    <h2 class="dd-section-title">%s</h2>\n'
            '    <p class="dd-section-intro">%s</p>\n\n%s\n  </section>' % (i, s['title'], s['intro'], items))
    sections_html = '\n\n'.join(secs)

    rel = ''.join(
        '      <li><span class="dd-related-icon"><svg aria-hidden="true"><use href="#%s"/></svg></span>'
        '<a href="%s">%s</a></li>\n' % (r.get('icon', 'si_Library_books'), r['url'], r['label'])
        for r in related).rstrip('\n')

    body = (
        '<main id="main-content" class="dd-wrap">\n'
        '  <a class="dd-back" href="/DeepDives/">← All Deep Dives</a>\n\n'
        '  <div class="dd-eyebrow">Deep Dive · ' + topic + '</div>\n'
        '  <h1 class="dd-title">' + title + '</h1>\n'
        '  <p class="dd-tagline">' + tagline + '</p>\n'
        '  <div class="dd-chips">\n' + chip_html + '\n  </div>\n\n'
        '  <div class="dd-curator">\n'
        '    <div class="dd-curator-avatar" style="background:linear-gradient(135deg,#0EA5E9 0%,#6366F1 100%);">' + curator_initials + '</div>\n'
        '    <div class="dd-curator-body">\n'
        '      <div class="dd-curator-name">' + curator + '</div>\n'
        '      <div class="dd-curator-role">' + curator_role + '</div>\n'
        '      <div class="dd-curator-bio">' + curator_bio + '</div>\n'
        '      <span class="dd-curator-badge">' + curator_badge + '</span>\n'
        '    </div>\n  </div>\n\n'
        '  <div class="dd-note">\n    <div class="dd-note-label">Editor\'s Note</div>\n' + notes + '\n  </div>\n\n'
        + sections_html + '\n\n'
        '  <div class="dd-related">\n    <div class="dd-related-label">Continue on ImpactMojo</div>\n    <ul>\n' + rel + '\n    </ul>\n  </div>\n\n'
        '  <div class="dd-cite-block">\n    <div class="dd-cite-label">Suggested citation</div>\n'
        '    <p class="dd-cite-text">' + citation + '</p>\n  </div>\n\n'
        '  <div class="dd-cta">\n    <h3>Want to curate a Deep Dive?</h3>\n'
        '    <p>If you teach, research, or practice in development and have a reading list worth sharing — pitch us.</p>\n'
        '    <a href="/contact.html?topic=DeepDive">Pitch a Deep Dive →</a>\n  </div>\n\n'
        '<svg class="im-paper-plane" viewBox="0 0 200 200" xmlns="http://www.w3.org/2000/svg" aria-hidden="true"><path d="M50,150 L150,50 L50,100 L80,130 Z" fill="none" stroke="#0EA5E9" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/><path d="M80,130 L150,50" stroke="#10B981" stroke-width="2" stroke-dasharray="4,4"/><circle cx="150" cy="50" r="4" fill="#6366F1"/></svg>\n'
        '</main>\n\n')

    doc = head + TOPBAR + '\n\n' + body + FOOTER + '\n\n' + SCRIPTS + '\n</body>\n</html>\n'
    out = os.path.join(ROOT, 'DeepDives', slug + '.html')
    open(out, 'w').write(doc)
    # sanity: reading_count should match item total
    total = sum(len(s['items']) for s in sections)
    assert total == reading_count, "reading_count %d != items %d" % (reading_count, total)
    return out, len(doc), total
