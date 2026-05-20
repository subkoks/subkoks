# GitHub profile redesign plan — subkoks → steipete-style

**Target:** [github.com/subkoks](https://github.com/subkoks)  
**Inspiration:** [github.com/steipete](https://github.com/steipete)  
**Publish target:** [subkoks/subkoks](https://github.com/subkoks/subkoks) README  
**Draft source:** [profile/README.md](profile/README.md)

---

## 1. What you have today

| Element | Current | Issue |
|---------|---------|-------|
| Hero | Centered `# Blackterminal` + tagline | Good; steipete uses left-aligned, lighter header |
| Activity | `github-readme-activity-graph` **line/area chart**, title “Coding activity (Last 12 Months)” | Not the heatmap steipete uses; feels like a different widget |
| Badges | Dark flat shields (`labelColor=0d1117`) | Low contrast vs steipete’s **brand-colored flat-square** tiles |
| Projects | 5 bullets, one without link (“MASTER PLAN…”) | Broken UX; only **4 public repos** on GitHub |
| Stack | Single flat row | No grouping (Languages / Platforms / Tools) |
| Footer | X, GitHub, view counter | Fine; steipete adds more socials (you can stay minimal) |

**Public repos (2026-05-20):** `subkoks`, `about-me`, `agents-md`, `BEST-Self-Enhancement-Learning-AI`.  
`apple-all-schematic` is referenced locally but not in public API — pin only when public.

---

## 2. What steipete actually does (inspect summary)

From [steipete/steipete README](https://github.com/steipete/steipete/blob/main/README.md):

1. **Short identity block** — name, location, role (no huge centered banner).
2. **Colorful badge strip** — `style=flat-square` with full logo colors (Swift orange, TS blue, etc.).
3. **“Start Here”** — 6–7 flagship links with emoji + star counts (you scale to **3–4**).
4. **Large categorized project lists** — skip 90% of this; you don’t have 171 repos.
5. **## GitHub Activity** — contribution **heatmap**, not line chart:
   ```md
   ![GitHub Contribution Graph](https://ghchart.rshah.org/steipete)
   ```
6. **“What I’m Doing”** — 4 short bullets (mindset / focus).
7. **Blog RSS block** — optional automation (defer unless you have a blog).
8. **Connect** — social badges row.
9. **Collapsible `<details>`** — extras (Recognition, Media) — optional for you later.

**Key insight:** The graph you liked on steipete’s profile is almost certainly **ghchart** (calendar grid), not `github-readme-activity-graph` (commits-over-time line).

---

## 3. Recommended layout for subkoks (honest, steipete-like)

Order optimized for “graph on top” without losing identity:

```
┌─────────────────────────────────────────┐
│ # Blackterminal                         │
│ One-liner + location/focus (1–2 lines)  │
├─────────────────────────────────────────┤
│ [Colorful flat-square badge strip]      │  ← steipete-style tools row
├─────────────────────────────────────────┤
│ ## GitHub Activity                      │
│ [ghchart heatmap — green #238636]       │  ← TOP visual (replaces line chart)
├─────────────────────────────────────────┤
│ ## Start here                           │  ← 3–4 real repos only
├─────────────────────────────────────────┤
│ ## Currently building                   │  ← same repos, 1-line each
├─────────────────────────────────────────┤
│ ## Stack & tools                        │  ← grouped flat-square badges
├─────────────────────────────────────────┤
│ ## Focus                                │  ← short keyword line (keep yours)
├─────────────────────────────────────────┤
│ ## Connect                              │  ← X, GitHub, optional site
│ [profile views counter]                 │
└─────────────────────────────────────────┘
```

**Do not add** fake star counts, blog automation, or 20 project sections until repos exist.

---

## 4. Activity graph decision

| Option | URL pattern | Look | Verdict |
|--------|-------------|------|---------|
| **A. ghchart (steipete)** | `https://ghchart.rshah.org/238636/subkoks` | Contribution calendar, green shades | **Recommended primary** |
| B. github-readme-activity-graph | `...vercel.app/graph?username=subkoks&theme=github-dark&area=true` | Line/area, “last 12 months” | Keep only in `about-me` if you want both |
| C. Both | ghchart on profile; line chart on about-me | Richer but redundant | Optional |

**Action:** Remove line chart from main profile; use ghchart with your existing brand green `238636`.  
Sync [subkoks/about-me](https://github.com/subkoks/about-me) to the same heatmap OR document why about-me keeps the line chart.

---

## 5. Badge system (steipete-like colors)

**Row 1 — headline strip** (above activity): `flat-square`, full brand colors, no dark `labelColor` hack.

Include only what you actually use:

- Python, TypeScript, JavaScript, Node.js  
- Solana  
- Bash/Zsh, CLI  
- macOS, Linux  
- Cursor / VS Code (optional), Git  

**Row 2 — Stack & tools** (below projects): same style, grouped headings:

- **Languages & runtimes**  
- **Platforms**  
- **Tools** (Cursor, Claude, Git, etc.)

Avoid `for-the-badge` on the main strip unless you want a louder, “marketing” look; steipete uses flat-square.

---

## 6. Content inventory (truthful)

| Repo | Role on profile |
|------|-----------------|
| [agents-md](https://github.com/subkoks/agents-md) | Flagship — cross-editor GOTCHA rules + Solana pack |
| [BEST-Self-Enhancement-Learning-AI](https://github.com/subkoks/BEST-Self-Enhancement-Learning-AI) | Flagship — BSELA control plane |
| [about-me](https://github.com/subkoks/about-me) | Secondary — extended about (not profile host) |
| [subkoks](https://github.com/subkoks/subkoks) | Meta — this README repo |

**Defer / fix:**

- **MASTER PLAN: Quit Your Job With Solana** — no public repo; use plain text or create repo before linking.  
- **apple-all-schematic** — add when public; until then omit or “private WIP”.  
- **hacker-agent**, **stake-dice-graph** — local Active workspace; add when pushed public.

**GitHub profile bio** (Settings → Profile): align with README one-liner; set website when `black.terminal` is live.

---

## 7. Visual theme tokens

| Token | Value | Use |
|-------|-------|-----|
| Page bg | `#0d1117` | Matches GitHub dark |
| Accent | `#238636` | ghchart base, links, view counter |
| Text | `#c9d1d9` | Implied via GitHub |
| Badge style | `flat-square` + logo | steipete parity |

---

## 8. Implementation phases

### Phase 0 — Workspace (done in this folder)

- [x] `GitHub-Profile` repo with plan, prompt, draft README, scripts  
- [ ] Optional: `git remote add origin` → new `subkoks/GitHub-Profile` or keep local-only

### Phase 1 — Draft & preview (1 session)

1. Review [profile/README.md](profile/README.md).  
2. Run `./scripts/preview-urls.sh` and open URLs in browser.  
3. Tweak ghchart color / badge list.  
4. Run `./scripts/deploy-check.sh`.

### Phase 2 — Publish profile (1 commit)

1. Copy `profile/README.md` → `subkoks/subkoks/README.md` (or PR from this repo).  
2. Push `main` on `subkoks/subkoks`.  
3. Verify on [github.com/subkoks](https://github.com/subkoks) (cache may take ~1 min).

### Phase 3 — Align about-me

1. Update `about-me` README: same ghchart embed + link back to profile.  
2. Remove duplicate/conflicting graph widgets.

### Phase 4 — GitHub settings (manual)

- [ ] Profile picture / banner (optional)  
- [ ] Pinned repos: `agents-md`, `BEST-Self-Enhancement-Learning-AI`, `agents-md` or `about-me` (max 6)  
- [ ] Bio, location, X handle consistency (`@Subkoks`)

### Phase 5 — Optional polish (later)

- Custom PNG badges (Figma → R2/img.shields) for 1:1 steipete tile look  
- `github-readme-stats` card (minimal: top langs only) — **below** heatmap, not above  
- Blog post list via GitHub Action (only if you have RSS)  
- `<details>` for media / recognition when you have links

---

## 9. Perplexity ideas — adopted vs skipped

| Idea | Decision |
|------|----------|
| Hero → badges → activity → projects → stack → links | **Adopted** (section order) |
| github-readme-activity-graph at top | **Modified** — use **ghchart** at top for steipete parity; line chart optional on about-me |
| for-the-badge headline row | **Skipped** — flat-square matches steipete closer |
| 3–6 “Currently building” | **Adopted** — capped at real public repos |
| No fake stats | **Adopted** |
| Custom Figma badges | **Phase 5** |

---

## 10. Success criteria

- [ ] First screen: identity + **heatmap** + colorful stack (no scroll for graph).  
- [ ] No broken project links.  
- [ ] Reads clean on mobile (badges wrap; graph scales).  
- [ ] Dark mode: no white boxes around chart.  
- [ ] `about-me` and profile don’t fight each other visually.

---

## 11. Risks & mitigations

| Risk | Mitigation |
|------|------------|
| ghchart third-party down | Fallback link to github.com/subkoks; document alt URL in PLAN |
| External images blocked | All HTTPS; avoid mixed content |
| Too empty vs steipete | Quality over quantity; strong copy on 3–4 projects |
| Widget overload | Max 2 dynamic widgets on profile (heatmap + view counter) |

---

## 12. Next action

1. Read draft: [profile/README.md](profile/README.md).  
2. Run Cursor with [PROMPT.md](PROMPT.md) when ready to apply to `subkoks/subkoks`.  
3. Say when to publish — copy draft → live repo and push.
