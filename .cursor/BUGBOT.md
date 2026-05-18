# Bugbot — subkoks profile README review rules

## Repository type

GitHub profile README only (`README.md`). No application runtime.

## Review focus

- Flag broken image/badge URLs or shields.io links that 404.
- Flag exposing private email, phone, wallet addresses, or seed phrases in README.
- Flag `cache_seconds` or embed params that break GitHub's renderer (invalid query strings).
- Keep badge styling consistent (dark theme: `bg_color=161b22`, accent `238636` / `2ea043`).

## Non-blocking

- Wording, emoji, or layout preference changes.
- Third-party stats service downtime (komarev, streak stats) — note only, do not block.

## Scope

- Do not request tests or CI for markdown-only profile updates unless workflows are added.
