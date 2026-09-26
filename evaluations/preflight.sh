#!/usr/bin/env bash
# SPDX-FileCopyrightText: 2026 LibreCode coop and contributors
# SPDX-License-Identifier: AGPL-3.0-or-later

set -euo pipefail

if [[ "${ENABLE_SKILL_EVALS:-}" != 'true' ]]; then
  echo '::notice::Model evaluation disabled. Set ENABLE_SKILL_EVALS=true to opt in; no API key is needed for the other checks.'
  echo 'Model evaluation skipped (opt-in disabled). No API calls were made.' >> "$GITHUB_STEP_SUMMARY"
elif [[ -z "${MODEL_API_KEY:-}" ]]; then
  echo '::warning::Model evaluation skipped: OPENAI_API_KEY is not configured. The structural checks still run.'
  echo 'Model evaluation skipped (OPENAI_API_KEY is not configured). No API calls were made.' >> "$GITHUB_STEP_SUMMARY"
else
  echo 'enabled=true' >> "$GITHUB_OUTPUT"
  echo 'Model evaluation enabled for three synthetic fixtures.' >> "$GITHUB_STEP_SUMMARY"
fi
