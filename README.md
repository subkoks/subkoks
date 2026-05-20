# GitHub-Profile

Workspace for redesigning [github.com/subkoks](https://github.com/subkoks) (profile README in `subkoks/subkoks`), inspired by [github.com/steipete](https://github.com/steipete).

## Quick start

```bash
cd GitHub-Profile   # or your chosen path after moving this folder
cp .env.example .env
open PLAN.md
```

| File | Purpose |
|------|---------|
| [PLAN.md](PLAN.md) | Full redesign plan (layout, widgets, phases) |
| [PROMPT.md](PROMPT.md) | Cursor-ready execution prompt |
| [profile/README.md](profile/README.md) | Draft profile README to copy into `subkoks/subkoks` |
| [docs/design-audit.md](docs/design-audit.md) | steipete vs subkoks visual breakdown |
| [docs/deploy.md](docs/deploy.md) | Publish checklist |

## Scripts

```bash
./scripts/preview-urls.sh    # widget preview URLs in terminal
./scripts/deploy-check.sh    # link + image smoke check on profile/README.md
```

## Movable install

This repo is path-independent. Move the whole `GitHub-Profile` folder anywhere; update `PROFILE_REPO_PATH` in `.env` if you use `deploy-check.sh` against a local clone of `subkoks/subkoks`.

## Related repos

- Live profile host: `subkoks/subkoks`
- Extended about page: `subkoks/about-me`
- Local clone (optional): `../subkoks` in Active workspace
