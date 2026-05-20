# Design audit — steipete vs subkoks

## Profile page vs README repo

GitHub shows `username/username` README on the profile. Both users use that pattern (`steipete/steipete`, `subkoks/subkoks`).

## Side-by-side

| Aspect | steipete | subkoks (before) | subkoks (planned) |
|--------|----------|------------------|-------------------|
| Header | `# Hi, I'm Peter` + meta lines | Centered `# Blackterminal` | Left `# Blackterminal` + 2 lines |
| Top badges | Colorful `flat-square` | Dark flat shields | Colorful `flat-square` |
| Activity widget | `ghchart.rshah.org` heatmap | `github-readme-activity-graph` line | `ghchart.rshah.org/238636/subkoks` |
| Activity position | After huge project lists | Under hero (good position) | After badges (top fold) |
| Projects | Many categorized sections | Single “Currently building” | Start here + Currently building (small) |
| Stack | In badge row + prose | Separate Stack section | Grouped Stack & tools |
| Social proof | Stars, blog, media, talks | Followers badge, views | Minimal Connect + views |
| Extras | `<details>` blocks | None | Optional later |

## Widget URLs

**steipete heatmap:**

```text
https://ghchart.rshah.org/steipete
```

**subkoks heatmap (green):**

```text
https://ghchart.rshah.org/238636/subkoks
```

**Old subkoks line chart (remove from profile):**

```text
https://github-readme-activity-graph.vercel.app/graph?username=subkoks&bg_color=0d1117&...
```

## What not to copy

- 15+ project categories and 80+ links  
- Star counts on every line (you don’t have them yet)  
- Blog RSS Action block without a blog  
- Recognition / media sections without content  

## What to copy

- Badge color treatment  
- Heatmap-style GitHub Activity section title and placement (relative to your smaller content: higher than steipete’s)  
- “Start here” pattern with 3–4 anchors  
- Short “Focus” / “What I’m doing” prose  
