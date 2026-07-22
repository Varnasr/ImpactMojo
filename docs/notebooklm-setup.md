# NotebookLM Setup

Programmatic management of ImpactMojo's 12 AI Study Companion notebooks using [notebooklm-py](https://github.com/teng-lin/notebooklm-py).

## Installation

```bash
pip install -r requirements.txt
playwright install chromium
```

## Authentication

One-time setup — opens a browser for Google OAuth:

```bash
notebooklm login
```

Use the Google account that owns the 11 course notebooks. Credentials are stored locally and never committed.

Verify with:

```bash
notebooklm status
```

## Usage

### Management script

```bash
# Check auth status
python3 scripts/notebooklm-manage.py status

# List all notebooks with registry cross-reference
python3 scripts/notebooklm-manage.py list

# Sync registry titles from live API
python3 scripts/notebooklm-manage.py sync-registry

# Add a reading/URL to a course notebook
python3 scripts/notebooklm-manage.py add-source devecon https://example.com/paper.pdf

# Generate audio overview for a course
python3 scripts/notebooklm-manage.py generate-audio gandhi
```

### CLI (notebooklm-py built-in)

```bash
notebooklm list                          # List all notebooks
notebooklm sources list <notebook-id>    # List sources in a notebook
notebooklm ask <notebook-id> "question"  # Ask a question
notebooklm audio <notebook-id>           # Generate audio overview
```

## Registry

`data/notebooklm-registry.json` maps course slugs to notebook IDs. This is the single source of truth for automation — notebook IDs are also embedded in course HTML pages but the registry is what scripts read.

## Course notebooks

| Slug | Course |
|------|--------|
| sel | Social and Emotional Learning 101 |
| dataviz | Data Visualization 101 |
| devai | Development & AI 101 |
| devecon | Development Economics 101 |
| gandhi | Gandhi & Nonviolence 101 |
| gender | Gender & Equity 101 |
| law | Law & Justice 101 |
| media | Media & Information 101 |
| mel | MEAL 101 |
| poa | Policy & Advocacy 101 |
| pubpol | Public Policy 101 |

## Limitations

- **Unofficial API** — uses undocumented Google APIs that may break without notice
- **Interactive auth** — `notebooklm login` requires a browser, cannot run in CI/headless
- **Per-machine credentials** — auth tokens are stored locally, not in the repo
- **Rate limits** — Google may throttle requests; avoid rapid-fire operations

## Study-companion kit (prompts + source packs)

Reusable prompts and cited-readings lists for every flagship live in `notebooklm/` (built by `scripts/notebooklm-build-pack.py`). See `notebooklm/README.md`. Full source packs are generated locally and git-ignored (course content is DB-backed / anti-fork).
