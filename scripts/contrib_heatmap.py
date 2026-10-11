#!/usr/bin/env python3
"""Render the GitHub contribution calendar as a self-contained SVG.

The profile README embeds the generated file, so the heatmap can use a palette
GitHub does not offer (dark card, orange squares) and does not depend on a
third-party chart service staying up.

Data comes from GitHub's public contribution calendar HTML: no token and no API
quota. `--local-json` optionally merges local coding activity (Codex turns and
local commits, including unpushed work) collected by
`scripts/local_activity.py`. A day takes the brighter of the two levels, so the
graph reads "GitHub or local work happened". Refresh manually with:

    python3 scripts/contrib_heatmap.py --user subkoks --out assets/activity.svg
    python3 scripts/contrib_heatmap.py --user subkoks --out activity.svg \
        --local-json local-activity.json

`.github/workflows/activity-graph.yml` runs the same command weekly and
publishes the result to the `activity` branch, which is what the README loads.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import pathlib
import re
import sys
import urllib.error
import urllib.request
from xml.sax.saxutils import escape

CELL = 11
GAP = 3
STEP = CELL + GAP
PAD_LEFT = 34
PAD_TOP = 20
PAD_RIGHT = 14
LEGEND_TOP_GAP = 18

BG = "#000000"
LABEL = "#8d8178"
FONT = '-apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif'

# Level 0 (no contributions) through 4 (busiest), dark to bright.
LEVELS = ("#241c18", "#5a2f0c", "#98490c", "#d2690b", "#ff9f43")

# Local activity points (turns + commits) needed to reach each level above zero.
LOCAL_STEPS = (4, 14, 39)

MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec")
# GitHub's calendar runs Sunday-first; label alternate days only.
WEEKDAY_LABELS = {1: "Mon", 3: "Wed", 5: "Fri"}

CELL_RE = re.compile(r"<td\b[^>]*>", re.I)
DATE_RE = re.compile(r'data-date="(\d{4}-\d{2}-\d{2})"')
LEVEL_RE = re.compile(r'data-level="(\d)"')
TOTAL_RE = re.compile(
    r'id="js-contribution-activity-description"[^>]*>\s*([\d,]+)\s*contributions'
)


def fetch_html(user: str, timeout: float = 30.0) -> str:
    url = f"https://github.com/users/{user}/contributions"
    request = urllib.request.Request(
        url, headers={"User-Agent": "contrib-heatmap/1.0 (profile README generator)"}
    )
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return response.read().decode("utf-8", "replace")


def parse_calendar(html: str) -> tuple[dict[dt.date, int], str | None]:
    """Map each day to its contribution level, plus the trailing-year total."""
    days: dict[dt.date, int] = {}
    for tag in CELL_RE.findall(html):
        date_match = DATE_RE.search(tag)
        level_match = LEVEL_RE.search(tag)
        if date_match and level_match:
            day = dt.date.fromisoformat(date_match.group(1))
            days[day] = min(4, int(level_match.group(1)))
    if not days:
        raise ValueError("no contribution cells found (GitHub layout changed?)")
    total = TOTAL_RE.search(html)
    return days, (total.group(1) if total else None)


def local_level(points: int) -> int:
    """Bucket local activity into the same 0-4 scale as GitHub's levels."""
    if points <= 0:
        return 0
    for level, ceiling in enumerate(LOCAL_STEPS, start=1):
        if points <= ceiling:
            return level
    return 4


def load_local(path: pathlib.Path) -> tuple[dict[dt.date, int], dict[str, int]]:
    """Read the collector's JSON into per-day points plus its totals."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    points: dict[dt.date, int] = {}
    for day, counts in payload.get("days", {}).items():
        total = sum(int(v) for v in counts.values())
        if total:
            points[dt.date.fromisoformat(day)] = total
    return points, {k: int(v) for k, v in payload.get("totals", {}).items()}


def render(
    days: dict[dt.date, int],
    total: str | None,
    *,
    user: str,
    bg: str = BG,
    levels: tuple[str, ...] = LEVELS,
    label: str = LABEL,
    local_points: dict[dt.date, int] | None = None,
    local_totals: dict[str, int] | None = None,
) -> str:
    # GitHub levels win by default; local activity can only brighten a day.
    merged = dict(days)
    for day, points in (local_points or {}).items():
        merged[day] = max(merged.get(day, 0), local_level(points))

    first, last = min(merged), max(merged)
    # Anchor the grid to the Sunday on or before the first day so columns are weeks.
    start = first - dt.timedelta(days=(first.weekday() + 1) % 7)
    columns = (last - start).days // 7 + 1

    grid_width = columns * STEP - GAP
    grid_height = 7 * STEP - GAP
    width = PAD_LEFT + grid_width + PAD_RIGHT
    legend_y = PAD_TOP + grid_height + LEGEND_TOP_GAP
    height = legend_y + CELL + 6

    if local_totals:
        summary = (
            f"{total or 0} on GitHub · {local_totals.get('turns', 0)} turns ·"
            f" {local_totals.get('commits', 0)} commits"
        )
    else:
        summary = f"{total} contributions in the last year" if total else f"@{user} contribution activity"
    body: list[str] = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}"'
        f' viewBox="0 0 {width} {height}" role="img"'
        f' aria-label="Contribution activity for @{escape(user)}: {escape(summary)}"'
        f' font-family=\'{FONT}\' font-size="10">',
        f"<title>@{escape(user)} — {escape(summary)}</title>",
        f'<rect width="{width}" height="{height}" rx="8" fill="{bg}"/>',
    ]

    previous_month: int | None = None
    for column in range(columns):
        week_start = start + dt.timedelta(days=column * 7)
        if week_start.month != previous_month:
            previous_month = week_start.month
            x = PAD_LEFT + column * STEP
            body.append(
                f'<text x="{x}" y="{PAD_TOP - 7}" fill="{label}">'
                f"{MONTHS[week_start.month - 1]}</text>"
            )

    for day, level in sorted(merged.items()):
        column = (day - start).days // 7
        row = (day.weekday() + 1) % 7
        x = PAD_LEFT + column * STEP
        y = PAD_TOP + row * STEP
        body.append(
            f'<rect x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2"'
            f' fill="{levels[level]}"/>'
        )

    for row, name in WEEKDAY_LABELS.items():
        y = PAD_TOP + row * STEP + CELL - 2
        body.append(
            f'<text x="{PAD_LEFT - 6}" y="{y}" text-anchor="end" fill="{label}">'
            f"{name}</text>"
        )

    legend_x = PAD_LEFT
    body.append(f'<text x="{legend_x}" y="{legend_y + CELL - 2}" fill="{label}">Less</text>')
    swatch_x = legend_x + 34
    for color in levels:
        body.append(
            f'<rect x="{swatch_x}" y="{legend_y}" width="{CELL}" height="{CELL}"'
            f' rx="2" fill="{color}"/>'
        )
        swatch_x += STEP
    body.append(f'<text x="{swatch_x + 4}" y="{legend_y + CELL - 2}" fill="{label}">More</text>')
    if total or local_totals:
        body.append(
            f'<text x="{width - PAD_RIGHT}" y="{legend_y + CELL - 2}"'
            f' text-anchor="end" fill="{label}">{escape(summary)}</text>'
        )

    body.append("</svg>")
    return "\n".join(body) + "\n"


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--user", default="subkoks", help="GitHub login to render")
    parser.add_argument("--out", default="assets/activity.svg", help="SVG output path")
    parser.add_argument("--html", help="read a saved contributions page instead of fetching")
    parser.add_argument("--bg", default=BG, help=f"background colour (default {BG})")
    parser.add_argument(
        "--colors",
        help="comma-separated level palette, dark to bright (default: orange ramp)",
    )
    parser.add_argument(
        "--local-json",
        help="merge local activity counts from scripts/local_activity.py",
    )
    args = parser.parse_args(argv)

    levels = LEVELS
    if args.colors:
        levels = tuple(color.strip() for color in args.colors.split(","))
        if len(levels) != 5:
            parser.error("--colors needs exactly 5 colours (levels 0-4)")

    try:
        html = (
            pathlib.Path(args.html).read_text(encoding="utf-8", errors="replace")
            if args.html
            else fetch_html(args.user)
        )
    except (urllib.error.URLError, OSError) as error:
        print(f"could not load contributions: {error}", file=sys.stderr)
        return 1

    days, total = parse_calendar(html)

    local_points: dict[dt.date, int] = {}
    local_totals: dict[str, int] = {}
    if args.local_json:
        local_path = pathlib.Path(args.local_json)
        if local_path.is_file():
            local_points, local_totals = load_local(local_path)
        else:
            print(f"note: {local_path} not found, rendering GitHub only", file=sys.stderr)

    svg = render(
        days,
        total,
        user=args.user,
        bg=args.bg,
        levels=levels,
        local_points=local_points,
        local_totals=local_totals,
    )

    out = pathlib.Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(svg, encoding="utf-8")
    detail = f", local days={len(local_points)}" if local_points else ""
    print(f"{out}: {len(days)} days {min(days)}..{max(days)}, total={total}{detail}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
