/**
 * Mojini AI — universal chat handler for the Mojini widget.
 *
 * The widget lives inline on ~20 pages, each with its own tiny canned
 * sendChatMessage()/sendMessage(). This script overrides those globals with a
 * single smart handler: it answers known questions instantly from the local FAQ
 * bank (window.mojiniAnswer, provided by js/faq-bank.js where present) and hands
 * everything else to the server-side LLM proxy at /api/mojini (Groq/Gemini/
 * DeepSeek — the API key stays on the server, never in the browser).
 *
 * Drop-in: <script src="/js/mojini-ai.js" defer></script>. Safe on pages with
 * no widget (it just never finds #chatInput).
 */
(function () {
  "use strict";
  if (window.__mojiniAI) return;
  window.__mojiniAI = true;

  function box() {
    return document.getElementById("chatMessages") || document.querySelector(".chat-messages");
  }
  function esc(s) {
    return String(s == null ? "" : s).replace(/[&<>"']/g, function (c) {
      return ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[c];
    });
  }
  // Escape, then make emails / http(s) links / root-relative .html paths clickable.
  function linkify(raw) {
    var s = esc(raw);
    s = s.replace(/([A-Za-z0-9._%+\-]+@[A-Za-z0-9.\-]+\.[A-Za-z]{2,})/g, '<a href="mailto:$1">$1</a>');
    s = s.replace(/(https?:\/\/[^\s<]+)/g, '<a href="$1" target="_blank" rel="noopener">$1</a>');
    try {
      s = s.replace(/(?<!["\w\/])(\/[A-Za-z0-9\-_\/]+\.html)\b/g, '<a href="$1">$1</a>');
    } catch (e) { /* older engines without lookbehind: leave paths as text */ }
    return s;
  }

  function renderUser(text) {
    var b = box(); if (!b) return;
    var wrap = document.createElement("div");
    wrap.className = "message user-message";
    var bub = document.createElement("div");
    bub.className = "user-bubble";
    bub.style.marginLeft = "auto";
    bub.textContent = text;
    wrap.appendChild(bub); b.appendChild(wrap); b.scrollTop = b.scrollHeight;
  }
  function renderBot(htmlSafe) {
    var b = box(); if (!b) return;
    // Prefer the page's own renderer if it accepts HTML; otherwise build our own.
    var wrap = document.createElement("div");
    wrap.className = "message bot-message";
    var bub = document.createElement("div");
    bub.className = "bot-bubble";
    bub.innerHTML = htmlSafe;
    wrap.appendChild(bub); b.appendChild(wrap); b.scrollTop = b.scrollHeight;
  }
  function showTyping() {
    var b = box(); if (!b) return null;
    var wrap = document.createElement("div");
    wrap.className = "message bot-message mojini-typing";
    var bub = document.createElement("div");
    bub.className = "bot-bubble";
    bub.setAttribute("aria-label", "Mojini is thinking");
    bub.innerHTML = '<span class="mojini-dots"><span>.</span><span>.</span><span>.</span></span>';
    wrap.appendChild(bub); b.appendChild(wrap); b.scrollTop = b.scrollHeight;
    return wrap;
  }

  async function askAI(text) {
    try {
      var r = await fetch("/api/mojini", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: text, page: location.pathname }),
      });
      if (!r.ok) return null;
      var d = await r.json();
      return d && typeof d.answer === "string" && d.answer.trim() ? d.answer.trim() : null;
    } catch (e) { return null; }
  }

  var FALLBACK =
    "I'm not certain about that one. The catalog (/catalog.html) and the search cover almost everything on ImpactMojo — or email hello@impactmojo.in and a human will help.";

  function handleSend() {
    var inp = document.getElementById("chatInput");
    if (!inp) return;
    var text = (inp.value || "").trim();
    if (!text) return;

    renderUser(text);
    inp.value = "";

    // 1) Instant answer from the local FAQ bank (js/faq-bank.js), if loaded.
    if (typeof window.mojiniAnswer === "function") {
      try {
        var a = window.mojiniAnswer(text);
        if (a) { renderBot(linkify(a)); return; }
      } catch (e) { /* fall through to AI */ }
    }

    // 2) Otherwise ask the AI (server-side key), with a graceful fallback.
    var typing = showTyping();
    askAI(text).then(function (ans) {
      if (typing && typing.remove) typing.remove();
      renderBot(linkify(ans || FALLBACK));
    }).catch(function () {
      if (typing && typing.remove) typing.remove();
      renderBot(linkify(FALLBACK));
    });
  }

  function injectStyle() {
    if (document.getElementById("mojini-ai-style")) return;
    var st = document.createElement("style");
    st.id = "mojini-ai-style";
    st.textContent =
      ".mojini-dots span{display:inline-block;animation:mojiniBlink 1.2s infinite both;font-weight:700}" +
      ".mojini-dots span:nth-child(2){animation-delay:.2s}" +
      ".mojini-dots span:nth-child(3){animation-delay:.4s}" +
      "@keyframes mojiniBlink{0%,80%,100%{opacity:.2}40%{opacity:1}}";
    document.head.appendChild(st);
  }

  function install() {
    if (!document.getElementById("chatInput")) return; // no widget on this page
    injectStyle();
    // Override the per-page handlers (both names are used across the site).
    window.sendChatMessage = handleSend;
    window.sendMessage = handleSend;
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", install);
  } else {
    install();
  }
})();
