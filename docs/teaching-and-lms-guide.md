# Teaching with ImpactMojo: LMS Export, Submissions & Gradebook

This guide is for the person running a course. It covers the three pieces that let you teach ImpactMojo material inside your own institution: packaging a course for your LMS, collecting student work from the Studios, and turning that work into a gradebook.

All three run **entirely in your browser**. Nothing you package and no student file you open is uploaded to us.

---

## 1. Put a course in your LMS

**[/lms-export](https://www.impactmojo.in/lms-export)**

Pick any of the 71 courses (or one of the 47 practice workbooks), choose a format, and download a package.

| Format | Use it when |
|--------|-------------|
| **SCORM 1.2** | The safest default. Every LMS built in the last twenty years imports it — Moodle, Canvas, Blackboard, TalentLMS, most corporate systems. |
| **SCORM 2004 (4th Ed.)** | Your LMS specifically asks for it, or you need finer sequencing data. |
| **IMS Common Cartridge 1.3** | Canvas and Moodle both take it, and it survives moving between systems better than SCORM. |
| **Single HTML file** | No LMS at all. One file you can email, put on a USB stick, or host anywhere. Works offline. |

### What is actually in the package

The export fetches the **live course page** at the moment you click, so a package is never a stale copy of something we generated months ago. It then does two things worth knowing about:

- **It strips our code.** Analytics, sign-in, the Supabase client, translation, the site chrome, the service worker — none of that belongs running inside your students' LMS session, so it is removed before packaging. If you unzip a package and search it for `gtag(` or `supabase`, you will find nothing.
- **It inlines everything else.** Styles, scripts and images are embedded, so the imported course needs no connection to impactmojo.in and keeps working if we ever move a file.

### Completion reporting

SCORM packages report completion **once, when the learner reaches the final slide**, hooked to the deck's own navigation. They do not mark a student complete on opening the course, and they do not fire a status update on every slide change.

### Known limits

- **xAPI is not offered.** xAPI needs a Learning Record Store to post statements to, and we do not run one. If your institution has an LRS and you want statements, tell us what endpoint you would point at.
- **One SCO per course.** The whole course is a single unit. You can already deep-link a specific slide with `#s42`, but a per-section SCO — so an LMS shows twelve trackable sections instead of one course — is not built yet.

---

## 2. Collect student work from the Studios

The [Interactive Studios](labs-guide.md) let students build something — a theory of change, a logframe, a sampling design — and export it. Historically that export carried **no identity at all**: a student clicked "export JSON" and got a file describing the artefact and nothing about who made it. Thirty students meant thirty anonymous files.

`js/studio-submit.js` fixes that. Where a Studio has adopted it, a **Submit for grading** button appears next to the existing export. It asks the student once for their name, an ID and a course code, remembers them, and wraps the Studio's own export in an envelope:

```json
{
  "impactmojo_submission": 1,
  "studio": "logframe-builder",
  "studio_title": "LogFrame Builder Studio",
  "student_name": "…",
  "student_id": "…",
  "course": "…",
  "submitted_at": "2026-08-21T09:14:22.104Z",
  "payload_type": "json",
  "payload": { "…the student's actual work…" },
  "digest": "…"
}
```

The `digest` is computed over the payload. It is not security — a determined student can regenerate it — but it does catch the ordinary case of a file edited after export, and the gradebook flags any mismatch.

**Adoption so far**: the **LogFrame Builder** Studio is wired up as the reference implementation. The remaining Studios take the same two lines:

```html
<script src="/js/studio-submit.js"></script>
```

```js
IMStudioSubmit.addButton({
  after: '#btnExportJson',
  studio: 'logframe-builder',
  studioTitle: 'LogFrame Builder Studio',
  getPayload: function () { return state; }
});
```

---

## 3. Turn submissions into a gradebook

**[/gradebook](https://www.impactmojo.in/gradebook)**

Drag a folder of submission files onto the page. You get one table and one CSV.

- Each row is one submission: student name, ID, course, Studio, timestamp, and a summary of what they built.
- Files whose digest does not match their payload are **flagged**, not silently accepted.
- Files that are not ImpactMojo submissions are skipped with a reason, so a stray PDF in the folder does not break the run.
- The CSV is written with a UTF-8 byte-order mark, so Excel renders Indian names correctly instead of turning them into mojibake.

Nothing leaves the browser. There is no upload, no account, and no request to our servers while you are grading.

---

## 4. Linking to a specific slide

Every slide in every deck has a stable `id`, and the fragment navigates. So a syllabus can say:

```
Week 4 reading: https://www.impactmojo.in/101-courses/mel-basics.html#s42
```

and that link will still land on the right slide next term. What is **not** yet published is a section-to-slide map, so today you have to open the deck and find the number yourself. That map, and the per-section SCO that would follow from it, are on the [roadmap](roadmap.md).

---

## Licensing

Course material is **CC BY-NC-ND 4.0**. You may use it in teaching, distribute it to your students, and import it into your institution's LMS. Credit ImpactMojo, keep it non-commercial, and do not redistribute modified versions. If you want to adapt or translate something for a specific context, write to [hello@impactmojo.in](mailto:hello@impactmojo.in) — we would rather help you do it well than have a bad copy circulate.

## Related

- [Teach with ImpactMojo](https://www.impactmojo.in/teach) — syllabus mappings and ready-made course kits
- [Labs Guide](labs-guide.md) — what each of the 35 Studios does
- [101 Course Decks Guide](101-decks-guide.md) — the foundational decks
- [Workshops & Facilitation](workshops-and-facilitation.md) — running the material live
