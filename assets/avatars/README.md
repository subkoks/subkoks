# Profile avatar — options

All 1024×1024 PNG, ready to upload to GitHub. Four direction sets (A = sigil, B = CRT face, C = noir portrait, D = research-informed new directions).

## Sigil set (A — brutalist mark)

| File | Mark | Notes |
|------|------|-------|
| `avatar-option-a-sigil.png` | `>/` brush-stroke sigil + green dot | Original. Reads as both a slash and a chevron. |
| `avatar-option-a2-prompt.png` | Chunky `>_` prompt + green dot | Most literal "Blackterminal" mark. Bold at any size. |
| `avatar-option-a3-slash.png` | Single diagonal slash + green dot | Maximum minimalism. Most expensive-looking. |
| `avatar-option-a4-block.png` | Solid cursor block (vertical bar) + green dot | Most literal "blinking cursor" evocation. Reads massive at small size. |
| `avatar-option-a5-stroke.png` | Zen horizontal brush stroke + green dot | Most artisanal / gallery-art aesthetic. |
| `avatar-option-a6-wedge.png` | Asymmetric wedge / cursor arrow + green dot | Reads as a mouse cursor, play button, or paper plane. Most dynamic. |

## CRT face set (B — cyberpunk face)

| File | Variant | Notes |
|------|---------|-------|
| `avatar-option-b-crt-face.png` | Straight-on, light scanlines, subtle green aberration | Original. Calm cyberpunk. |
| `avatar-option-b2-three-quarter.png` | Three-quarter angle, low-poly wireframe + green RGB split | Most sculptural / 3D-feeling. |
| `avatar-option-b3-heavy-glitch.png` | Full RGB chromatic split (green + magenta), dense scanlines | Most aggressive cyberpunk. |

## Noir portrait set (C — editorial character)

| File | Variant | Notes |
|------|---------|-------|
| `avatar-option-c-noir-portrait.png` | Side-glance + purple rim light | Original. Most "moody". |
| `avatar-option-c2-front-green.png` | Straight-on direct gaze + green rim light | On-brand green accent. Most "presence" / direct. |
| `avatar-option-c3-silhouette.png` | Side-profile silhouette + purple contour light | Most dramatic / mysterious. Heavy negative space. |

## D — new directions (informed by what top devs actually use)

Sampled 18 top dev profiles (karpathy, antfu, shadcn, yetone, sindresorhus, t3dotgg, simonw, ggerganov, midudev, mxstbr, defunkt, adamwathan, pi0, danielroe, armaniferrante, okjodom, rasbt, steipete). Dominant pattern: **branded photo (~65%)** or **stylized portrait (~25%)**. Pure abstract sigils are essentially absent on individual dev profiles.

| File | Direction | Reference | Notes |
|------|-----------|-----------|-------|
| `avatar-option-d1-branded-photo.png` | Branded studio photo (green backdrop) | t3dotgg (purple), midudev (blue), sindresorhus | Generic stock-feeling face — not a real photo of you. Risky unless treated as a brand stand-in. |
| `avatar-option-d2-hooded-terminal.png` | Minimalist hooded figure + green terminal slit eye | okjodom (cyberpunk) | **Most on-brand for "Blackterminal".** Editorial flat illustration, not anime. Literally embodies the name. |
| `avatar-option-d3-mascot.png` | Original cat mascot, single CRT green eye | Octocat, Tux — mascot strategy | Memorable, ownable, scales to merch/site. Loses "senior dev" signal in exchange for brand recall. |
| `avatar-option-d4-editorial-warm.png` | Editorial illustrated portrait, green backdrop | antfu, yetone, armaniferrante, shadcn | Pattern-matched safe bet. Painterly, not anime. Closest to proven popular formula. |

## How to set on GitHub

1. Open https://github.com/settings/profile
2. Click **Edit picture** on the current avatar
3. **Upload a photo** → pick a file from `GitHub-Profile/assets/avatars/`
4. Crop preview is a circle; all three are designed to read cleanly inside a circle.
5. Save changes.

## Source files

The pre-crop 1536×1024 originals live in this workspace under
`~/.cursor/projects/Users-black-terminal-Projects-Current-Active/assets/`.
The 1024×1024 squares in this folder are center-cropped via `sips`.

## Iterate

If none of these land, the next round can explore: pixel-art portrait, isometric terminal render, ASCII-art portrait, animated APNG terminal cursor, or a wordmark-based mark with custom typography.
