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

mkdir "$work/repo"
cd "$work/repo"
git init -q -b "$branch"
git config user.name "black.terminal"
git config user.email "subkoks@users.noreply.github.com"

# HTTPS with the gh credential helper: the agent may run without an ssh-agent,
# so the global https->ssh url rewrite is overridden for these remote operations.
remote_git() {
    git -c credential.helper= -c credential.helper='!gh auth git-credential' \
        -c "url.$repo_url.insteadOf=$repo_url" "$@"
}

if remote_git ls-remote --exit-code --heads "$repo_url" "refs/heads/$branch" > /dev/null; then
    remote_git fetch -q --depth=1 "$repo_url" "refs/heads/$branch"
    git switch -q --create "$branch" FETCH_HEAD
else
    status=$?
    if [ "$status" -ne 2 ]; then
        exit "$status"
    fi
fi

cp "$work/activity.svg" activity.svg
cp "$work/local-activity.json" local-activity.json
git add activity.svg local-activity.json
if git diff --cached --quiet; then
    echo "activity graph and local counts unchanged; nothing to publish"
    exit 0
fi

# Append to the published history without touching the SSH key.
git -c commit.gpgsign=false commit -q -m "chore(activity): refresh GitHub + local activity graph"
# A concurrent local/hosted update must fail rather than be overwritten.
remote_git push -q "$repo_url" "HEAD:refs/heads/$branch"

echo "published activity graph to $branch"
