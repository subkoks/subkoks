#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
# shellcheck source=/dev/null
[[ -f "${ROOT}/.env" ]] && source "${ROOT}/.env"

README="${PROFILE_REPO_PATH:-${ROOT}/profile/README.md}"
if [[ ! -f "${README}" ]]; then
  echo "README not found: ${README}" >&2
  exit 1
fi

MIN_IMAGE_BYTES=200

echo "Checking: ${README}"
FAIL=0
WARN=0

while IFS= read -r url; do
  read -r code ct size < <(
    curl -sL -o /dev/null \
      --max-time 15 \
      -w '%{http_code} %{content_type} %{size_download}\n' \
      "${url}" || echo "000 - 0"
  )

  status="OK"
  detail=""
  if [[ ! "${code}" =~ ^(200|301|302)$ ]]; then
    status="FAIL"
    FAIL=1
    detail="bad HTTP"
  elif [[ "${url}" =~ shields\.io|ghchart|komarev|streak-stats|github-readme ]]; then
    if [[ ! "${ct}" =~ image|svg ]]; then
      status="WARN"
      WARN=1
      detail="non-image content-type: ${ct}"
    elif (( size < MIN_IMAGE_BYTES )); then
      status="WARN"
      WARN=1
      detail="tiny image (${size}B) — likely broken slug or empty render"
    fi
  fi

  printf '  %-4s %s %s %s\n' "${status}" "${code}" "${url}" "${detail:+— ${detail}}"
done < <(grep -oE 'https?://[^)" ]+' "${README}" | sed 's/[),]$//' | sort -u)

if grep -q 'github-readme-activity-graph' "${README}"; then
  echo "  WARN profile still references github-readme-activity-graph (old line chart)" >&2
  WARN=1
fi

if grep -qiE 'master plan' "${README}"; then
  echo "  WARN MASTER PLAN mention without resolved link" >&2
  WARN=1
fi

echo ""
if (( FAIL > 0 )); then
  echo "Result: FAIL (one or more URLs broken)" >&2
  exit 1
fi
if (( WARN > 0 )); then
  echo "Result: OK with warnings"
  exit 0
fi
echo "Result: OK"
