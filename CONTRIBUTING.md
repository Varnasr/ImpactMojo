# Contributing to ImpactMojo

Thank you for your interest in contributing to ImpactMojo! Whether you're fixing a broken link, improving accessibility, translating content, or building a new tool, we appreciate every contribution.

## Ways to Contribute

- **Content**: Improve courses, add South Asian case studies, update examples, suggest readings
- **Translations**: Translate content into Hindi, Tamil, Bengali, Telugu, Marathi, or other South Asian languages
- **Accessibility**: WCAG compliance, screen reader improvements, keyboard navigation
- **Bug fixes**: Report or fix broken links, layout issues, or JavaScript errors
- **Design**: Improve UI/UX, mobile experience, dark mode, or responsive layouts
- **Tools & Labs**: Build or improve interactive learning tools

## Getting Started

1. **Fork** the repository on GitHub
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/ImpactMojo.git
   cd ImpactMojo
   ```
3. **Install dependencies** (this also activates git hooks):
   ```bash
   npm install
   ```
4. **Start a local server** (required for auth and routing):
   ```bash
   npm run serve
   # or: python -m http.server 8000
   ```
5. **Create a feature branch**:
   ```bash
   git checkout -b feature/your-feature-name
   ```
6. **Make your changes** and test locally
7. **Commit** with a clear message:
   ```bash
   git commit -m "Add: descriptive summary of your change"
   ```
8. **Push** and open a Pull Request

## Commit Message Style

Git hooks enforce commit message prefixes automatically. Use a short prefix to categorize your change:

- `Add:` — New feature, course, or tool
- `Fix:` — Bug fix or broken link
- `Update:` — Improvement to existing content or code
- `Refactor:` — Code restructuring (no behaviour change)
- `Translate:` — Translation work
- `Docs:` — Documentation changes
- `Test:` — Adding or updating tests
- `CI:` — CI/CD pipeline changes
- `Chore:` — Maintenance (deps, configs, tooling)

## Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR
- Include a brief description of what changed and why
- Test on both desktop and mobile views
- If your change affects premium features, note that in the PR description

## Code Style

This is a vanilla HTML/CSS/JS project. No build step required.

- Use semantic HTML where possible
- Keep CSS in `<style>` blocks within each page (existing pattern) or in external files under `css/`
- Use `const`/`let` over `var`
- Prefer readable code over clever code
- Remove `console.log`/`debugger` before committing (the pre-commit hook will warn)

## Git Hooks

After `npm install`, git hooks are automatically active:

- **pre-commit** — Blocks `.env`/credentials, catches `debugger` statements, detects merge conflict markers, warns on large files
- **commit-msg** — Rejects commits without a valid prefix (see above)

To bypass hooks in emergencies: `git commit --no-verify` (use sparingly)

## Reporting Issues

Use [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) to report:

- Broken links or pages
- Accessibility barriers
- Content errors or outdated information
- Feature requests

## Community

- **WhatsApp PLC**: [Request to join the Professional Learning Community](https://forms.gle/vJaHFd7QcMe4JVF19)
- **Discord**: [Join for tech discussions](https://discord.gg/M3ZCmUe7ab)
- **Telegram**: [Follow for free resources](https://t.me/impactmojo)
- **Email**: hello@impactmojo.in

## License

By contributing, you agree that your contributions will be licensed under the [CC-BY-4.0 License](LICENSE).
