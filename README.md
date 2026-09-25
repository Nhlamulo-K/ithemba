# Ithemba

**Find safe help, quietly.** Ithemba is a discreet support finder and awareness dashboard for gender-based violence (GBV) in South Africa.

> **Disclaimer:** Ithemba is a personal project. It is not an emergency service and does not replace professional help. Directory information may be out of date; always confirm details with the organisation.

---

## What Ithemba does

**1. Support finder**
- Find shelters, Thuthuzela Care Centres, police stations, legal aid and helplines by province or nearby location.
- Quick-exit button that leaves the site immediately.
- No login, no tracking, no stored searches.
- Location is handled in the browser and never sent to the server.

**2. Insights dashboard**
- Charts built from published public statistics, for awareness and advocacy.
- Updated by a scheduled data pipeline.

## Architecture


| Component | Purpose |
|---|---|
| S3 + CloudFront | Hosts the static site |
| API Gateway + Lambda (Python) | Directory API |
| DynamoDB | Support-services directory |
| RDS PostgreSQL | Statistics used by the insights pipeline |
| Dockerised ETL job | Cleans data, loads the database, writes `insights.json` to S3 |
| EC2 | Runs scheduled validation and backup scripts |
| VPC, IAM, Parameter Store | Network isolation, least privilege, secrets |
| CloudFormation | Infrastructure as code |
| GitHub Actions | Linting and tests |

## How it covers the course topics

| Topic | Where it appears in Ithemba |
|---|---|
| Cloud computing |
| Linux and bash |
| Networking |
| Security |
| Python programming | Backend |
| Databases |
| Tooling and automation |
| Servers |
| Serverless |
| Containers |

## Privacy and safety by design

- No user accounts, cookies for tracking, analytics or stored search history.
- The user's location stays on their device.
- Neutral page titles and a quick-exit button.
- No personal data is collected or stored anywhere in the system.
- Least-privilege IAM roles; secrets kept out of the repo.

## Repository structure

```text
ithemba/
├── frontend/          Static site (support finder + insights pages)
├── backend/           Directory API (Python Lambda) and its tests
├── etl/               Dockerised data pipeline and SQL schema
├── data/              Directory dataset, raw and processed statistics
├── infra/             CloudFormation templates
├── scripts/           Bash scripts: deploy, teardown, validate, backup, harden
├── local/             docker-compose for local development
