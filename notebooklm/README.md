# NotebookLM AI Study Companion kit

Reusable prompts + source material to build a NotebookLM "AI Study Companion" for
every ImpactMojo flagship course. Generated from the live course content by
`scripts/notebooklm-build-pack.py`.

## What's here
- `prompts/<slug>.md` — a ready-to-use study-companion + audio-overview steering prompt, plus suggested seed questions, per flagship. **Committed.**
- `readings/<slug>.md` — the open-access readings cited across the course, as ready-to-run `add-source` commands. **Committed.**
- `packs/<slug>-source-pack.md` — the full course text (all modules) to upload to NotebookLM. **Git-ignored** — course content is DB-backed on purpose (anti-fork); regenerate locally when needed.

## Regenerate
```bash
set -a; . .claude/.env.keys; set +a          # needs SUPABASE_PAT
python3 scripts/notebooklm-build-pack.py                 # all flagships
python3 scripts/notebooklm-build-pack.py social-movements # one course
```

## Create a notebook for a course (per docs/notebooklm-setup.md)
1. `notebooklm login` (one-time Google OAuth, on your machine — not CI/sandbox).
2. Create the notebook in NotebookLM; upload `packs/<slug>-source-pack.md`.
3. Add the cited readings: run the `add-source` commands in `readings/<slug>.md`.
4. Paste the `prompts/<slug>.md` audio-overview steering prompt into NotebookLM's "Customise".
5. Register it: add `<slug>` → notebook-id to `data/notebooklm-registry.json`, put the share
   URL in the course shell's "AI Study Companion" button, then optionally
   `python3 scripts/notebooklm-manage.py generate-audio <slug>`.
