#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck source=/dev/null
[[ -f "${ROOT}/.env" ]] && source "${ROOT}/.env"
USERNAME="${GITHUB_USERNAME:-subkoks}"
GREEN="${GHCHART_COLOR:-238636}"

echo "Profile widget previews for @${USERNAME}"
echo ""
echo "Heatmap (steipete-style):"
echo "  https://ghchart.rshah.org/${GREEN}/${USERNAME}"
echo ""
echo "Old line chart (optional / about-me only):"
echo "  https://github-readme-activity-graph.vercel.app/graph?username=${USERNAME}&theme=github-dark&hide_border=true&area=true"
echo ""
echo "Profile views:"
echo "  https://komarev.com/ghpvc/?username=${USERNAME}&color=${GREEN}&style=flat-square&label=views"
echo ""
echo "Live profile:"
echo "  https://github.com/${USERNAME}"
