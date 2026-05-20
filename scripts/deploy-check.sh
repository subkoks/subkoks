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

echo "Checking: ${README}"
FAIL=0

while IFS= read -r url; do
  code="$(curl -sL -o /dev/null -w "%{http_code}" --max-time 15 "${url}" || echo "000")"
  if [[ "${code}" =~ ^(200|301|302)$ ]]; then
    echo "  OK ${code} ${url}"
  else
    echo "  FAIL ${code} ${url}" >&2
    FAIL=1
  fi
done < <(grep -oE 'https?://[^)]+' "${README}" | sed 's/)$//' | sort -u)

if grep -q 'github-readme-activity-graph' "${README}"; then
  echo "  WARN: profile still references github-readme-activity-graph (line chart)" >&2
fi

if grep -q 'MASTER PLAN' "${README}"; then
  echo "  WARN: MASTER PLAN mention without repo link" >&2
fi

exit "${FAIL}"
