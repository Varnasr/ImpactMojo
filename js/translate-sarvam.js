/* ImpactMojo — site-wide Sarvam-backed language switcher.
   Translates the current page's visible text on demand via /api/translate
   (Netlify function → Sarvam Mayura, server-cached). Per-user localStorage
   cache + in-memory originals so switching back to English is instant.
   Add to any page:  <script src="/js/translate-sarvam.js" defer></script>
   Opt a subtree out of translation with  data-no-translate. */
(function () {
  "use strict";
  var LANGS = {
    en: { label: "EN", native: "English" },
    hi: { label: "हिन्दी", native: "हिन्दी", font: "Noto Sans Devanagari", url: "Noto+Sans+Devanagari:wght@400;500;600;700" },
    ta: { label: "தமிழ்", native: "தமிழ்", font: "Noto Sans Tamil", url: "Noto+Sans+Tamil:wght@400;500;600;700" },
    bn: { label: "বাংলা", native: "বাংলা", font: "Noto Sans Bengali", url: "Noto+Sans+Bengali:wght@400;500;600;700" },
    mr: { label: "मराठी", native: "मराठी", font: "Noto Sans Devanagari", url: "Noto+Sans+Devanagari:wght@400;500;600;700" }
  };
  var SKIP = { SCRIPT: 1, STYLE: 1, NOSCRIPT: 1, SVG: 1, CODE: 1, PRE: 1, KBD: 1, SAMP: 1, CANVAS: 1, TEXTAREA: 1, OPTION: 1 };
  var KEY_LS = "im-lang";
  var originals = [];      // [{node, text}]
  var collected = false;
  var busy = false;

  function isTranslatable(s) {
    s = s.trim();
    if (s.length < 2) return false;
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
    if (collected) return;
    var walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT, {
      acceptNode: function (n) {
        if (!isTranslatable(n.nodeValue)) return NodeFilter.FILTER_REJECT;
        if (skipEl(n.parentNode)) return NodeFilter.FILTER_REJECT;
        return NodeFilter.FILTER_ACCEPT;
      }
    });
    var n;
    while ((n = walker.nextNode())) originals.push({ node: n, text: n.nodeValue });
    collected = true;
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
        'html[data-imlang="bn"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Bengali",sans-serif!important}';
      document.head.appendChild(st);
    }
  }

  function cacheGet(lang, s) { try { return localStorage.getItem("xlate:" + lang + ":" + s); } catch (e) { return null; } }
  function cacheSet(lang, s, t) { try { localStorage.setItem("xlate:" + lang + ":" + s, t); } catch (e) {} }

  async function apiTranslate(lang, misses) {
    var out = {};
    for (var i = 0; i < misses.length; i += 60) {
      var batch = misses.slice(i, i + 60);
      try {
        var r = await fetch("/api/translate", {
          method: "POST", headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ lang: lang, q: batch })
        });
        if (r.ok) { var d = await r.json(); Object.assign(out, d.t || {}); }
      } catch (e) { /* network — leave untranslated */ }
    }
    return out;
  }

  function restoreEnglish() {
    for (var i = 0; i < originals.length; i++) originals[i].node.nodeValue = originals[i].text;
    document.documentElement.removeAttribute("data-imlang");
    document.documentElement.setAttribute("lang", "en");
  }

  async function translateTo(lang) {
    if (busy) return;
    if (lang === "en") { restoreEnglish(); save(lang); markActive(lang); return; }
    busy = true; markBusy(true);
    collect(); loadFont(lang);
    document.documentElement.setAttribute("data-imlang", lang);
    document.documentElement.setAttribute("lang", lang);
    // unique source strings
    var uniq = {}, order = [];
    for (var i = 0; i < originals.length; i++) {
      var s = originals[i].text.trim();
      if (!(s in uniq)) { uniq[s] = cacheGet(lang, s); if (uniq[s] == null) order.push(s); }
    }
    if (order.length) {
      var fetched = await apiTranslate(lang, order);
      for (var k in fetched) { uniq[k] = fetched[k]; cacheSet(lang, k, fetched[k]); }
    }
    for (var j = 0; j < originals.length; j++) {
      var t = uniq[originals[j].text.trim()];
      if (t) {
        var raw = originals[j].node.nodeValue, lead = raw.match(/^\s*/)[0], trail = raw.match(/\s*$/)[0];
        originals[j].node.nodeValue = lead + t + trail;
      }
    }
    save(lang); markActive(lang); busy = false; markBusy(false);
  }

  function save(lang) { try { localStorage.setItem(KEY_LS, lang); } catch (e) {} }

  // ---- UI ----
  var bar;
  function markActive(lang) {
    if (!bar) return;
    [].forEach.call(bar.querySelectorAll("button"), function (b) {
      b.style.background = b.dataset.l === lang ? "rgba(29,78,216,0.9)" : "transparent";
      b.style.color = b.dataset.l === lang ? "#fff" : "rgba(120,120,120,0.95)";
    });
  }
  function markBusy(on) { if (bar) bar.style.opacity = on ? "0.6" : "1"; }
  function buildUI() {
    bar = document.createElement("div");
    bar.id = "im-lang-switch"; bar.setAttribute("data-no-translate", "");
    bar.setAttribute("aria-label", "Language");
    bar.style.cssText = "position:fixed;bottom:14px;left:14px;z-index:99998;display:flex;gap:2px;" +
      "background:rgba(255,255,255,0.92);backdrop-filter:blur(8px);border:1px solid rgba(0,0,0,0.1);" +
      "border-radius:999px;padding:3px;box-shadow:0 4px 14px rgba(0,0,0,0.15);font-family:system-ui,sans-serif";
    Object.keys(LANGS).forEach(function (code) {
      var b = document.createElement("button");
      b.textContent = LANGS[code].label; b.dataset.l = code;
      b.title = LANGS[code].native;
      b.style.cssText = "border:none;cursor:pointer;font-size:12px;font-weight:600;padding:5px 9px;border-radius:999px;background:transparent;color:rgba(120,120,120,0.95)";
      b.addEventListener("click", function () { translateTo(code); });
      bar.appendChild(b);
    });
    document.body.appendChild(bar);
  }

  function init() {
    buildUI();
    var saved = null; try { saved = localStorage.getItem(KEY_LS); } catch (e) {}
    if (saved && saved !== "en" && LANGS[saved]) translateTo(saved); else markActive("en");
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", init);
  else init();
})();
