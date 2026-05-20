# Deploy checklist — profile README

## Prerequisites

- GitHub repo: [subkoks/subkoks](https://github.com/subkoks/subkoks)  
- Local clone (example): `Projects/Current/Active/subkoks`

## Publish

1. Copy draft:
   ```bash
   cp profile/README.md /path/to/subkoks/README.md
   ```
2. Preview diff:
   ```bash
   git -C /path/to/subkoks diff README.md
   ```
3. Commit (when you want):
   ```bash
   git -C /path/to/subkoks add README.md
   git commit -m "docs(profile): steipete-style layout with ghchart heatmap"
   git push origin main
   ```
4. Open https://github.com/subkoks — hard refresh if images look cached.

## Sync about-me

```bash
# Use same ghchart block in about-me/README.md under ## Coding activity
git -C /path/to/about-me add README.md && git commit -m "docs: align activity graph with profile"
```

## GitHub UI (manual)

- **Settings → Profile:** bio matches README intro  
- **Pinned repositories:** agents-md, BEST-Self-Enhancement-Learning-AI, about-me (pick 3–6)  
- **Social accounts:** X @Subkoks  

## Rollback

Restore previous README from git:

```bash
git -C /path/to/subkoks checkout HEAD~1 -- README.md
```
