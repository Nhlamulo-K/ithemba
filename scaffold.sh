#!/usr/bin/env bash
# scaffold.sh - creates the Ithemba repository structure.
# Usage: ./scaffold.sh [target-directory]      (default: ./ithemba)
# Safe to re-run: existing files are never overwritten.
set -euo pipefail

ROOT="${1:-ithemba}"
mkdir -p "$ROOT"
cd "$ROOT"

# ---------- helpers ----------
write_if_missing() {   # usage: write_if_missing <path>   (file content on stdin)
  if [ -e "$1" ]; then
    echo "skip    $1 (already exists)"
    cat >/dev/null
  else
    mkdir -p "$(dirname "$1")"
    cat >"$1"
    echo "created $1"
  fi
}

make_script() {        # usage: make_script <path> <description>
  write_if_missing "$1" <<EOF
#!/usr/bin/env bash
# $2
set -euo pipefail

# TODO: implement
echo "$1 is not implemented yet"
EOF
  chmod +x "$1"
}

# ---------- directories ----------
dirs=(
  frontend/css frontend/js
  backend/directory_api backend/tests
  etl/src etl/sql
  data/directory data/raw data/processed
  infra/cloudformation
  scripts
  local
  docs/screenshots
  .github/workflows
)
for d in "${dirs[@]}"; do mkdir -p "$d"; done

# ---------- .gitignore ----------
write_if_missing .gitignore <<'EOF'
# Secrets and local config - NEVER commit these
.env
.env.*
!.env.example
*.pem
*.key
credentials
.aws/

# Terraform (if you ever use it)
*.tfstate
*.tfstate.*
.terraform/
*.tfvars
!*.tfvars.example

# Python
__pycache__/
*.pyc
.venv/
venv/
.pytest_cache/
.mypy_cache/
*.egg-info/

# Build and packaging output
build/
dist/
*.zip
node_modules/

# Local data and emulator state
volume/
localstack-data/
data/raw/*
!data/raw/.gitkeep

# OS / editor
.DS_Store
Thumbs.db
.vscode/
.idea/
EOF

# ---------- .env.example ----------
write_if_missing .env.example <<'EOF'
# Copy to .env and fill in real values. Never commit .env.

# Local PostgreSQL (docker compose)
POSTGRES_USER=ithemba
POSTGRES_PASSWORD=change-me
POSTGRES_DB=ithemba

# AWS (use a named CLI profile or lab credentials - never paste keys into files that get committed)
AWS_REGION=af-south-1
AWS_PROFILE=

# Names used by the deploy scripts
PROJECT_NAME=ithemba
S3_SITE_BUCKET=
S3_DATA_BUCKET=

# Only needed if you choose to use LocalStack (it now requires a free account and auth token)
LOCALSTACK_AUTH_TOKEN=
EOF

# ---------- local docker compose ----------
write_if_missing local/docker-compose.yml <<'EOF'
# Run from the repo root:  docker compose -f local/docker-compose.yml --env-file .env up -d postgres
services:
  postgres:
    image: postgres:16
    environment:
      POSTGRES_USER: ${POSTGRES_USER:-ithemba}
      POSTGRES_PASSWORD: ${POSTGRES_PASSWORD:?set POSTGRES_PASSWORD in .env}
      POSTGRES_DB: ${POSTGRES_DB:-ithemba}
    ports:
      - "5432:5432"
    volumes:
      - pgdata:/var/lib/postgresql/data

  # Optional: AWS emulator. Requires a free LocalStack account + auth token in .env.
  # Start with:  docker compose -f local/docker-compose.yml --env-file .env --profile localstack up -d
  localstack:
    image: localstack/localstack
    profiles: ["localstack"]
    ports:
      - "4566:4566"
    environment:
      LOCALSTACK_AUTH_TOKEN: ${LOCALSTACK_AUTH_TOKEN:?set LOCALSTACK_AUTH_TOKEN in .env}

volumes:
  pgdata:
EOF

# ---------- backend ----------
write_if_missing backend/directory_api/handler.py <<'EOF'
"""Directory API Lambda handler (placeholder)."""
import json


def lambda_handler(event, context):
    # TODO: read services from DynamoDB, filter by province/type, return JSON
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"services": []}),
    }
EOF
write_if_missing backend/directory_api/requirements.txt <<'EOF'
boto3
EOF
write_if_missing backend/requirements-dev.txt <<'EOF'
pytest
moto[dynamodb,s3]
boto3
EOF
write_if_missing backend/tests/test_handler.py <<'EOF'
import json

from directory_api.handler import lambda_handler


def test_handler_returns_200():
    response = lambda_handler({}, None)
    assert response["statusCode"] == 200
    assert "services" in json.loads(response["body"])
EOF
write_if_missing backend/tests/__init__.py </dev/null
write_if_missing backend/directory_api/__init__.py </dev/null
write_if_missing backend/pytest.ini <<'EOF'
[pytest]
pythonpath = .
EOF

# ---------- frontend ----------
write_if_missing frontend/index.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ithemba</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- TODO: quick-exit button, helplines banner, support finder -->
  <main>
    <h1>Ithemba</h1>
    <p>Find safe help, quietly.</p>
  </main>
  <script src="js/app.js"></script>
</body>
</html>
EOF
write_if_missing frontend/insights.html <<'EOF'
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Ithemba - Insights</title>
  <link rel="stylesheet" href="css/style.css">
</head>
<body>
  <!-- TODO: load insights.json and draw charts -->
  <main><h1>Insights</h1></main>
</body>
</html>
EOF
write_if_missing frontend/css/style.css <<'EOF'
/* TODO: styles */
EOF
write_if_missing frontend/js/app.js <<'EOF'
// TODO: quick-exit handler, load directory, distance calculation in the browser
EOF

# ---------- etl ----------
write_if_missing etl/Dockerfile <<'EOF'
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
# Run as a non-root user
RUN useradd --create-home appuser
USER appuser
CMD ["python", "-m", "src.main"]
EOF
write_if_missing etl/requirements.txt <<'EOF'
boto3
psycopg2-binary
pandas
EOF
write_if_missing etl/src/__init__.py </dev/null
write_if_missing etl/src/main.py <<'EOF'
"""ETL entry point: ingest -> transform -> load -> export insights.json (placeholder)."""


def main():
    # TODO: call ingest, transform, load, export_insights
    print("ETL job not implemented yet")


if __name__ == "__main__":
    main()
EOF
for f in ingest transform load export_insights; do
  write_if_missing "etl/src/$f.py" <<EOF
"""$f step (placeholder)."""
EOF
done
write_if_missing etl/sql/schema.sql <<'EOF'
-- TODO: tables for crime statistics (e.g. period, province, precinct, category, count)
EOF

# ---------- data ----------
write_if_missing data/directory/services.json <<'EOF'
[]
EOF
write_if_missing data/raw/.gitkeep </dev/null
write_if_missing data/processed/.gitkeep </dev/null

# ---------- infrastructure ----------
write_if_missing infra/cloudformation/01-network.yaml <<'EOF'
AWSTemplateFormatVersion: "2010-09-09"
Description: Ithemba - network (VPC, subnets, security groups, endpoints)
Resources: {}
# TODO: add resources. Avoid NAT Gateways (hourly cost); use free S3/DynamoDB gateway endpoints.
EOF
write_if_missing infra/cloudformation/02-data.yaml <<'EOF'
AWSTemplateFormatVersion: "2010-09-09"
Description: Ithemba - data (DynamoDB, RDS, S3 buckets)
Resources: {}
EOF
write_if_missing infra/cloudformation/03-app.yaml <<'EOF'
AWSTemplateFormatVersion: "2010-09-09"
Description: Ithemba - application (Lambda, API Gateway, CloudFront, EC2)
Resources: {}
EOF

# ---------- scripts ----------
make_script scripts/deploy.sh            "Deploy the CloudFormation stacks in order (network, data, app)."
make_script scripts/teardown.sh          "Delete all Ithemba stacks and empty the S3 buckets. Run after every demo."
make_script scripts/validate_directory.sh "Validate data/directory/services.json (required fields, phone formats, stale entries)."
make_script scripts/backup_to_s3.sh      "Back up the directory data to S3."
make_script scripts/harden_server.sh     "Basic EC2 hardening: non-root user, key-only SSH, firewall."

# ---------- docs ----------
write_if_missing docs/architecture.md <<'EOF'
# Architecture

TODO: diagram (save as docs/architecture-diagram.png) and component descriptions.
EOF
write_if_missing docs/data-sources.md <<'EOF'
# Data sources

## Directory entry format (suggested)

Fields: name, type (shelter | thuthuzela | police | legal | helpline | clinic),
province, city, address, latitude, longitude, phone, hours, source_url, last_verified.

## Sources

TODO: list each official source, what you took from it, and the date you checked it.
EOF
write_if_missing docs/privacy-and-safety.md <<'EOF'
# Privacy and safety

TODO: explain the design choices (no accounts, no tracking, location stays in the browser,
quick exit, neutral titles, no personal data stored) and how they reduce risk to users.
EOF
write_if_missing docs/screenshots/.gitkeep </dev/null

# ---------- CI ----------
write_if_missing .github/workflows/ci.yml <<'EOF'
name: CI
on: [push, pull_request]

jobs:
  checks:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install tools
        run: |
          pip install cfn-lint -r backend/requirements-dev.txt

      - name: Lint CloudFormation
        run: cfn-lint infra/cloudformation/*.yaml

      - name: Lint shell scripts
        run: shellcheck scripts/*.sh

      - name: Python tests
        working-directory: backend
        run: pytest

      - name: Build ETL image
        run: docker build -t ithemba-etl etl/
EOF

echo
echo "Done. Next steps:"
echo "  1. Copy README.md into $(pwd)"
echo "  2. git init && git add . && git commit -m 'Initial project structure'"
echo "  3. cp .env.example .env   (then fill in values; .env is git-ignored)"
