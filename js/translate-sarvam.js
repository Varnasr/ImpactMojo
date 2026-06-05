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
        'html[data-imlang="bn"] body *:not(svg):not([class*="icon"]):not(.material-icons){font-family:"Noto Sans Bengali",sans-serif!important}';
      document.head.appendChild(st);
    }
  }

  function cacheGet(lang, s) { try { return localStorage.getItem("xlate:" + lang + ":" + s); } catch (e) { return null; } }
  function cacheSet(lang, s, t) { try { localStorage.setItem("xlate:" + lang + ":" + s, t); } catch (e) {} }

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
    document.documentElement.setAttribute("data-imlang", lang);
    document.documentElement.setAttribute("lang", lang);
    // unique source strings
    var uniq = {}, order = [];
    for (var i = 0; i < originals.length; i++) {
      var s = originals[i].text.trim();
      if (!(s in uniq)) { uniq[s] = cacheGet(lang, s); if (uniq[s] == null) order.push(s); }
    }
    applyTranslations(uniq);                 // apply cached strings instantly
    // fetch + apply each batch progressively (don't wait for the whole page)
    for (var i = 0; i < order.length; i += 12) {
      if (curLang !== lang) break;           // user switched away — stop
      var fetched = await apiBatch(lang, order.slice(i, i + 12));
      // accept only real translations (skip the function's failure fallback)
      for (var k in fetched) {
        if (fetched[k] && fetched[k] !== k) { uniq[k] = fetched[k]; cacheSet(lang, k, fetched[k]); }
      }
      applyTranslations(uniq);
    }
    save(lang); markActive(lang); busy = false; markBusy(false);
    // one delayed pass to catch content added by deferred scripts (auth bar, etc.)
    if (!isRepass) setTimeout(function () { if (curLang === lang) translateTo(lang, true); }, 3000);
  }

  function save(lang) { try { localStorage.setItem(KEY_LS, lang); } catch (e) {} }

  // ---- UI ----
  var bar;
  function markActive(lang) {
    if (!bar) return;
    [].forEach.call(bar.querySelectorAll("button"), function (b) {
      b.style.background = b.dataset.l === lang ? "rgba(29,78,216,0.9)" : "transparent";
      b.style.color = b.dataset.l === lang ? "#fff" : "#475569";
    });
  }
  function markBusy(on) {
    if (!bar) return;
    bar.style.opacity = on ? "0.85" : "1";
    var s = document.getElementById("im-xlate-status");
    if (s) { s.style.display = on ? "inline-block" : "none"; }
  }
  function buildUI() {
    bar = document.createElement("div");
    bar.id = "im-lang-switch"; bar.setAttribute("data-no-translate", "");
    bar.setAttribute("aria-label", "Language");
    bar.style.cssText = "position:fixed;bottom:14px;left:14px;z-index:99998;display:flex;gap:2px;" +
      "background:#ffffff;backdrop-filter:blur(8px);border:1px solid rgba(0,0,0,0.1);" +
      "border-radius:999px;padding:3px;box-shadow:0 4px 14px rgba(0,0,0,0.15);font-family:system-ui,sans-serif";
    Object.keys(LANGS).forEach(function (code) {
      var b = document.createElement("button");
      b.textContent = LANGS[code].label; b.dataset.l = code;
      b.title = LANGS[code].native;
      b.style.cssText = "border:none;cursor:pointer;font-size:12px;font-weight:600;padding:5px 9px;border-radius:999px;background:transparent;color:#475569";
      b.addEventListener("click", function () { translateTo(code); });
      bar.appendChild(b);
    });
    var status = document.createElement("span");
    status.id = "im-xlate-status"; status.textContent = "translating…";
    status.style.cssText = "display:none;align-self:center;font-size:11px;font-weight:600;color:#1D4ED8;padding:0 8px 0 4px;animation:imXlatePulse 1s ease-in-out infinite";
    bar.appendChild(status);
    var kf = document.createElement("style");
    kf.textContent = "@keyframes imXlatePulse{0%,100%{opacity:.45}50%{opacity:1}}";
    document.head.appendChild(kf);
    document.body.appendChild(bar);
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
