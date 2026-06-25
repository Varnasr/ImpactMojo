/* ImpactMojo — site-wide language switcher.
   Static-first: applies hard-wired, pre-translated strings shipped at
   /i18n/<lang>.json (built once by scripts/build-i18n.py) instantly, then a live
   fallback (/api/translate → Sarvam Mayura, server-cached) fills in any
   remaining strings progressively and caches them. The static dictionary is the
   high-quality source of truth and always wins; the fallback only covers the
   long tail. Disable the fallback with window.IMX_LIVE_TRANSLATE = false.
   Per-user localStorage cache + in-memory originals so switching back to
   English is instant.
   Add to any page:  <script src="/js/translate-sarvam.js" defer></script>
   Opt a subtree out of translation with  data-no-translate. */
(function () {
  "use strict";
  var LANGS = {
    en: { label: "EN", native: "English" },
    hi: { label: "हिन्दी", native: "हिन्दी", font: "Noto Sans Devanagari", url: "Noto+Sans+Devanagari:wght@400;500;600;700" },
    ta: { label: "தமிழ்", native: "தமிழ்", font: "Noto Sans Tamil", url: "Noto+Sans+Tamil:wght@400;500;600;700" },
    bn: { label: "বাংলা", native: "বাংলা", font: "Noto Sans Bengali", url: "Noto+Sans+Bengali:wght@400;500;600;700" },
    mr: { label: "मराठी", native: "मराठी", font: "Noto Sans Devanagari", url: "Noto+Sans+Devanagari:wght@400;500;600;700" },
    te: { label: "తెలుగు", native: "తెలుగు", font: "Noto Sans Telugu", url: "Noto+Sans+Telugu:wght@400;500;600;700" }
  };
  var SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, SVG: 1, CODE: 1, PRE: 1, KBD: 1, SAMP: 1, CANVAS: 1, TEXTAREA: 1, OPTION: 1 };
  // Brand / proper nouns that must never be translated
  var KEEP = { "ImpactMojo": 1, "ImpactLex": 1, "VaniScribe": 1, "Mojini": 1, "PinPoint Ventures": 1, "DevDiscourses": 1, "Dataverse": 1, "Bulbul": 1, "Mayura": 1, "Saaras": 1 };
  var KEY_LS = "im-lang";
  var originals = [];      // [{node, text}]
  var seen = (typeof WeakSet !== "undefined") ? new WeakSet() : null;
  var busy = false;
  var curLang = "en";

  function isTranslatable(s) {
    s = s.trim();
    if (s.length < 2) return false;
    if (KEEP[s]) return false;                            // brand / proper nouns
    if (!/[A-Za-z]/.test(s)) return false;               // needs letters
    if (/^(https?:\/\/|www\.|\S+@\S+)/.test(s)) return false; // urls/emails
    return true;
  }
  function skipEl(el) {
    while (el) {
      if (el.nodeType === 1) {
        if (SKIP[el.tagName]) return true;
        if (el.hasAttribute && (el.hasAttribute("data-no-translate") || el.getAttribute("translate") === "no")) return true;
        if (el.isContentEditable) return true;
      }
      el = el.parentNode;
    }
    return false;
  }
  function collect() {
    // Additive + idempotent: only adds new, untranslated text nodes. Safe to
    // re-run to catch content injected by deferred scripts.
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (seen && seen.has(n)) return NodeFilter.FILTER_REJECT;
        if (!isTranslatable(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        if (skipEl(n.parentNode)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = walker.nextNode())) { if (seen) seen.add(n); originals.push({ node: n, text: n.nodeValue }); }
  }

  function loadFont(lang) {
    var L = LANGS[lang];
    if (!L.url || document.getElementById("im-xlate-font-" + lang)) return;
    var l = document.createElement("link");
    l.id = "im-xlate-font-" + lang; l.rel = "stylesheet";
    l.href = "https://fonts.googleapis.com/css2?family=" + L.url + "&display=swap";
    document.head.appendChild(l);
    if (!document.getElementById("im-xlate-fontcss")) {
      var st = document.createElement("style"); st.id = "im-xlate-fontcss";
      st.textContent = 'html[data-imlang="hi"] body *:not(svg):not([class*="icon"]):not(.material-icons),' +
        'html[data-imlang="mr"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Devanagari",sans-serif!important}' +
        'html[data-imlang="ta"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Tamil",sans-serif!important}' +
        'html[data-imlang="te"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Telugu",sans-serif!important}' +
        'html[data-imlang="bn"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Bengali",sans-serif!important}';
      document.head.appendChild(st);
    }
  }

  function cacheGet(lang, s) { try { return localStorage.getItem("xlate:" + lang + ":" + s); } catch (e) { return null; } }
  function cacheSet(lang, s, t) { try { localStorage.setItem("xlate:" + lang + ":" + s, t); } catch (e) {} }

  // ---- Static dictionary (the hard-wired, pre-translated strings) -----------
  // Each language ships a flat { "English source": "translation" } map at
  // /i18n/<lang>.json, built once (scripts/build-i18n.py) and cached forever by
  // the CDN/browser. This is the primary source of truth: no API call, instant,
  // works offline, and any phrase can be corrected permanently in the JSON.
  var staticDict = {};   // { lang: {src: translation} }  — shared/common strings
  var staticTried = {};  // { lang: true } — don't refetch a 404
  function loadStaticDict(lang) {
    if (staticDict[lang] || staticTried[lang]) return Promise.resolve();
    staticTried[lang] = true;
    return fetch("/i18n/" + lang + ".json", { cache: "force-cache" })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { staticDict[lang] = d || {}; })
      .catch(function () { staticDict[lang] = {}; });
  }

  // ---- Per-page dictionary -------------------------------------------------
  // The common dict above holds strings that recur across the site. Everything
  // else lives in a per-page file at /i18n/pages/<lang>/<pageKey>.json so each
  // page downloads only its own strings (not one giant site-wide dictionary).
  // pageKey is derived from the URL path; the build script uses the same rule.
  var pageDict = {};     // { lang: {src: translation} }
  var pageTried = {};    // { "lang:key": true }
  function pageKey() {
    var p = location.pathname.replace(/\/+$/, "").replace(/\/index\.html?$/i, "").replace(/\.html?$/i, "").replace(/^\/+/, "");
    if (!p) p = "index";
    return p.replace(/[^A-Za-z0-9._-]+/g, "__");
  }
  function loadPageDict(lang) {
    var key = lang + ":" + pageKey();
    if (pageDict[lang] || pageTried[key]) return Promise.resolve();
    pageTried[key] = true;
    return fetch("/i18n/pages/" + lang + "/" + pageKey() + ".json", { cache: "force-cache" })
      .then(function (r) { return r.ok ? r.json() : {}; })
      .then(function (d) { pageDict[lang] = d || {}; })
      .catch(function () { pageDict[lang] = {}; });
  }

  async function apiBatch(lang, batch) {
    try {
      var r = await fetch("/api/translate", {
        method: "POST", headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ lang: lang, q: batch })
      });
      if (r.ok) { var d = await r.json(); return d.t || {}; }
    } catch (e) { /* network — leave untranslated */ }
    return {};
  }

  // Apply whatever translations are known so far (idempotent). Lets us render
  // progressively, batch by batch, instead of all-or-nothing at the end.
  function applyTranslations(uniq) {
    for (var j = 0; j < originals.length; j++) {
      var o = originals[j], t = uniq[o.text.trim()];
      if (t && o.node.nodeValue === o.text) {
        var lead = o.text.match(/^\s*/)[0], trail = o.text.match(/\s*$/)[0];
        o.node.nodeValue = lead + t.trim() + trail;
      }
    }
  }

  function restoreEnglish() {
    for (var i = 0; i < originals.length; i++) originals[i].node.nodeValue = originals[i].text;
    document.documentElement.removeAttribute("data-imlang");
    document.documentElement.setAttribute("lang", "en");
  }

  async function translateTo(lang, isRepass) {
    if (busy) return;
    curLang = lang;
    if (lang === "en") { restoreEnglish(); save(lang); markActive(lang); return; }
    busy = true; markBusy(true);
    collect(); loadFont(lang);
    await Promise.all([loadStaticDict(lang), loadPageDict(lang)]);
    document.documentElement.setAttribute("data-imlang", lang);
    document.documentElement.setAttribute("lang", lang);
    var common = staticDict[lang] || {}, page = pageDict[lang] || {};
    // Resolve each unique source string: localStorage cache -> page dict ->
    // common dict (page-specific wins, then the shared dictionary).
    var uniq = {}, order = [];
    for (var i = 0; i < originals.length; i++) {
      var s = originals[i].text.trim();
      if (s in uniq) continue;
      var hit = cacheGet(lang, s);
      if (hit == null && page[s] != null) hit = page[s];
      if (hit == null && common[s] != null) hit = common[s];
      uniq[s] = hit;
      if (hit == null) order.push(s);        // not yet translated anywhere
    }
    applyTranslations(uniq);                  // apply everything we know, instantly
    // Live fallback for strings missing from the static dictionary: machine-
    // translate via /api/translate (Sarvam Mayura, server-cached) and cache the
    // result per-user. The static dictionary is still the source of truth and is
    // applied FIRST (above), so the shell renders instantly; this only fills in
    // the long-tail body content progressively, batch by batch. It cannot hang
    // the page (bounded batches, busy-guard, no Google-mutation loop). Disable by
    // setting window.IMX_LIVE_TRANSLATE = false before this script loads.
    if (window.IMX_LIVE_TRANSLATE !== false && order.length) {
      for (var j = 0; j < order.length; j += 12) {
        if (curLang !== lang) break;          // user switched away — stop
        var fetched = await apiBatch(lang, order.slice(j, j + 12));
        for (var k in fetched) {
          if (fetched[k] && fetched[k] !== k) { uniq[k] = fetched[k]; cacheSet(lang, k, fetched[k]); }
        }
        applyTranslations(uniq);
      }
    }
    save(lang); markActive(lang); busy = false; markBusy(false);
    // one delayed pass to catch content added by deferred scripts (auth bar, etc.)
    if (!isRepass) setTimeout(function () { if (curLang === lang) translateTo(lang, true); }, 3000);
  }

  function save(lang) { try { localStorage.setItem(KEY_LS, lang); } catch (e) {} }

  // ---- UI: compact collapsible globe (stacks ABOVE the cookie, bottom-left) ----
  // A single 44px round button; tapping it opens a small upward popover with the
  // five languages, then collapses. Replaces the old wide pill that overlapped
  // the cookie / accessibility widgets on mobile.
  var fab, menu, isOpen = false;

  function markActive(lang) {
    if (menu) {
      [].forEach.call(menu.querySelectorAll("button"), function (b) {
        var on = b.dataset.l === lang;
        b.style.background = on ? "rgba(29,78,216,0.95)" : "transparent";
        b.style.color = on ? "#fff" : "#1e293b";
        b.style.fontWeight = on ? "700" : "600";
      });
    }
    if (fab) {
      var lbl = fab.querySelector(".im-fab-lbl");
      if (lbl) {
        if (lang === "en") { lbl.style.display = "none"; lbl.textContent = ""; }
        else { lbl.textContent = LANGS[lang].label; lbl.style.display = "block"; }
      }
    }
  }
  function markBusy(on) {
    if (!fab) return;
    var sp = fab.querySelector(".im-fab-spin");
    if (sp) sp.style.display = on ? "block" : "none";
  }
  function toggleMenu(force) {
    isOpen = (typeof force === "boolean") ? force : !isOpen;
    if (menu) {
      menu.style.opacity = isOpen ? "1" : "0";
      menu.style.visibility = isOpen ? "visible" : "hidden";
      menu.style.transform = isOpen ? "translateY(0)" : "translateY(8px)";
    }
    if (fab) fab.setAttribute("aria-expanded", isOpen ? "true" : "false");
  }
  function buildUI() {
    // Prefer mounting inline in the top navigation. The content-page topbar
    // (.im-topbar-right) is visible at every breakpoint; the homepage's
    // .nav-buttons is display:none on mobile, so only mount inline when the
    // target is actually visible — otherwise fall back to the floating globe
    // so the switcher is never hidden.
    var navTarget = document.querySelector(".im-topbar-right") || document.querySelector(".nav-buttons");
    var inNav = !!navTarget && navTarget.offsetParent !== null;

    var wrap = document.createElement("div");
    wrap.id = "im-lang-switch"; wrap.setAttribute("data-no-translate", "");
    wrap.className = inNav ? "im-lang-innav" : "im-lang-floating";
    wrap.style.cssText = inNav
      ? "position:relative;display:inline-flex;align-items:center;z-index:9990;font-family:system-ui,-apple-system,sans-serif"
      // Floating fallback (mainly the homepage on mobile, where the nav buttons
      // collapse): sit above the speed-dial FAB so the two don't overlap.
      : "position:fixed;right:16px;bottom:5.5rem;z-index:9990;font-family:system-ui,-apple-system,sans-serif";

    // popover menu — drops DOWN when in the nav, UP when floating
    menu = document.createElement("div");
    menu.setAttribute("role", "menu"); menu.setAttribute("aria-label", "Choose language");
    menu.style.cssText = "position:absolute;" + (inNav ? "top:46px;" : "bottom:54px;") + "right:0;left:auto;display:flex;flex-direction:column;gap:3px;" +
      "background:#fff;border:1px solid rgba(0,0,0,0.12);border-radius:14px;padding:5px;" +
      "box-shadow:0 8px 28px rgba(0,0,0,0.18);min-width:130px;z-index:10000;" +
      "opacity:0;visibility:hidden;transform:translateY(8px);transition:opacity .18s ease,transform .18s ease,visibility .18s";
    Object.keys(LANGS).forEach(function (code) {
      var b = document.createElement("button");
      b.dataset.l = code; b.type = "button"; b.setAttribute("role", "menuitem");
      b.textContent = LANGS[code].native; b.title = LANGS[code].native;
      b.style.cssText = "border:none;cursor:pointer;font-size:14px;font-weight:600;text-align:left;" +
        "padding:9px 12px;border-radius:10px;background:transparent;color:#1e293b;white-space:nowrap";
      b.addEventListener("click", function () { translateTo(code); toggleMenu(false); });
      menu.appendChild(b);
    });
    wrap.appendChild(menu);

    // round globe button (slightly smaller, no drop-shadow when sitting in the nav)
    var sz = inNav ? 38 : 44;
    fab = document.createElement("button");
    fab.type = "button"; fab.className = "im-fab";
    fab.setAttribute("aria-label", "Choose language");
    fab.setAttribute("aria-haspopup", "true"); fab.setAttribute("aria-expanded", "false");
    fab.style.cssText = "width:" + sz + "px;height:" + sz + "px;border-radius:50%;background:#fff;padding:0;" +
      "border:2px solid rgba(0,0,0,0.12);" + (inNav ? "box-shadow:none;" : "box-shadow:0 4px 15px rgba(0,0,0,0.2);") + "cursor:pointer;" +
      "display:flex;align-items:center;justify-content:center;position:relative;transition:transform .2s ease";
    fab.innerHTML =
      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#1D4ED8" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"></circle><path d="M3 12h18"></path><path d="M12 3a14 14 0 0 1 0 18 14 14 0 0 1 0-18z"></path></svg>' +
      '<span class="im-fab-lbl" style="display:none;position:absolute;bottom:-4px;right:-4px;background:#1D4ED8;color:#fff;font-size:9px;font-weight:700;line-height:1;padding:2px 4px;border-radius:8px;min-width:8px;text-align:center;box-shadow:0 1px 3px rgba(0,0,0,.3)"></span>' +
      '<span class="im-fab-spin" style="display:none;position:absolute;inset:-3px;border-radius:50%;border:2px solid transparent;border-top-color:#1D4ED8;animation:imXlateSpin .8s linear infinite"></span>';
    fab.addEventListener("click", function (e) { e.stopPropagation(); toggleMenu(); });
    wrap.appendChild(fab);

    var kf = document.createElement("style");
    kf.textContent = "@keyframes imXlateSpin{to{transform:rotate(360deg)}}" +
      "#im-lang-switch .im-fab:active{transform:scale(.93)}" +
      "#im-lang-switch [role=menuitem]:hover{background:rgba(0,0,0,0.05)!important}" +
      "@media(max-width:480px){#im-lang-switch.im-lang-floating{right:14px!important;bottom:5.5rem!important}}";
    document.head.appendChild(kf);

    // collapse on outside tap / Escape
    document.addEventListener("click", function () { if (isOpen) toggleMenu(false); });
    document.addEventListener("keydown", function (e) { if (e.key === "Escape" && isOpen) toggleMenu(false); });

    if (inNav) navTarget.insertBefore(wrap, navTarget.firstChild);
    else document.body.appendChild(wrap);
  }

  // Translate content injected later (flagship Supabase module bodies, auth bar,
  // search results...) whenever a non-English language is active. Observing only
  // childList means our own nodeValue edits don't retrigger it (no loop).
  function startObserver() {
    if (!window.MutationObserver) return;
    var t;
    new MutationObserver(function () {
      if (curLang === "en" || busy) return;
      clearTimeout(t);
      t = setTimeout(function () { if (curLang !== "en" && !busy) translateTo(curLang, true); }, 800);
    }).observe(document.body, { childList: true, subtree: true });
  }

  function init() {
    buildUI();
    startObserver();
    var saved = null; try { saved = localStorage.getItem(KEY_LS); } catch (e) {}
    if (saved && saved !== "en" && LANGS[saved]) translateTo(saved); else markActive("en");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
