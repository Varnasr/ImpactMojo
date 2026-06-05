# ImpactMojo

Free development education platform for South Asia. Static HTML/CSS/JS, Supabase backend, Netlify hosting.

## Commands

```
# No build step — static site, auto-deploys on push to main via Netlify
# Tests: open HTML files directly in browser
```

## Architecture

- **Site**: impactmojo.in
- **Games**: Self-contained HTML in `/Games/` (single file, no deps)
- **Labs**: Browser-based in `/Labs/*-lab.html`
- **Courses**: 15 flagship (`/courses/{name}/`), 45 foundational (catalog)
- **Handouts**: 400+ in `/Handouts/{Track}/`
- **Data**: JSON in `/data/` (search-index, dataverse, BCT repository)
- **Docs**: GitBook in `/docs/`
- **NotebookLM**: 11 AI Study Companion notebooks managed via `notebooklm-py`. Registry: `data/notebooklm-registry.json`. Script: `scripts/notebooklm-manage.py`

## Conventions

- Games: single self-contained HTML (inline CSS + JS, Indian folk art illustrations)
- Forms use Netlify Forms (`data-netlify="true"` with `netlify-honeypot="bot-field"`)
- Content counts hardcoded in multiple places — grep before updating

## Watch out for

- `index.html` is ~620KB — backup to `Backups/` before major changes
- Content counts in nav, hero, cards, sidebar — update ALL occurrences
- Stale `101.impactmojo.in` links — should point to self-hosted files
- `data/search-index.json` must stay valid JSON
- Update `docs/changelog.md` for user-facing changes

## API Keys

`$GITHUB_PAT` · `$SUPABASE_PAT` · `$NETLIFY_PAT` · `$GAMMA_API_KEY` · `$GEMINI_API_KEY` · `$NAPKIN_API_KEY` · `$GROK_API_KEY` · `$DEEPSEEK_API_KEY` · `$SARVAM_API_KEY`

See `.claude/rules/api-conventions.md` for endpoints and auth patterns.

## Memory

Persistent project context lives in `.claude/memory.md` — carries state, decisions, and session logs across Claude Code sessions. Use `/memory` to read, update, or query it.

## .claude/ Structure

- **memory.md** — persistent context across sessions (project state, decisions, known issues, session log)
- **rules/** — modular instructions (code-style, content-management, api-conventions, testing)
- **commands/** — `/project:review`, `/project:fix-issue`, `/project:deploy-check`, `/project:audit`, `/project:add-game`
- **skills/** — auto-invoked workflows (add-files, housekeeping, github-ops, netlify-ops, supabase-ops, gamma-ops, gemini-ai, grok-ai, deepseek-ai, sarvam-ai, napkin-ai, threads-writer, blog-writer, dojo-ops, book-summaries, memory, frontend-design, seo, deep-research, debugging, tufte-viz)
- **agents/** — subagent personas (code-reviewer, content-auditor)
- **hooks/** — session-start (API key bootstrap), pre-tool-use (destructive command guard), stop (memory sync prompt)

## References (not loaded by default — saves tokens)

- **Community resources** (skills, MCP servers, repos): `.claude/references.md`
- **Claude Code best practices** (vendored guides): `.claude/vendor/claude-code-synthesis/` — sync with `/project:sync-guides`
- **Open-source AI catalog**: [alvinunreal/awesome-opensource-ai](https://github.com/alvinunreal/awesome-opensource-ai) — curated models, frameworks, tools & infrastructure (14 categories)
