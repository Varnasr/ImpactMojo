/* LMS export — turn a published ImpactMojo course into a package an LMS can import.
 *
 * Everything happens in the visitor's browser. There is no build step and no
 * server, so the alternative would have been committing a zip per course (71 of
 * them, rebuilt on every content edit and stale the moment one drifted). Fetching
 * the live page and packaging it on demand means an export is always the course
 * as it stands right now.
 *
 * Four formats, one pipeline. SCORM 1.2 and 2004 differ only in manifest and API
 * discovery; Common Cartridge is the same payload with an IMS manifest; "web"
 * is the payload with no manifest at all.
 *
 * The payload step matters more than the manifest step. A course page carries
 * analytics, auth, Supabase, translation and the shared site chrome, none of
 * which belong inside someone else's LMS -- they would phone home from a
 * student's session, and several would throw where the origin no longer matches.
 * buildPayload() strips them and inlines what remains, so the exported file
 * opens with no network at all.
 */
(function () {
  'use strict';

  var CHART_CDN = 'https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js';

  // Scripts that are site plumbing rather than course content. Matched against
  // the src attribute; inline blocks are matched by content in stripInline().
  var DROP_SRC = [
    'googletagmanager', 'gtag/js', 'google-analytics',
    'supabase', 'state-manager', 'config.js', 'auth.js',
    'site-chrome', 'translate-sarvam', 'pwa.js', 'offline.js',
    'search.js', 'tours.js', 'feedback', 'mojini'
  ];
  var DROP_INLINE = [
    'gtag(', 'dataLayer', 'serviceWorker', 'supabase', 'createClient',
    'G-JRCMEB9TBW'
  ];

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;')
      .replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&apos;');
  }

  // A manifest identifier must be a valid XML NCName: letters/digits/._- and it
  // may not start with a digit. Course slugs are already close, but "101-csr-esg"
  // starts with a digit and would produce a manifest an LMS rejects at import.
  function ncname(s) {
    var v = String(s).replace(/[^A-Za-z0-9._-]/g, '-');
    return /^[A-Za-z_]/.test(v) ? v : 'im-' + v;
  }

  function absolutise(url, base) {
    try { return new URL(url, base).href; } catch (e) { return url; }
  }

  function fetchText(url) {
    return fetch(url, { credentials: 'omit' }).then(function (r) {
      if (!r.ok) throw new Error(r.status + ' ' + r.statusText);
      return r.text();
    });
  }

  /* ---- payload -------------------------------------------------------- */

  /* Fetch the course page and rewrite it into one self-contained file.
   * onStep reports progress; the caller shows it, because inlining Chart.js
   * over a slow connection is several seconds of apparent nothing. */
  function buildPayload(courseUrl, opts, onStep) {
    opts = opts || {};
    onStep = onStep || function () {};
    var base = absolutise(courseUrl, location.href);

    onStep('Fetching the course…');
    return fetchText(base).then(function (html) {
      var doc = new DOMParser().parseFromString(html, 'text/html');

      onStep('Removing site analytics and login code…');
      stripSiteOnly(doc);

      onStep('Inlining stylesheets…');
      return inlineAll(doc, base, 'link[rel=stylesheet][href]', 'href', function (d, node, text) {
        var st = d.createElement('style');
        st.textContent = text;
        node.parentNode.replaceChild(st, node);
      }).then(function () {
        onStep('Inlining scripts…');
        return inlineAll(doc, base, 'script[src]', 'src', function (d, node, text) {
          var sc = d.createElement('script');
          sc.textContent = text;
          node.parentNode.replaceChild(sc, node);
        });
      }).then(function () {
        // Absolutise anything still pointing at the site, so links in an
        // exported file resolve from wherever the LMS serves it.
        rebaseLinks(doc, base);
        if (opts.scorm) injectScormWrapper(doc, opts.scorm);
        addProvenance(doc, base, opts);
        return '<!DOCTYPE html>\n' + doc.documentElement.outerHTML;
      });
    });
  }

  function stripSiteOnly(doc) {
    Array.prototype.slice.call(doc.querySelectorAll('script')).forEach(function (s) {
      var src = s.getAttribute('src') || '';
      if (src) {
        for (var i = 0; i < DROP_SRC.length; i++) {
          if (src.indexOf(DROP_SRC[i]) !== -1) { s.remove(); return; }
        }
      } else {
        var t = s.textContent || '';
        for (var j = 0; j < DROP_INLINE.length; j++) {
          if (t.indexOf(DROP_INLINE[j]) !== -1) { s.remove(); return; }
        }
      }
    });
    // The service-worker registration and any PWA manifest are meaningless on
    // another origin and register against the LMS instead.
    var m = doc.querySelector('link[rel=manifest]');
    if (m) m.remove();
  }

  /* Replace every same-origin (or CDN) asset with its inline text. Failures are
   * collected rather than thrown: one unreachable stylesheet should degrade the
   * export, not abort it. */
  function inlineAll(doc, base, selector, attr, replace) {
    var nodes = Array.prototype.slice.call(doc.querySelectorAll(selector));
    var jobs = nodes.map(function (node) {
      var raw = node.getAttribute(attr);
      var url = absolutise(raw, base);
      // Only same-origin assets and the known Chart.js CDN are inlined.
      var same = url.indexOf(location.origin) === 0;
      var isChart = url.indexOf('cdn.jsdelivr.net') !== -1;
      if (!same && !isChart) return Promise.resolve();
      return fetchText(url).then(function (text) {
        replace(doc, node, text);
      }).catch(function () {
        // Leave the node pointing at the absolute URL; the export still works
        // online, and addProvenance() records that it is not fully offline.
        node.setAttribute(attr, url);
        buildPayload._degraded = true;
      });
    });
    return Promise.all(jobs);
  }

  function rebaseLinks(doc, base) {
    ['a[href]', 'img[src]', 'source[src]'].forEach(function (sel) {
      Array.prototype.slice.call(doc.querySelectorAll(sel)).forEach(function (n) {
        var a = n.hasAttribute('href') ? 'href' : 'src';
        var v = n.getAttribute(a) || '';
        if (!v || v.charAt(0) === '#' || /^(mailto:|tel:|data:|https?:)/i.test(v)) return;
        n.setAttribute(a, absolutise(v, base));
      });
    });
  }

  function addProvenance(doc, base, opts) {
    var when = new Date().toISOString().slice(0, 10);
    var note = doc.createComment(
      ' Exported from ImpactMojo (' + base + ') on ' + when + '.\n' +
      '     Licence: CC BY-NC-ND 4.0 — use in teaching with attribution;\n' +
      '     do not sell the materials or publish modified versions.\n' +
      '     ' + (buildPayload._degraded
        ? 'NOTE: some assets could not be inlined and still load from the web.'
        : 'This file is self-contained and works with no network.') + ' ');
    doc.head.insertBefore(note, doc.head.firstChild);
  }

  /* ---- SCORM ---------------------------------------------------------- */

  /* The runtime wrapper. Finds the LMS API (1.2 exposes window.API on some
   * ancestor or the opener; 2004 exposes API_1484_11), reports the course
   * incomplete on open and complete when the learner reaches the final slide,
   * and commits on unload.
   *
   * It hooks the deck's own showSlide() rather than counting clicks, so the
   * completion signal follows real navigation including keyboard and deep links.
   * If the deck ever stops exposing showSlide the wrapper degrades to marking
   * completion on unload, which is why findApi failures are silent: a missing
   * LMS API must never break the content for a learner. */
  function scormWrapperSource(version) {
    var apiName = version === '2004' ? 'API_1484_11' : 'API';
    var kCompletion = version === '2004' ? 'cmi.completion_status' : 'cmi.core.lesson_status';
    var kInit = version === '2004' ? 'Initialize' : 'LMSInitialize';
    var kSet = version === '2004' ? 'SetValue' : 'LMSSetValue';
    var kCommit = version === '2004' ? 'Commit' : 'LMSCommit';
    var kFinish = version === '2004' ? 'Terminate' : 'LMSFinish';
    return [
      '(function(){',
      '  "use strict";',
      '  var API=null, started=false, done=false;',
      '  function findApi(win,depth){',
      '    while(win && depth-- > 0){',
      '      if(win.' + apiName + ') return win.' + apiName + ';',
      '      if(win.parent === win) break;',
      '      win = win.parent;',
      '    }',
      '    return null;',
      '  }',
      '  API = findApi(window,12) || (window.opener ? findApi(window.opener,12) : null);',
      '  function set(k,v){ try{ API && API.' + kSet + '(k,String(v)); }catch(e){} }',
      '  function commit(){ try{ API && API.' + kCommit + '(""); }catch(e){} }',
      '  function start(){',
      '    if(started || !API) return; started=true;',
      '    try{ API.' + kInit + '(""); }catch(e){}',
      '    set("' + kCompletion + '","incomplete");',
      '    commit();',
      '  }',
      '  function complete(){',
      '    if(done) return; done=true;',
      '    set("' + kCompletion + '","completed");',
      (version === '2004' ? '    set("cmi.success_status","passed");' : ''),
      '    commit();',
      '  }',
      '  start();',
      '  // Hook the deck\'s navigation so completion follows real progress.',
      '  var total = (window.slides && window.slides.length) || 0;',
      '  var orig = window.showSlide;',
      '  if(typeof orig === "function"){',
      '    window.showSlide = function(n){',
      '      var r = orig.apply(this, arguments);',
      '      try{',
      '        var t = (window.slides && window.slides.length) || total;',
      '        if(t && typeof window.cur === "number"){',
      '          set("' + (version === '2004' ? 'cmi.progress_measure' : 'cmi.core.lesson_location') + '",',
      (version === '2004'
        ? '            Math.min(1,(window.cur+1)/t));'
        : '            String(window.cur+1));'),
      '          if(window.cur >= t-1) complete();',
      '        }',
      '      }catch(e){}',
      '      return r;',
      '    };',
      '  }',
      '  window.addEventListener("beforeunload",function(){',
      '    commit();',
      '    try{ API && API.' + kFinish + '(""); }catch(e){}',
      '  });',
      '})();'
    ].join('\n');
  }

  function injectScormWrapper(doc, version) {
    var s = doc.createElement('script');
    s.setAttribute('data-impactmojo', 'scorm-' + version);
    s.textContent = scormWrapperSource(version);
    doc.body.appendChild(s);
  }

  /* ---- manifests ------------------------------------------------------ */

  function scorm12Manifest(meta) {
    var id = ncname(meta.slug);
    return '<?xml version="1.0" encoding="UTF-8"?>\n' +
'<manifest identifier="' + id + '" version="1.2"\n' +
'  xmlns="http://www.imsproject.org/xsd/imscp_rootv1p1p2"\n' +
'  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_rootv1p2"\n' +
'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
'  xsi:schemaLocation="http://www.imsproject.org/xsd/imscp_rootv1p1p2 imscp_rootv1p1p2.xsd\n' +
'                      http://www.adlnet.org/xsd/adlcp_rootv1p2 adlcp_rootv1p2.xsd">\n' +
'  <metadata>\n' +
'    <schema>ADL SCORM</schema>\n' +
'    <schemaversion>1.2</schemaversion>\n' +
'  </metadata>\n' +
'  <organizations default="' + id + '-org">\n' +
'    <organization identifier="' + id + '-org">\n' +
'      <title>' + esc(meta.title) + '</title>\n' +
'      <item identifier="' + id + '-item" identifierref="' + id + '-res" isvisible="true">\n' +
'        <title>' + esc(meta.title) + '</title>\n' +
'        <adlcp:masteryscore>100</adlcp:masteryscore>\n' +
'      </item>\n' +
'    </organization>\n' +
'  </organizations>\n' +
'  <resources>\n' +
'    <resource identifier="' + id + '-res" type="webcontent" adlcp:scormtype="sco" href="index.html">\n' +
'      <file href="index.html"/>\n' +
'    </resource>\n' +
'  </resources>\n' +
'</manifest>\n';
  }

  function scorm2004Manifest(meta) {
    var id = ncname(meta.slug);
    return '<?xml version="1.0" encoding="UTF-8"?>\n' +
'<manifest identifier="' + id + '" version="1.0"\n' +
'  xmlns="http://www.imsglobal.org/xsd/imscp_v1p1"\n' +
'  xmlns:adlcp="http://www.adlnet.org/xsd/adlcp_v1p3"\n' +
'  xmlns:adlseq="http://www.adlnet.org/xsd/adlseq_v1p3"\n' +
'  xmlns:adlnav="http://www.adlnet.org/xsd/adlnav_v1p3"\n' +
'  xmlns:imsss="http://www.imsglobal.org/xsd/imsss"\n' +
'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
'  xsi:schemaLocation="http://www.imsglobal.org/xsd/imscp_v1p1 imscp_v1p1.xsd\n' +
'                      http://www.adlnet.org/xsd/adlcp_v1p3 adlcp_v1p3.xsd\n' +
'                      http://www.adlnet.org/xsd/adlseq_v1p3 adlseq_v1p3.xsd\n' +
'                      http://www.adlnet.org/xsd/adlnav_v1p3 adlnav_v1p3.xsd\n' +
'                      http://www.imsglobal.org/xsd/imsss imsss_v1p0.xsd">\n' +
'  <metadata>\n' +
'    <schema>ADL SCORM</schema>\n' +
'    <schemaversion>2004 4th Edition</schemaversion>\n' +
'  </metadata>\n' +
'  <organizations default="' + id + '-org">\n' +
'    <organization identifier="' + id + '-org">\n' +
'      <title>' + esc(meta.title) + '</title>\n' +
'      <item identifier="' + id + '-item" identifierref="' + id + '-res">\n' +
'        <title>' + esc(meta.title) + '</title>\n' +
'      </item>\n' +
'    </organization>\n' +
'  </organizations>\n' +
'  <resources>\n' +
'    <resource identifier="' + id + '-res" type="webcontent" adlcp:scormType="sco" href="index.html">\n' +
'      <file href="index.html"/>\n' +
'    </resource>\n' +
'  </resources>\n' +
'</manifest>\n';
  }

  function commonCartridgeManifest(meta) {
    var id = ncname(meta.slug);
    return '<?xml version="1.0" encoding="UTF-8"?>\n' +
'<manifest identifier="' + id + '"\n' +
'  xmlns="http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1"\n' +
'  xmlns:lomimscc="http://ltsc.ieee.org/xsd/imsccv1p3/LOM/manifest"\n' +
'  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"\n' +
'  xsi:schemaLocation="http://www.imsglobal.org/xsd/imsccv1p3/imscp_v1p1 imscp_v1p3.xsd">\n' +
'  <metadata>\n' +
'    <schema>IMS Common Cartridge</schema>\n' +
'    <schemaversion>1.3.0</schemaversion>\n' +
'    <lomimscc:lom>\n' +
'      <lomimscc:general>\n' +
'        <lomimscc:title><lomimscc:string>' + esc(meta.title) + '</lomimscc:string></lomimscc:title>\n' +
'        <lomimscc:description><lomimscc:string>' + esc(meta.description || meta.title) + '</lomimscc:string></lomimscc:description>\n' +
'      </lomimscc:general>\n' +
'      <lomimscc:rights>\n' +
'        <lomimscc:copyrightAndOtherRestrictions>\n' +
'          <lomimscc:value>yes</lomimscc:value>\n' +
'        </lomimscc:copyrightAndOtherRestrictions>\n' +
'        <lomimscc:description><lomimscc:string>CC BY-NC-ND 4.0 — ImpactMojo</lomimscc:string></lomimscc:description>\n' +
'      </lomimscc:rights>\n' +
'    </lomimscc:lom>\n' +
'  </metadata>\n' +
'  <organizations>\n' +
'    <organization identifier="' + id + '-org" structure="rooted-hierarchy">\n' +
'      <item identifier="root">\n' +
'        <item identifier="' + id + '-item" identifierref="' + id + '-res">\n' +
'          <title>' + esc(meta.title) + '</title>\n' +
'        </item>\n' +
'      </item>\n' +
'    </organization>\n' +
'  </organizations>\n' +
'  <resources>\n' +
'    <resource identifier="' + id + '-res" type="webcontent" href="index.html">\n' +
'      <file href="index.html"/>\n' +
'    </resource>\n' +
'  </resources>\n' +
'</manifest>\n';
  }

  function readme(meta, format) {
    var how = {
      scorm12: 'Upload the .zip as a SCORM package.\n' +
        '  Moodle:  Add an activity > SCORM package > upload this file.\n' +
        '  Canvas:  Settings > Import Course Content > SCORM package.\n' +
        '  Blackboard: Build Content > Content Package (SCORM).\n' +
        'Completion is reported when a learner reaches the final slide.',
      scorm2004: 'Upload the .zip as a SCORM 2004 package.\n' +
        'Use this only if your LMS specifically wants 2004; SCORM 1.2 is more\n' +
        'widely supported and reports the same completion.',
      cc: 'Upload the .imscc as a Common Cartridge.\n' +
        '  Moodle:  Restore / Import > Common Cartridge.\n' +
        '  Canvas:  Import Course Content > Common Cartridge.\n' +
        'Common Cartridge carries no completion tracking — use SCORM if you\n' +
        'need the LMS to record who finished.',
      web: 'A single HTML file. Upload it anywhere and link to it, or open it\n' +
        'locally in a browser. No tracking, no LMS required.'
    }[format];
    return 'ImpactMojo — ' + meta.title + '\n' +
      new Array(('ImpactMojo — ' + meta.title).length + 1).join('=') + '\n\n' +
      'Source:  ' + absolutise(meta.url, location.href) + '\n' +
      'Exported: ' + new Date().toISOString().slice(0, 10) + '\n\n' +
      'HOW TO USE\n----------\n' + how + '\n\n' +
      'LICENCE\n-------\n' +
      'CC BY-NC-ND 4.0. Use it in your teaching and credit\n' +
      '"Content from ImpactMojo — impactmojo.in". You may charge for your\n' +
      'facilitation; you may not sell these materials or publish modified\n' +
      'versions. For adaptations or translations, write to us — we are\n' +
      'flexible with mission-aligned use.\n\n' +
      'A NOTE ON ACCURACY\n------------------\n' +
      'This is a snapshot taken on the date above. Courses are revised; law\n' +
      'and statistics in them go out of date. Check the source URL before\n' +
      'teaching from an old export.\n';
  }

  /* ---- package -------------------------------------------------------- */

  function build(meta, format, onStep) {
    if (typeof JSZip === 'undefined') {
      return Promise.reject(new Error('The packaging library did not load. Reload the page and try again.'));
    }
    buildPayload._degraded = false;
    var scorm = format === 'scorm12' ? '1.2' : (format === 'scorm2004' ? '2004' : null);

    return buildPayload(meta.url, { scorm: scorm }, onStep).then(function (html) {
      if (format === 'web') {
        return { blob: new Blob([html], { type: 'text/html' }),
                 name: meta.slug + '.html', degraded: buildPayload._degraded };
      }
      onStep('Building the package…');
      var zip = new JSZip();
      zip.file('index.html', html);
      zip.file('README.txt', readme(meta, format));
      var ext = 'zip';
      if (format === 'scorm12') zip.file('imsmanifest.xml', scorm12Manifest(meta));
      else if (format === 'scorm2004') zip.file('imsmanifest.xml', scorm2004Manifest(meta));
      else if (format === 'cc') { zip.file('imsmanifest.xml', commonCartridgeManifest(meta)); ext = 'imscc'; }

      onStep('Compressing…');
      return zip.generateAsync({ type: 'blob', compression: 'DEFLATE' }).then(function (blob) {
        return { blob: blob, name: meta.slug + '-' + format + '.' + ext,
                 degraded: buildPayload._degraded };
      });
    });
  }

  window.IMLmsExport = {
    build: build,
    buildPayload: buildPayload,
    // exported for the test harness
    _ncname: ncname,
    _manifests: { scorm12: scorm12Manifest, scorm2004: scorm2004Manifest, cc: commonCartridgeManifest },
    _wrapper: scormWrapperSource
  };
})();
