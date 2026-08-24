# The Development Law Docket

Indian judgments that changed what development organisations, state programmes
and rights-holders can actually do.

Data: `data/judgments.json`. Guard: `scripts/check-judgments.py` (CI job
`judgments`). Guide sections: `scripts/build-law-guide-cases.py`.

## What this is, and what it is not

It is orientation. It is **not** legal advice, and it must never read as advice.
Holdings are summarised editorially; the linked judgment is authoritative.

That distinction is not a disclaimer to satisfy a lawyer. NGO staff will act on
what this page says, and the failure mode is specific: a case summary is exactly
the kind of text a language model produces fluently and wrongly, and a wrong
holding looks identical to a right one. Everything below exists to make that
failure visible instead of invisible.

## The two things that must be true of every entry

**It is sourced.** Every entry links to the judgment. `verified` records the
date, the source checked against, and the specific things checked — the case
name, the decision year, and named terms confirmed present in the judgment text.

**Its status is stated.** `status` is mandatory and constrained:

| status | means |
|---|---|
| `good-law` | stands, applied as decided |
| `codified` | Parliament enacted it; the statute now governs |
| `modified` | a later bench narrowed or reworked it |
| `partly-overruled` | part no longer holds |
| `overruled` | no longer good law |
| `under-reference` | pending before a larger bench |

There is deliberately **no `unknown`**. "Nobody checked" is not something this
file may say silently. Anything other than `good-law` must carry a
`status_note` explaining the qualification, and the guard enforces it.

This matters more than it sounds. Unni Krishnan was substantially reworked by
T.M.A. Pai. Section 66A was struck down in Shreya Singhal and is still used to
book people. Common Cause's living-will procedure was simplified in 2023
because the original was unworkable. An entry that omits this reads
authoritative and is worse than no entry.

## How the current set was built

Sixty candidate cases were resolved against Indian Kanoon, filtered on case
name and decision year, then re-checked: each entry declares terms that must
appear in the judgment text, and an entry whose terms are absent is dropped
rather than published.

Six were dropped, and they are listed in `meta.excluded` on the page itself —
because a docket that shows only what it found looks more complete than it is.
One drop is worth keeping in mind: a search for *Consumer Education & Research
Centre v. Union of India* matched **LIC v. CERC**, a different case, and the
name-and-year filter alone let it through. The term check is what caught it.

**What is verified is identity, not interpretation.** That a case exists, has
this name and this date, and contains these terms — checked. That the summary
correctly characterises what the case means — editorial. Do not describe this
dataset as verified case law.

## Adding an entry

1. Resolve the case and confirm name and year against the judgment text.
2. Write `holding` (what was decided) and `what_changed` (what a practitioner
   does differently). If you cannot write the second, the case may not belong.
3. Set `status`, and `status_note` if it is anything but `good-law`.
4. Tag `statutes` with the law-guide stem it belongs to, if any.
5. Run `python3 scripts/build-law-guide-cases.py`, then the guard.

## Coverage, stated plainly

Supreme Court of India only. High Court and tribunal decisions are not here,
and district and trial courts are absent from the underlying corpus entirely.

## Related

- `law-guides/development-law-docket.html` — the page
- `data/dataverse.json` — Open India Law, the corpus this draws on
- `.claude/rules/testing.md` — the other guards and what each exists because of
