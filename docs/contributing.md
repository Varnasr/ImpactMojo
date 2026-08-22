# Contributing to ImpactMojo

Thank you for your interest in contributing! ImpactMojo is built by and for the development community. Whether you're a practitioner who spotted an outdated statistic, an educator with a great case study, or a developer who can fix a bug — there's a meaningful way for you to contribute.

**Found a bug?** Check [Known Issues](https://www.impactmojo.in/known-issues.html) first — it reads live from this repository's issue tracker, so if we already know, it is listed there with what we know so far. If it is not listed, open an issue and label it `bug`; that is what puts it on the page. If you do not use GitHub, the same page has a form.

## You Don't Need to Be Technical

Many of our most valuable contributions come from practitioners, not programmers. Here's how you can help without writing a single line of code:

| What you can do | How | Difficulty |
|-----------------|-----|------------|
| **Report an error** | Found a broken link, wrong statistic, or outdated reference? Open a [Content Issue](https://github.com/ImpactMojo/ImpactMojo/issues/new?template=content_issue.md) | Very easy |
| **Suggest a topic** | Know a topic that should be covered? Start a [Discussion](https://github.com/ImpactMojo/ImpactMojo/discussions/categories/ideas) | Very easy |
| **Share a case study** | Have a real-world development case study from your work? Email us at hello@impactmojo.in | Easy |
| **Translate content** | Help make courses available in Hindi, Tamil, Bengali, Telugu, or Marathi | Easy–Medium |
| **Review content** | Are you an expert in MEL, gender studies, or development economics? Help us review courses for accuracy | Easy |
| **Write a handout** | Create a reference sheet on a topic you know well | Medium |

## For Technical Contributors

If you're comfortable with HTML, CSS, or JavaScript, there are plenty of ways to contribute:

| Area | Examples | Difficulty |
|------|----------|------------|
| **Bug fixes** | Broken links, layout issues, JavaScript errors | Easy–Medium |
| **Accessibility** | WCAG compliance, screen reader support, keyboard navigation | Medium |
| **Design** | UI/UX improvements, mobile experience | Medium |
| **Tools & Labs** | Build or improve interactive learning tools | Hard |
| **Games** | New economics simulations | Medium–Hard |

### Getting Started (Technical)

ImpactMojo is a vanilla HTML/CSS/JS project — no frameworks, no build step. You can run it locally with just a web browser and a simple server:

```bash
# 1. Fork and clone the repository
git clone https://github.com/<your-username>/ImpactMojo.git
cd ImpactMojo

# 2. Start a local server (pick whichever you have)
python -m http.server 8000
# or: npx http-server -p 8080

# 3. Open http://localhost:8000 in your browser

# 4. Create a branch for your changes
git checkout -b feature/your-feature-name

# 5. Make your changes, test locally

# 6. Commit using the prefix convention
git commit -m "Add: descriptive summary of what you did"

# 7. Push and open a Pull Request on GitHub
git push origin feature/your-feature-name
```

### Commit Message Convention

Every commit message starts with a prefix that describes the type of change:

| Prefix | When to use it | Example |
|--------|---------------|---------|
| `Add:` | New feature, course, or tool | `Add: interactive budget planning lab` |
| `Fix:` | Bug fix or broken link | `Fix: broken nav dropdown on mobile Safari` |
| `Update:` | Improvement to existing content or code | `Update: MEL course module 3 with 2025 data` |
| `Translate:` | Translation work | `Translate: gender studies course to Hindi` |
| `Docs:` | Documentation changes | `Docs: add workshop facilitation guide` |
| `Refactor:` | Code restructuring (no behaviour change) | `Refactor: extract auth logic to separate file` |
| `Test:` | Adding or updating tests | `Test: add accessibility checks for games` |
| `CI:` | CI/CD pipeline changes | `CI: add broken link checker workflow` |
| `Chore:` | Maintenance (dependencies, configs) | `Chore: update dependabot config` |

### Pull Request Guidelines

- Keep PRs focused — one feature or fix per PR
- Test on desktop and mobile
- Include screenshots for visual changes
- Note if changes affect premium features

## Content Writing Style

If you're contributing educational content, here's what we aim for:

- **Tone:** Accessible but rigorous. Write for a practitioner with 2–3 years of experience.
- **Examples:** Prefer South Asian context (India, Bangladesh, Nepal, Sri Lanka).
- **Jargon:** Define terms on first use. If it's a common sector term, add it to [ImpactLex](https://www.impactmojo.in/impactlex/).
- **Attribution:** Always cite sources. Link to [DevDiscourses](https://www.impactmojo.in/dataverse) where possible.
- **Accessibility:** Use clear headings, alt text for images, and sufficient colour contrast.

## Reporting Issues

Use [GitHub Issues](https://github.com/ImpactMojo/ImpactMojo/issues) with the appropriate template:

- **Bug Report** — something is broken (link, layout, error)
- **Feature Request** — a new idea or improvement
- **Content Issue** — factual error, outdated information, missing topic

## Community Channels

- [WhatsApp PLC](https://forms.gle/vJaHFd7QcMe4JVF19) — Peer discussions among practitioners
- [Discord](https://discord.gg/M3ZCmUe7ab) — Technical discussions and tinkering
- [Telegram](https://t.me/impactmojo) — Free resources and updates
- [GitHub Discussions](https://github.com/ImpactMojo/ImpactMojo/discussions) — Ideas, Q&A, and announcements
- **Email:** hello@impactmojo.in — For anything else
