# How defects get recorded

Every defect worth telling readers about gets a filed issue, before it gets a fix.

Enforced by `scripts/check-fix-issues.py` (CI job `fix-issues`).

## Why this file exists

On 2026-08-22 the public [Known Issues](https://www.impactmojo.in/known-issues.html)
page was found showing nothing at all. The page was working exactly as designed:
it reads bug-labelled issues live from GitHub, and in the entire history of this
repository, three had ever been filed.

The changelog, meanwhile, carried **92 `### Fixed` entries**. Ninety-two real
defects — a five-column grid class that was never declared, twenty-one pages
silently outside the asset-stamping guard, callout boxes rendering with no
colour on eleven courses, a resource card pointing at a 404 — every one of them
found, fixed, written up for readers, and recorded nowhere a reader could search.

Nothing had failed. The workflow was find-it-and-fix-it-in-the-same-commit,
which is fast and leaves no trace. **A page that can only show what the workflow
files will show nothing, forever, without ever going red.** That is the failure
mode this file exists to close: not a bug, but an absence that looks identical
to "nothing is broken".

## The rule

> If a fix is worth a line in the release notes, it is worth a filed issue.

That is the whole rule, and the guard checks exactly it — no more. In particular
it does **not** require an issue per commit (noise), and it does **not** read git
history (squash-merges rewrite commit messages, so the record would not survive).

## The sequence

1. **File first.** Open an issue, label it `bug`, describe what is wrong and how
   you found it. It appears on the public page immediately — which is the point:
   a reader hitting the same defect can see that it is known.
2. **Fix it.** Reference the issue number in the commit.
3. **Close it** with `state_reason: completed` once the fix is on `main`. Do not
   close it while the fix is only on a branch — the page would then say it is
   fixed when production still has the defect.
4. **Cite it in the changelog** under `### Fixed`, as `(#NNN)`.

Step 4 is the one CI checks, because it is the one that survives every other
process change.

## What belongs on the page, and what does not

| | Goes to |
|---|---|
| A defect: something behaving other than as intended | A `bug` issue → this page |
| The site is down or degraded right now | System Status |
| Something missing that was never built | The roadmap |
| A security vulnerability | Contact privately — **never** a public issue |
| Content that is wrong rather than broken | A `bug` issue, labelled `content` too |

## The two guards

**`scripts/check-fix-issues.py`** — every `### Fixed` bullet in a release dated
2026-08-23 or later must cite `#NNN`. Releases before that date are
grandfathered, because they are the backlog that prompted this. The cutoff is a
fixed date rather than a moving window, so the exemption can only ever cover
less.

**`scripts/build-fix-history.py`** — derives `data/fix-history.json` from the
changelog's Fixed sections, and `--check` fails when the two drift apart.

## Why the backlog was not backfilled as issues

The obvious move was to file the 92 historical defects as issues and close them,
so the page had content. It was rejected.

The page prints "Fixed N days ago" from the issue's `closed_at`. Ninety-two
issues closed in one afternoon would every one of them read **"Fixed today"** —
including defects fixed in April. A page built specifically so we could not
overstate what we know would have begun by overstating when we knew it.

The changelog already holds the true date: the release the fix shipped in. So
the history is derived from there and rendered as a separate, explicitly-dated
section, with the page saying in as many words that those dates come from
release notes rather than from the tracker.

The general lesson is worth keeping: **a record with a fabricated timestamp is
worse than no record**, because it is indistinguishable from a real one.

## Related

- `known-issues.html` — the public page
- `.claude/rules/content-management.md` — where this sits in the release checklist
- `.claude/rules/testing.md` — the other guards and what each exists because of
