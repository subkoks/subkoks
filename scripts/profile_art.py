#!/usr/bin/env python3
"""Generate the profile's monospace SVG furniture.

Two kinds of static artwork, both in the same palette as `assets/activity.svg`
(orange accent on neutral gray, transparent background so they read correctly in
light and dark mode):

* `assets/tagline.svg` — the two-line mono intro under the title.
* `assets/labels/<slug>.svg` — uppercase micro-labels used inside `<h2>` tags.

The text is static, so these are generated once and committed. Re-run after
editing `LABELS` or `TAGLINE`:

    python3 scripts/profile_art.py
"""

from __future__ import annotations

import pathlib
from xml.sax.saxutils import escape

MONO = 'ui-monospace, SFMono-Regular, Menlo, Consolas, "Liberation Mono", monospace'
ACCENT = "#FF7F0E"
INK = "#969696"
DIM = "#7a7a7a"

# slug -> uppercase label text. Labels live in one place and are referenced by
# both READMEs (about-me uses absolute raw URLs to this repo).
LABELS = {
    "github-activity": "GITHUB ACTIVITY",
    "currently-building": "CURRENTLY BUILDING",
    "projects": "PROJECTS",
    "connect": "CONNECT",
    "coding-activity": "CODING ACTIVITY",
    "what-im-building": "WHAT I'M BUILDING",
    "focus": "FOCUS",
    "links": "LINKS",
    "codex-cli": "CODEX CLI",
}

TAGLINE = (
    "Building AI coding agent infrastructure, developer tools, and Solana automation.",
    "Web3, local automation, practical scripts — deep in vibe-coding mode.",
)

LABEL_HEIGHT = 24


def mono_width(text: str, size: float, spacing: float) -> float:
    """Approximate width of monospace text (advance ~0.6em plus tracking)."""
    return len(text) * (size * 0.6 + spacing)


def label_svg(text: str) -> str:
    size, spacing = 12.5, 1.6
    text_x = 21.0
    baseline = 17.0
    # The trailing rule is left to the surrounding <h2>, which draws a
    # full-width hairline under the label.
    width = round(text_x + mono_width(text, size, spacing) + 8)
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}"'
            f' height="{LABEL_HEIGHT}" viewBox="0 0 {width} {LABEL_HEIGHT}"'
            f' role="img" aria-label="{escape(text)}"'
            f' font-family=\'{MONO}\'>',
            f"<title>{escape(text)}</title>",
            f'<circle cx="8" cy="12" r="3.2" fill="{ACCENT}"/>',
            f'<text x="{text_x:g}" y="{baseline:g}" fill="{INK}" font-size="{size:g}"'
            f' letter-spacing="{spacing:g}">{escape(text)}</text>',
            "</svg>",
        ]
    ) + "\n"


def tagline_svg() -> str:
    width, height = 880, 58
    return "\n".join(
        [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
            f' viewBox="0 0 {width} {height}" role="img"'
            f' aria-label="{escape(" ".join(TAGLINE))}" font-family=\'{MONO}\'>',
            f"<title>{escape(TAGLINE[0])}</title>",
            f'<circle cx="7" cy="15" r="3.5" fill="{ACCENT}"/>',
            f'<text x="22" y="20" fill="{INK}" font-size="15">{escape(TAGLINE[0])}</text>',
            f'<text x="22" y="42" fill="{DIM}" font-size="13.5">{escape(TAGLINE[1])}</text>',
            "</svg>",
        ]
    ) + "\n"


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    labels_dir = root / "assets" / "labels"
    labels_dir.mkdir(parents=True, exist_ok=True)

    (root / "assets" / "tagline.svg").write_text(tagline_svg(), encoding="utf-8")
    for slug, text in LABELS.items():
        (labels_dir / f"{slug}.svg").write_text(label_svg(text), encoding="utf-8")

    print(f"wrote assets/tagline.svg and {len(LABELS)} label(s) to assets/labels/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
