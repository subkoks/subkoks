# CLAUDE.md — GitHub-Profile

Workspace for redesigning the [@subkoks](https://github.com/subkoks) GitHub
profile (steipete-inspired). **Not the live profile** — the published README
lives at `subkoks/subkoks`; this repo drafts and validates it, then you copy
`profile/README.md` over.

**Documentation/tooling only — no application runtime.** Path-independent: the
whole folder can be moved anywhere.

## Layout

| Path | Purpose |
|------|---------|
| `profile/README.md` | Draft profile README to copy into `subkoks/subkoks` |
| `PLAN.md` | Full redesign plan (layout, widgets, phases) |
| `PROMPT.md` | Cursor-ready execution prompt |
| `docs/design-audit.md` | steipete vs subkoks visual breakdown |
| `docs/deploy.md` | Publish checklist |
| `assets/avatars/` | Image assets |
| `scripts/` | `preview-urls.sh`, `deploy-check.sh`, `cloud-setup.sh` |

## Commands

```bash
cp .env.example .env          # set PROFILE_REPO_PATH for deploy-check
./scripts/preview-urls.sh     # print widget preview URLs in terminal
./scripts/deploy-check.sh     # link + image smoke check on profile/README.md
```

`PROFILE_REPO_PATH` (in `.env`) points `deploy-check.sh` at a local clone of
`subkoks/subkoks`. `.env` is gitignored — never commit it.

## Conventions

- Markdown-first; keep every widget/badge/image URL valid (run `deploy-check.sh`).
- Edit the draft in `profile/README.md`; publishing = copy to `subkoks/subkoks`, not push from here.
- One logical change per commit; `type(scope): description`; feature branches only.

## Related

- `subkoks/subkoks` — live profile host (publish target).
- `subkoks/about-me` — extended about page.
