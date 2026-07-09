# How I Built a Global Claude Code Setup with 16 Skills, Safety Hooks, and a Self-Updating Knowledge Base

*A detailed walkthrough of the ~/.claude/ configuration that follows me into every project.*

---

Most developers using Claude Code treat each project as a blank slate. Every new repo means re-explaining your preferred API patterns, re-establishing safety rails, and re-building workflows you've already figured out.

I spent the last few months building a different approach. Everything reusable lives in `~/.claude/` — Claude Code's global configuration directory. When I open any project, 16 skills, 2 safety hooks, a persistent memory system, and current best practices are already loaded. The project just adds its own layer on top.

Here's the full breakdown.

---

## The Architecture: Global vs. Project-Specific

Claude Code reads configuration from two places:

1. **`~/.claude/`** — Global. Available in every project, every session.
2. **`.claude/`** — Project-scoped. Lives in the repo, checked into version control.

The rule I follow is simple: if a skill works in any repository, it goes global. If it references specific file paths, URLs, brand colours, or content structures, it stays project-scoped.

For ImpactMojo (my development education platform), the split looks like this:

- **Global (16 skills):** AI APIs, platform ops, content creation, research
- **Project-specific (8 skills):** Blog writing, brand guidelines, content auditing, book summaries, housekeeping — all tied to ImpactMojo's structure

This separation means I could start a completely unrelated project tomorrow and still have PDF generation, SEO audits, Supabase management, and five AI providers ready to go.

---

## The 16 Global Skills

### AI API Wrappers (4 skills)

Each of these knows the authentication pattern, available models, endpoint structure, and capabilities of its respective provider. I don't look up API docs anymore — I just say what I need.

**Gemini AI** — Google's Generative Language API. Auth via query parameter (`?key=$GEMINI_API_KEY`). I use this primarily for content generation and embeddings. The skill knows every model variant and parameter.

**Grok AI** — xAI's Grok-3 via an OpenAI-compatible endpoint. Bearer token auth. I find Grok particularly useful for opinionated first drafts and reasoning tasks where I want a different perspective from Claude's own output.

**DeepSeek AI** — DeepSeek-V3, also OpenAI-compatible. The cost-effective option. When I'm running batch operations — say, generating descriptions for 40 course entries — DeepSeek handles the volume without burning through credits.

**Sarvam AI** — This one's niche but critical for my work. Sarvam provides South Asian language processing: speech-to-text (Saaras), translation (Mayura), and text-to-speech (Bulbul) across Hindi, Tamil, Bengali, Telugu, Marathi, and more. Since ImpactMojo serves South Asia, having multilingual capabilities one command away is transformative.

### Platform Operations (5 skills)

These are the skills that turn Claude Code into a full infrastructure management layer.

**GitHub Ops** — Full GitHub API access. Create and merge PRs, manage issues, handle releases, label management, branch operations. The skill includes auto-labeling logic — it knows which labels to apply based on which files changed. I create, review, and merge PRs without leaving the terminal.

**Supabase Ops** — Database migrations, edge function deployment, auth management, storage operations — all through the Supabase Management API. Earlier today, I used it to create a new user, set their subscription tier, and send a password reset email. Three API calls, one natural language instruction.

**Netlify Ops** — Deployment management, DNS configuration, environment variables, build hooks. When I need to check why a deploy failed or update an environment variable, I don't log into the dashboard.

**Gamma Ops** — Gamma's API for AI-generated presentations. I use this to auto-generate course slide decks. The skill manages the full lifecycle: create, poll for completion, download, organise into folders.

**Napkin AI** — Converts text descriptions into visual infographics and diagrams. When I write a blog post, I describe the visual I want and Napkin generates it. Publication-ready napkin-style illustrations from a text prompt.

### Content Creation (5 skills)

**PDF Processing** — Read, extract, create, merge, split PDFs using pdfplumber, reportlab, and pypdf. I generate handout packs (84 handouts across multiple tracks), extract tables from research reports, and create course exports. The skill preserves layout during extraction and handles images, charts, and multi-column layouts.

**PPTX (PowerPoint)** — Programmatic slide generation via python-pptx. The skill has explicit anti-"AI slop" instructions — no bullet-heavy slides, no generic clip art. It uses branded colour schemes, stat slides, comparison layouts, and proper visual hierarchy. This complements Gamma for cases where I need precise control over every element.

**Frontend Design** — HTML/CSS generation following a defined design system (typography, colour palette, spacing, components). Every generated page meets WCAG AA accessibility standards and is mobile-responsive. The skill knows the difference between a game page, a lab tool, and a landing section — each has its own layout pattern.

**Web Artifacts Builder** — Self-contained interactive HTML tools. Calculators, dashboards, simulators, data explorers — each as a single HTML file with inline CSS and JavaScript, zero external dependencies. These run entirely in the browser with no build step. I've generated sample size calculators, cost-effectiveness simulators, and progress tracking tools this way.

**SEO** — A 12-capability SEO skill covering technical audits, meta tag optimization, JSON-LD structured data, Open Graph tags, Core Web Vitals, E-E-A-T content quality assessment, image optimization, sitemap management, and multilingual SEO. It also handles AI search optimization — making sure content is structured for LLM-based search engines, not just Google.

### Research & Memory (2 skills)

**Deep Research** — Multi-source research synthesis. Define a research question, and the skill coordinates across multiple AI providers and web sources to gather evidence, cross-validate claims, and compile findings. I use this before creating any new course or game — it builds the evidence base that makes the content credible.

**Memory** — Persistent context across sessions at two levels. Global memory (`~/.claude/memory.md`) stores my preferences and cross-project decisions. Project memory (`.claude/memory.md`) tracks the current state — what's been built, what's known broken, recent architectural decisions. Both auto-load at session start. I never have to re-explain context when I return to a project after days away.

---

## The Safety Layer: 2 Hooks That Prevent Disasters

Skills are about capability. Hooks are about guardrails.

### Hook 1: block-destructive.sh (PreToolUse)

This shell script intercepts every Bash command before it executes. It pattern-matches against a blocklist:

- `rm -rf` — No recursive force-deletes
- `git push --force` / `git push -f` — No force-pushes
- `git reset --hard` — No hard resets
- `git clean -f` — No force-cleans
- `DROP TABLE` — No table drops

If a match is found, it returns `{"decision": "block"}` and the command never runs. Simple, effective, and it's saved me more than once. The key insight: Claude Code is powerful enough that a single misunderstood instruction could wipe uncommitted work. This hook makes that impossible.

### Hook 2: session-start.sh (SessionStart)

This runs automatically when any Claude Code session begins. It reads API keys from a gitignored `.env.keys` file and injects them into the session environment. Nine keys are bootstrapped:

`GITHUB_PAT`, `SUPABASE_PAT`, `NETLIFY_PAT`, `GAMMA_API_KEY`, `GEMINI_API_KEY`, `NAPKIN_API_KEY`, `GROK_API_KEY`, `DEEPSEEK_API_KEY`, `SARVAM_API_KEY`

The keys never appear in committed files. The hook handles the plumbing so every skill has its credentials ready from the first command.

---

## The Permission Matrix

Beyond hooks, `settings.json` defines what Claude Code can and cannot do:

**Allowed:**
- All safe git operations (status, diff, log, branch, fetch, add, commit, push, checkout, merge, stash, show)
- `curl -s` for API calls
- File operations (Read, Write, Edit, Glob, Grep)
- Skill invocations

**Denied:**
- `rm -rf` (redundant with the hook, but defence in depth)
- Force-push and force-reset
- Reading `.env`, `.env.*`, or `.env.keys` files

This creates a sandbox where Claude Code can do ambitious work — create files, make API calls, manage git branches — without accessing secrets directly or running destructive operations.

---

## Self-Updating Best Practices: Vendored Guides

The most unusual part of my setup: I vendor external best-practice guides and keep them current with a single command.

I sync from Griffin Hilly's [claude-code-synthesis](https://github.com/griffinhilly/claude-code-synthesis) repository — an opinionated operating model for Claude Code that distils real-world patterns into actionable guides:

- **Delegation Templates** — 7 agent archetypes (Implementer, Researcher, Reviewer, Batch Worker, Session Reviewer, Explorer, Creative) with mandatory report formats
- **Context Efficiency** — Strategies for reducing token consumption and maximising the 100:1 input-to-output ratio
- **Shell Rules** — Command patterns that avoid security scanner false positives
- **Overnight Runner** — Long-running job orchestration with checkpoints and resume capability
- **Prefer APIs** — Decision hierarchy: API > library > static data > browser automation
- **Postgres Batching** — Database query patterns (CTEs, combined queries, permission handling)

These live in `~/.claude/vendor/claude-code-synthesis/` and are loaded on demand — they don't bloat every session's context window. When the upstream repo updates, I run `/sync-guides` and get the latest.

The sync script does a shallow clone to a temp directory, copies only the CLAUDE.md and guides/ (skipping examples), records the commit SHA and timestamp in a `.sync-meta` file, and cleans up. It runs in under 5 seconds.

---

## How It All Fits Together: A Real Example

Here's what happened in a single session today:

1. **Created a Supabase user** — Used the `supabase-ops` skill to retrieve the service role key via the Management API, created an auth user, updated her profile to the highest subscription tier, and sent a password reset email. Four API calls, one instruction.

2. **Set up guide syncing** — Built the sync script, created a slash command, vendored the guides, added permissions — all committed and merged via `github-ops`.

3. **Promoted configs to global** — Audited all 26 project skills, classified each as global or project-specific, and copied the 16 reusable ones to `~/.claude/`.

Throughout all of this, `block-destructive.sh` silently intercepted a force-push attempt (needed after a rebase) and made me take the safer path of creating a new branch instead. The system worked exactly as designed.

---

## Getting Started With Your Own Setup

You don't need 16 skills on day one. Start with:

1. **One safety hook.** Copy the `block-destructive.sh` pattern. It's a few lines of bash that prevent the worst mistakes.

2. **One API skill.** Pick the service you use most. Write a SKILL.md that documents the auth pattern, base URL, and common operations. Claude Code will use it automatically when relevant.

3. **The memory skill.** Persistent context across sessions is transformative. You stop re-explaining your project every time you start a new conversation.

4. **The session-start hook.** Centralise your API keys in one gitignored file. No more scattered credentials.

Then grow from there. Each skill you add compounds — they reference each other, they share conventions, and they make Claude Code progressively more capable in your specific workflow.

The `~/.claude/` directory is the most underleveraged feature of Claude Code. It turns a general-purpose AI assistant into your personal engineering team — one that remembers your preferences, knows your APIs, respects your safety boundaries, and gets better every session.

---

*I'm building ImpactMojo — a free development education platform for South Asia with 64 courses, 84 handouts, 134 interactive games, and 13 labs. The entire platform is a static HTML/CSS/JS site with a Supabase backend, deployed on Netlify. Claude Code with this global setup is how a solo developer ships at this scale.*
