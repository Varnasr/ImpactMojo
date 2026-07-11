/* Field Radio — a community station for ImpactMojo PLC voice notes & shorts.
   Streams clips back-to-back (auto-advance), supports audio (cassette + waveform)
   and video (vertical short frame), tag filtering, and a transcript caption panel.
   Driven by /data/field-radio.json. No external dependencies. */
(function () {
  "use strict";

  var TRACK_COLORS = {
    "MEL & Research": "#3182ce",
    "Data & Technology": "#38a169",
    "Policy & Economics": "#d69e2e",
    "Gender & Equity": "#d53f8c",
    "Health & Communication": "#e53e3e",
    "Philosophy & Governance": "#805ad5"
  };

  var els = {};
  var clips = [];       // filtered, ordered list currently in the station
  var allClips = [];    // full list from manifest
  var idx = 0;          // current index into clips[]
  var media = null;     // the active <audio>/<video> element
  var playing = false;
  var activeTrack = "all";

  function $(id) { return document.getElementById(id); }
  function esc(s) { return String(s == null ? "" : s).replace(/[&<>"]/g, function (c) {
    return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }

  function trackColor(t) { return TRACK_COLORS[t] || "#0EA5E9"; }

  function boot() {
    els.stage = $("fr-stage");
    els.nowTitle = $("fr-now-title");
    els.nowMeta = $("fr-now-meta");
    els.ticker = $("fr-ticker");
    els.playBtn = $("fr-play");
    els.prevBtn = $("fr-prev");
    els.nextBtn = $("fr-next");
    els.eq = $("fr-eq");
    els.transcript = $("fr-transcript");
    els.list = $("fr-list");
    els.filters = $("fr-filters");
    els.dial = $("fr-dial");

    els.playBtn.addEventListener("click", toggle);
    els.prevBtn.addEventListener("click", function () { jump(idx - 1); });
    els.nextBtn.addEventListener("click", function () { jump(idx + 1); });

    fetch("/data/field-radio.json", { cache: "no-cache" })
      .then(function (r) { return r.json(); })
      .then(function (data) {
        var st = (data && data.station) || {};
        if (st.name) { var h = $("fr-station-name"); if (h) h.textContent = st.name; }
        if (st.tagline) { var t = $("fr-station-tagline"); if (t) t.textContent = st.tagline; }
        allClips = (data && Array.isArray(data.clips)) ? data.clips : [];
        renderFilters();
        applyFilter("all");
      })
      .catch(function () {
        els.stage.innerHTML = '<p class="fr-empty">Field Radio is warming up. Check back shortly.</p>';
      });
  }

  function renderFilters() {
    var tracks = [];
    allClips.forEach(function (c) { if (c.track && tracks.indexOf(c.track) < 0) tracks.push(c.track); });
    var html = '<button class="fr-chip is-on" data-track="all">All voices</button>';
    tracks.forEach(function (t) {
      html += '<button class="fr-chip" data-track="' + esc(t) + '" style="--chip:' + trackColor(t) + '">' + esc(t) + "</button>";
    });
    els.filters.innerHTML = html;
    els.filters.querySelectorAll(".fr-chip").forEach(function (b) {
      b.addEventListener("click", function () { applyFilter(b.getAttribute("data-track")); });
    });
  }

  function applyFilter(track) {
    activeTrack = track;
    els.filters.querySelectorAll(".fr-chip").forEach(function (b) {
      b.classList.toggle("is-on", b.getAttribute("data-track") === track);
    });
    clips = (track === "all") ? allClips.slice() : allClips.filter(function (c) { return c.track === track; });
    stop();
    idx = 0;
    renderList();
    if (clips.length) { load(0, false); } else {
      els.stage.innerHTML = '<p class="fr-empty">No voices on this frequency yet.</p>';
      els.nowTitle.textContent = "—";
      els.nowMeta.textContent = "";
      els.transcript.innerHTML = "";
    }
  }

  function renderList() {
    if (!clips.length) { els.list.innerHTML = ""; return; }
    var html = "";
    clips.forEach(function (c, i) {
      var icon = c.type === "video" ? "▶" : "♪";
      html += '<button class="fr-item" data-i="' + i + '">' +
        '<span class="fr-item-ic" style="--tc:' + trackColor(c.track) + '">' + icon + "</span>" +
        '<span class="fr-item-b">' +
          '<span class="fr-item-t">' + esc(c.title || "Untitled") + (c.sample ? ' <span class="fr-tag-sample">sample</span>' : "") + "</span>" +
          '<span class="fr-item-m">' + esc(c.speaker || "") + (c.track ? ' &middot; <span style="color:' + trackColor(c.track) + '">' + esc(c.track) + "</span>" : "") + "</span>" +
        "</span>" +
        '<span class="fr-item-d">' + esc(c.duration || "") + "</span>" +
      "</button>";
    });
    els.list.innerHTML = html;
    els.list.querySelectorAll(".fr-item").forEach(function (b) {
      b.addEventListener("click", function () { jump(parseInt(b.getAttribute("data-i"), 10)); });
    });
  }

  function markActive() {
    els.list.querySelectorAll(".fr-item").forEach(function (b, i) {
      b.classList.toggle("is-playing", i === idx);
    });
  }

  function stop() {
    if (media) {
      try { media.pause(); } catch (e) {}
      // detach our listeners before clearing src — an empty src fires a spurious
      // 'error' that would otherwise un-hide the next stage's "coming soon" box.
      media.removeEventListener("error", onMediaError);
      media.removeAttribute("src");
      media = null;
    }
    playing = false;
    if (els.eq) els.eq.classList.remove("is-on");
    if (els.dial) els.dial.classList.remove("is-spinning");
    setPlayIcon(false);
  }

  function setPlayIcon(isPlaying) {
    els.playBtn.innerHTML = isPlaying
      ? '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="6" y="5" width="4" height="14" rx="1"/><rect x="14" y="5" width="4" height="14" rx="1"/></svg>'
      : '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg>';
    els.playBtn.setAttribute("aria-label", isPlaying ? "Pause" : "Play");
  }

  function load(i, autoplay) {
    idx = ((i % clips.length) + clips.length) % clips.length;
    var c = clips[idx];
    var col = trackColor(c.track);

    // now-playing header
    els.nowTitle.textContent = c.title || "Untitled";
    els.nowMeta.innerHTML = (c.speaker ? '<b>' + esc(c.speaker) + "</b>" : "") +
      (c.role ? ' &middot; ' + esc(c.role) : "") +
      (c.track ? ' &middot; <span class="fr-track-dot" style="background:' + col + '"></span>' + esc(c.track) : "");
    els.ticker.textContent = c.title || "";
    els.transcript.innerHTML = c.transcript
      ? '<h3>Transcript</h3><p>' + esc(c.transcript) + "</p>"
      : '<p class="fr-no-tr">No transcript for this clip yet.</p>';

    // build the stage (cassette for audio, vertical frame for video)
    if (c.type === "video") {
      els.stage.innerHTML =
        '<div class="fr-video-frame">' +
          '<video id="fr-media" playsinline preload="metadata" ' +
            (c.poster ? 'poster="' + esc(c.poster) + '" ' : "") +
            'src="' + esc(c.src) + '"></video>' +
          '<div class="fr-media-err" hidden>Short coming soon</div>' +
        "</div>";
    } else {
      els.stage.innerHTML =
        '<div class="fr-cassette" style="--tc:' + col + '">' +
          '<div class="fr-reel"></div><div class="fr-reel"></div>' +
          '<div class="fr-cassette-label">' + esc(c.speaker || "Voice note") + "</div>" +
          '<audio id="fr-media" preload="metadata" src="' + esc(c.src) + '"></audio>' +
          '<div class="fr-media-err" hidden>Audio coming soon</div>' +
        "</div>";
    }

    media = $("fr-media");
    media.addEventListener("ended", function () { jump(idx + 1); });
    media.addEventListener("error", onMediaError);
    media.addEventListener("play", function () { onPlayState(true); });
    media.addEventListener("pause", function () { onPlayState(false); });

    markActive();
    document.documentElement.style.setProperty("--fr-accent", col);

    if (autoplay) { play(); }
  }

  function onMediaError(e) {
    if (e && e.target !== media) return; // ignore stale errors from a swapped-out clip
    var box = els.stage.querySelector(".fr-media-err");
    if (box) box.hidden = false;
    onPlayState(false);
  }

  function onPlayState(isPlaying) {
    playing = isPlaying;
    setPlayIcon(isPlaying);
    if (els.eq) els.eq.classList.toggle("is-on", isPlaying);
    if (els.dial) els.dial.classList.toggle("is-spinning", isPlaying);
    var cas = els.stage.querySelector(".fr-cassette");
    if (cas) cas.classList.toggle("is-playing", isPlaying);
  }

  function play() {
    if (!media) return;
    var p = media.play();
    if (p && p.catch) p.catch(function () { /* autoplay blocked or media missing */ });
  }

  function toggle() {
    if (!media) { if (clips.length) load(idx, true); return; }
    if (playing) { media.pause(); } else { play(); }
  }

  function jump(i) {
    if (!clips.length) return;
    var wasPlaying = playing || true; // station keeps rolling
    stop();
    load(i, wasPlaying);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", boot);
  } else { boot(); }
})();
