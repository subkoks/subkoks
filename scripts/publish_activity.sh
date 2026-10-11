#!/usr/bin/env bash
# Publish this machine's contribution graph - GitHub activity merged with local
# Codex turns and local commits - to the `activity` branch of subkoks/subkoks,
# which is the image the profile README loads.
#
# Called hourly by ~/Library/LaunchAgents/com.blackterminal.activity-sync.plist,
# and safe to run by hand. Reads only counts (never session content) and pushes
# nothing when the rendered graph is unchanged.
set -euo pipefail

repo_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
repo_url="https://github.com/subkoks/subkoks.git"
branch="activity"
user="subkoks"

work="$(mktemp -d)"
trap 'rm -rf "$work"' EXIT

python3 "$repo_dir/scripts/local_activity.py" --out "$work/local-activity.json"
python3 "$repo_dir/scripts/contrib_heatmap.py" \
    --user "$user" \
    --local-json "$work/local-activity.json" \
    --out "$work/activity.svg"

# Skip the push (and the image-cache churn) when nothing actually changed.
# Compared through the API rather than raw.githubusercontent.com, whose CDN
# serves stale copies for a few minutes after a push.
local_blob="$(git -C "$repo_dir" hash-object "$work/activity.svg")"
remote_blob="$(gh api "repos/$user/subkoks/contents/activity.svg?ref=$branch" \
    --jq .sha 2>/dev/null || true)"
if [ -n "$remote_blob" ] && [ "$remote_blob" = "$local_blob" ]; then
    echo "activity graph unchanged; nothing to publish"
    exit 0
fi

cd "$work"
git init -q -b "$branch"
git config user.name "black.terminal"
git config user.email "subkoks@users.noreply.github.com"
git add activity.svg local-activity.json
# Machine-generated commit on a throwaway branch: no need to touch the SSH key.
git -c commit.gpgsign=false commit -q -m "chore(activity): refresh GitHub + local activity graph"

# HTTPS with the gh credential helper: the agent may run without an ssh-agent,
# so the global https->ssh url rewrite is overridden for this one push.
git -c credential.helper= -c credential.helper='!gh auth git-credential' \
    -c "url.$repo_url.insteadOf=$repo_url" \
    push -q --force "$repo_url" "$branch"

echo "published activity graph to $branch"
