#!/usr/bin/env bash
set -euo pipefail

API_URL="https://PLACEHOLDER.execute-api.us-west-2.amazonaws.com/services"

cd "$(dirname "${BASH_SOURCE[0]}")/../backend"
curl -s "$API_URL" | py directory_api/validate.py