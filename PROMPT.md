# Cursor prompt — Apply subkoks profile redesign

Copy everything below the line into Cursor when implementing on `subkoks/subkoks` (or use draft in `GitHub-Profile/profile/README.md`).

---

```text
You are redesigning my GitHub profile README for repo `subkoks/subkoks`.

Reference:
- Inspiration layout: https://github.com/steipete/steipete/blob/main/README.md
- Design plan: GitHub-Profile/PLAN.md
- Draft: GitHub-Profile/profile/README.md

Goals:
- Visual style similar to steipete: colorful flat-square badge strip, contribution heatmap (not line chart), focused sections, dark-theme friendly.
- Put GitHub Activity (heatmap) high on the page — directly under the headline badge strip.
- Replace the current `github-readme-activity-graph` line/area chart on the main profile with ghchart:
  https://ghchart.rshah.org/238636/subkoks
- Keep content truthful; only public repos and real links. No fake stars or filler projects.

Constraints:
- Edit README.md only (profile repo root), unless asked to sync about-me.
- Markdown only; minimal HTML (no big centered div wrappers unless needed).
- No scripts, no GitHub Actions, no animated SVGs.
- Do not invent repos. Public repos: subkoks, about-me, agents-md, BEST-Self-Enhancement-Learning-AI.

Section order (exact):
1. Title + 2-line intro (left-aligned like steipete, not a heavy centered hero)
2. Headline badge strip — flat-square, full brand colors (Python, TS, Node, Solana, Bash, macOS, Linux, Git)
3. ## GitHub Activity — ghchart embed wrapped in <picture> for dark/light; HTML comment with fallback URL
4. ## Currently building — 3–4 bullets with emoji, repo name linked, 1–2 lines each (merged "Start here")
5. ## Stack & tools — grouped: Languages & runtimes | Platforms | Tools
6. ## Now — 3 status bullets (replaces redundant "Focus")
7. ## Connect — X + GitHub badges; HTML comment for future blog/site; komarev view counter at bottom

Fixes required:
- Remove old activity graph URL (github-readme-activity-graph) from profile README.
- Fix or remove "MASTER PLAN: Quit Your Job With Solana" bullet until a repo URL exists.
- Do not list apple-all-schematic unless the repo is public.
- Use accent color #238636 consistently (ghchart, view counter).
- Badge logos: use `logo=cursor` (not visualstudiocode), `logo=zsh` (not gnubash), `logo=anthropic` for Claude. Drop duplicate `CLI` badge (already covered by Bash).

Steps:
1. Read current subkoks/subkoks/README.md and GitHub-Profile/profile/README.md.
2. Merge best of draft into live README (or replace if draft is approved).
3. Run GitHub-Profile/scripts/deploy-check.sh if PROFILE_REPO_PATH is set.
4. Show final README.md as output and list what changed in 5 bullets.

Optional follow-up (only if asked):
- Sync subkoks/about-me to use the same ghchart embed.
- Update GitHub profile bio to match the new one-liner.
```
