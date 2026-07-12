# Field Radio Guide

## What Is Field Radio?

Field Radio is a **community station of voice notes and short videos** from development practitioners across South Asia. It is not a podcast: there are no numbered episodes, no seasons, and nothing to subscribe to. You press play and listen in — short, unpolished dispatches from the field.

Field Radio is **free, browser-based, and requires no login**. Every clip streams on the page and carries a full transcript, so it is readable as well as listenable.

### How Field Radio Differs from the Podcast

- **The Podcast** ([Between the Logframes](podcast-guide.md)) is a produced, long-form show — structured conversations, edited, released as episodes.
- **Field Radio** is the opposite: raw, minute-long voices from practitioners — a reflection after a hard field day, a tip that saved a survey, a question someone is still sitting with. One voice, one moment, no production.

If you want a deep conversation, use the podcast. If you want to hear the sector thinking out loud, tune in to Field Radio.

---

## What's on the Station

Field Radio currently carries **15 clips** — a mix of voice notes and short videos — from practitioners across ImpactMojo's thematic tracks. Each clip lists:

- **Speaker and role** — who is talking and what they do.
- **Track** — the thematic area (MEL, gender, data, facilitation, and so on).
- **Type** — voice note or short video.
- **Duration and date.**
- **Transcript** — the full text of the clip, for accessibility and for readers who prefer to skim.

Browse the station at [/field-radio.html](/field-radio.html).

---

## How Clips Are Organised

Field Radio is deliberately un-structured to listen to — you can just press play and let it run — but under the hood every clip is tagged by **track** and **type** so the station can be filtered. There is no algorithm and no ranking: clips are surfaced by track and recency, not by popularity.

The station data lives in `data/field-radio.json`; each entry has an `id`, `type`, `title`, `speaker`, `role`, `track`, `src`, `duration`, `date`, and `transcript`.

---

## Contributing a Clip

Field Radio is a community station — practitioners are invited to send in their own voice notes and short videos. If you have a reflection, a field tip, or an honest question from your work, you can contribute:

- Keep it short (roughly 30 seconds to two minutes).
- Say who you are and what track it belongs to.
- Record it however you can — a phone voice note is perfect.

See [How to Contribute](contributing.md) or write to `hello@impactmojo.in` to get a clip on the station.

---

## Accessibility

Every clip ships with a **full transcript**, so Field Radio works whether you listen or read. Audio and video use native browser controls (play/pause, seek, volume) and are keyboard-operable. There is no autoplay.

---

## Related

- [Podcast Guide](podcast-guide.md) — the produced long-form show.
- [Reading Companions Guide](book-summaries-guide.md) — interactive companions to key texts.
- [How to Contribute](contributing.md) — how community members add content.
