# Project Rules — subkoks

## Project Overview

- **Name:** subkoks (GitHub Profile README)
- **Type:** GitHub profile repository — no application runtime
- **Repo:** github.com/subkoks/subkoks
- **Owner:** @subkoks (subkoks@gmail.com)
- **License:** MIT (Copyright 2026 blackterminal)
- **Status:** Active — dark minimal professional theme

## Repository Structure

```
subkoks/
├── README.md                  # GitHub profile page (primary deliverable)
├── CLAUDE.md                  # AI assistant instructions (this file)
├── LICENSE                    # MIT
├── .gitignore                 # OS/editor artifacts only
├── .claude/
│   └── settings.json          # Claude Code project config
├── .cursor/
│   └── BUGBOT.md              # Cursor bugbot review rules
└── .github/
    ├── CODEOWNERS             # @subkoks owns everything
    ├── dependabot.yml         # Weekly github-actions updates
    └── workflows/
        ├── claude.yml         # Claude Code AI agent on issues/PRs
        ├── pr-check.yml       # Sanity gate (enables auto-merge)
        └── auto-merge.yml     # Squash-merge same-repo PRs automatically
```

## README Conventions

The README.md is the **only user-visible output**. Follow these rules strictly:

### Aesthetic
- Dark minimal professional — no decorative clutter or heavy emoji usage
- Content must be concise; every line earns its place
- No walls of text; prefer badges, short bullets, and terse section headers

### Badge Row
- Single consolidated row at the top
- Badges sorted by hue gradient (warm → cool)
- Use `shields.io` flat-style badges with `logo=` parameter for icons
- SVG logos embedded as base64 where shields.io lacks an official logo (e.g., Codex)
- Current stack represented: Git, Claude, JavaScript, Linux, Bash, Node.js, Windsurf, TypeScript, Python, Solana, Codex, macOS, Cursor, CLI, Zsh (and others)

### Sections
1. **Tagline** — one-liner describing current focus area
2. **Badge row** — tech stack / tools
3. **Activity graph** — `ghchart.rshah009.com` contribution graph (dark theme)
4. **Currently building** — active projects with short descriptions
5. **Connect** — X and GitHub profile badges
6. **Profile view counter** — `komarev.com` visitor counter

### URLs and External Services
- GitHub activity graph: `https://ghchart.rshah009.com/subkoks`
- Profile view counter: `https://komarev.com/ghpvc/`
- Shields badges: `https://img.shields.io/badge/`
- Do not introduce new third-party services without checking for renderer compatibility

## Development Workflow

### Branching
- Feature branches use descriptive names or `claude/` prefix for AI-generated branches
- Never push directly to `main`
- All changes go through pull requests

### Commit Style
- Follow **Conventional Commits**: `type(scope): message`
- Common types: `docs`, `style`, `fix`, `ci`, `chore`
- Common scopes: `profile`, `readme`, `deps`, `claude`
- Examples:
  - `docs(profile): add new project to currently building section`
  - `style(profile): sort badges by hue gradient`
  - `ci(deps): bump anthropics/claude-code-action`

### Pull Requests
- PRs targeting `main` from same-repo branches are **auto-merged** once `pr-check` passes
- External forks are never auto-merged (write token safety)
- Squash merge strategy — keeps history clean
- CODEOWNERS: @subkoks reviews everything

## CI/CD Workflows

### `pr-check.yml` — Sanity Gate
- Runs on every PR to `main`
- Checks: Python syntax (`py_compile`), shell syntax (`bash -n`), JSON validity (`python -m json.tool`)
- **Lenient by design** — only fails on real breakage, not style
- Required status check; must pass for auto-merge to trigger

### `auto-merge.yml` — Automatic Merging
- Triggers after `pr-check` succeeds
- Skips external forks (checks `github.event.pull_request.head.repo.fork`)
- Uses `GITHUB_TOKEN` with squash merge
- Applies to Dependabot PRs and owner/collaborator branches

### `claude.yml` — Claude Code Agent
- Triggered by: issue comments, issue assignments, PR reviews, PR comments mentioning `@claude`
- Auth gate: only repository members/collaborators/owner can trigger
- Uses `CLAUDE_CODE_OAUTH_TOKEN` (Claude Pro/Max subscription)
- Permissions: `contents:write`, `pull-requests:write`, `issues:write`, `actions:read`
- Max turns: 15
- Runs `claude-code-action` with the `code-review` plugin

### `dependabot.yml` — Dependency Updates
- Ecosystem: `github-actions` only (no app dependencies to track)
- Schedule: weekly on Monday
- Groups minor/patch updates to reduce PR noise
- Keeps SHA-pinned actions in `claude.yml` current

## Key Conventions for AI Assistants

1. **This repo is README-only** — there is no application to run, no tests to execute, no build step. Changes are markdown and CI config.

2. **Do not add application structure** — no `src/`, `package.json`, test suites, or build pipelines unless explicitly requested.

3. **Preserve the dark minimal aesthetic** — when editing README.md, remove as much as you add. No new decorative elements without a clear reason.

4. **Badge changes require consistency** — if adding/removing a badge, maintain the hue-sorted order and flat style.

5. **Broken URLs are blocking** — verify any new external URLs actually resolve. Cache-busting params on badge URLs matter for renderer freshness.

6. **No secrets in README** — the profile is fully public. Never include tokens, keys, wallet addresses, or private project details.

7. **CI is intentionally lenient** — do not tighten `pr-check.yml` linting unless asked. The goal is "don't break rendering," not style enforcement.

8. **Commit on the designated branch** — always develop on the branch specified in session instructions and open a draft PR after pushing.

9. **Auto-merge is active** — PRs from same-repo branches will merge automatically once `pr-check` passes. Do not merge manually unless there is a specific reason.

10. **CODEOWNERS is `@subkoks`** — do not modify CODEOWNERS without explicit instruction.
