#!/usr/bin/env python3
"""Collect local coding activity into a small JSON of per-day counts.

Two read-only sources, both on this machine:

* Codex session logs (`~/.codex/sessions/**/rollout-*.jsonl`) -> agent turns.
* Local git repositories (`~/Projects/**`) -> commit dates, including work that
  has not been pushed yet, which is exactly what GitHub cannot see.

Only counts are emitted. No prompts, code, file paths or session content leave
the machine, and the JSON that gets published stays inside this repository's
`activity` branch.

    python3 scripts/local_activity.py --out local-activity.json
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import pathlib
import re
import subprocess
import sys

DEFAULT_SESSIONS = pathlib.Path.home() / ".codex" / "sessions"
DEFAULT_PROJECTS = pathlib.Path.home() / "Projects"
DEFAULT_EXCLUDE = ("phase5-*",)

TIMESTAMP_RE = re.compile(r'"timestamp":"(\d{4}-\d{2}-\d{2})')
ROLLOUT_DATE_RE = re.compile(r"rollout-(\d{4}-\d{2}-\d{2})T")


def count_turns(sessions_dir: pathlib.Path, since: dt.date) -> dict[dt.date, int]:
    """Number of agent turns per day, from the session logs' own timestamps."""
    turns: dict[dt.date, int] = {}
    for path in sorted(sessions_dir.rglob("rollout-*.jsonl")):
        fallback = ROLLOUT_DATE_RE.search(path.name)
        fallback_date = dt.date.fromisoformat(fallback.group(1)) if fallback else None
        if fallback_date and fallback_date < since:
            continue
        try:
            handle = path.open(encoding="utf-8", errors="replace")
        except OSError:
            continue
        with handle:
            for line in handle:
                if '"turn_context"' not in line:
                    continue
                match = TIMESTAMP_RE.search(line)
                day = dt.date.fromisoformat(match.group(1)) if match else fallback_date
                if day and day >= since:
                    turns[day] = turns.get(day, 0) + 1
    return turns


def git(repo: pathlib.Path, *args: str) -> str:
    result = subprocess.run(
        ["git", "-C", str(repo), *args],
        capture_output=True,
        text=True,
        check=False,
    )
    return result.stdout


def count_commits(
    projects_dir: pathlib.Path, since: dt.date, exclude: tuple[str, ...], max_depth: int
) -> dict[dt.date, int]:
    """Commit dates across every local repository, pushed or not."""
    commits: dict[dt.date, int] = {}
    seen: set[pathlib.Path] = set()
    for marker in sorted(projects_dir.glob("**/.git")):
        repo = marker.parent
        depth = len(repo.relative_to(projects_dir).parts)
        if depth > max_depth or repo in seen:
            continue
        rel = repo.relative_to(projects_dir).as_posix()
        if any(fnmatch.fnmatch(rel, pattern) for pattern in exclude):
            continue
        seen.add(repo)
        out = git(repo, "log", f"--since={since.isoformat()}", "--format=%ad", "--date=short")
        for line in out.splitlines():
            line = line.strip()
            if line:
                day = dt.date.fromisoformat(line)
                commits[day] = commits.get(day, 0) + 1
    return commits


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--out", default="local-activity.json")
    parser.add_argument("--sessions-dir", default=str(DEFAULT_SESSIONS))
    parser.add_argument("--projects-dir", default=str(DEFAULT_PROJECTS))
    parser.add_argument("--days", type=int, default=365, help="window size in days")
    parser.add_argument(
        "--exclude",
        default=",".join(DEFAULT_EXCLUDE),
        help="comma-separated globs (relative to the projects dir) to skip",
    )
    parser.add_argument("--max-depth", type=int, default=4)
    args = parser.parse_args(argv)

    since = dt.date.today() - dt.timedelta(days=args.days - 1)
    exclude = tuple(g.strip() for g in args.exclude.split(",") if g.strip())

    sessions_dir = pathlib.Path(args.sessions_dir).expanduser()
    projects_dir = pathlib.Path(args.projects_dir).expanduser()

    turns = count_turns(sessions_dir, since) if sessions_dir.is_dir() else {}
    commits = (
        count_commits(projects_dir, since, exclude, args.max_depth)
        if projects_dir.is_dir()
        else {}
    )

    days: dict[str, dict[str, int]] = {}
    for day in sorted(set(turns) | set(commits)):
        days[day.isoformat()] = {"turns": turns.get(day, 0), "commits": commits.get(day, 0)}

    payload = {
        "generated_at": dt.datetime.now(dt.timezone.utc)
        .replace(microsecond=0)
        .isoformat()
        .replace("+00:00", "Z"),
        "window_days": args.days,
        "exclude": list(exclude),
        "totals": {
            "turns": sum(turns.values()),
            "commits": sum(commits.values()),
            "active_days": len(days),
        },
        "days": days,
    }

    out = pathlib.Path(args.out)
    out.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    totals = payload["totals"]
    print(
        f"{out}: {totals['turns']} turns, {totals['commits']} commits,"
        f" {totals['active_days']} active days"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
