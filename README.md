# Ithemba

> *Ithemba* means "hope" in isiZulu and isiXhosa.

**Find safe help, quietly.** Ithemba is a discreet support finder and awareness dashboard for gender-based violence (GBV) in South Africa, built on AWS as a cloud computing course project.

> **If you or someone you know is in danger, call SAPS on 10111.**
> GBV Command Centre (24 hours, free): **0800 428 428** or dial **\*120\*7867#**
> Stop Gender Violence Helpline (free): **0800 150 150**
>
> *[TODO: re-verify every number against an official source before publishing, and update the "last verified" date: YYYY-MM-DD]*

> **Disclaimer:** Ithemba is a student project and a prototype. It is not an emergency service and does not replace professional help. Directory information may be out of date; always confirm details with the organisation.

---

## Table of contents

1. [The problem](#the-problem)
2. [What Ithemba does](#what-ithemba-does)
3. [Architecture](#architecture)
4. [How it covers the course topics](#how-it-covers-the-course-topics)
5. [Privacy and safety by design](#privacy-and-safety-by-design)
6. [Repository structure](#repository-structure)
7. [Getting started (local)](#getting-started-local)
8. [Deploying to AWS](#deploying-to-aws)
9. [Data sources and verification](#data-sources-and-verification)
10. [Testing and CI](#testing-and-ci)
11. [Cost and cleanup](#cost-and-cleanup)
12. [Screenshots](#screenshots)
13. [Limitations and roadmap](#limitations-and-roadmap)
14. [Acknowledgements](#acknowledgements)
15. [Licence](#licence)

---

## The problem

*[TODO: 1-2 short paragraphs. Why GBV is a serious socio-economic issue in South Africa, and why finding help quickly and safely matters. Cite official sources for any statistic you use.]*

## What Ithemba does

**1. Support finder**
- Find shelters, Thuthuzela Care Centres, police stations, legal aid and helplines by province or nearby location.
- Quick-exit button that leaves the site immediately.
- No login, no tracking, no stored searches.
- Location is handled in the browser and never sent to the server.

**2. Insights dashboard**
- Charts built from published public statistics, for awareness and advocacy.
- Updated by a scheduled data pipeline.

*[TODO: add a short description or GIF of each feature once built.]*

## Architecture

![Architecture diagram](docs/architecture-diagram.png)

*[TODO: add the diagram, then describe each component in a sentence or two.]*

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
| Cloud computing | *[TODO]* |
| Linux and bash | *[TODO: e.g. `scripts/`, server hardening, cron]* |
| Networking | *[TODO: VPC, subnets, security groups, VPC endpoints]* |
| Security | *[TODO: IAM roles, HTTPS, private bucket, secrets handling]* |
| Python programming | *[TODO: Lambda handler, ETL job]* |
| Databases | *[TODO: DynamoDB and PostgreSQL, and why both]* |
| Tooling and automation | *[TODO: CloudFormation, deploy script, CI]* |
| Servers | *[TODO: EC2 setup and jobs]* |
| Serverless | *[TODO: Lambda, API Gateway, S3, CloudFront]* |
| Containers | *[TODO: ETL Dockerfile and how it runs]* |

## Privacy and safety by design

- No user accounts, cookies for tracking, analytics or stored search history.
- The user's location stays on their device.
- Neutral page titles and a quick-exit button.
- No personal data is collected or stored anywhere in the system.
- Least-privilege IAM roles; secrets kept out of the repo.
- *[TODO: note how this aligns with POPIA principles, in your own words.]*

See [`docs/privacy-and-safety.md`](docs/privacy-and-safety.md) for more detail.

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
├── docs/              Architecture, data sources, privacy notes, screenshots
└── .github/workflows/ CI
```

## Getting started (local)

**Prerequisites:** *[TODO: Docker, Python 3.x, AWS CLI, Git, versions]*

```bash
git clone https://github.com/<your-username>/ithemba.git
cd ithemba
cp .env.example .env        # then fill in your own values
docker compose -f local/docker-compose.yml up -d postgres
# TODO: commands to run the API tests, ETL job and front end
```

*[TODO: explain how to run each part locally. Unit tests use `moto`, which needs no AWS account.]*

## Deploying to AWS

*[TODO: prerequisites (AWS account, CLI configured, region), then the deploy order.]*

```bash
./scripts/deploy.sh
```

*[TODO: stacks and the order they deploy in (network, data, app), expected outputs, and how to tear everything down with `./scripts/teardown.sh`.]*

## Data sources and verification

- Directory entries come from *[TODO: official sources, e.g. government and NGO websites]*.
- Every entry has a `last_verified` date.
- Statistics come from *[TODO: source and release, e.g. SAPS crime statistics, with dates]*.
- Full list and method: [`docs/data-sources.md`](docs/data-sources.md).

## Testing and CI

- Python tests: `pytest` (AWS calls mocked with `moto`)
- Infrastructure lint: `cfn-lint`
- Shell script lint: `shellcheck`
- GitHub Actions runs all of the above on every push.

## Cost and cleanup

*[TODO: which AWS services you used, that you stayed within free credits, the budget alert you set up, and confirmation that all resources were deleted after the demo.]*

## Screenshots

*[TODO: add images from `docs/screenshots/`: the site, the AWS console for each slice, and a successful deployment.]*

## Limitations and roadmap

**Limitations**
- Prototype only; the directory covers a limited set of services.
- *[TODO]*

**Ideas for future work**
- More provinces and languages (isiZulu, isiXhosa, Sesotho and others)
- Offline-friendly / low-data mode
- Partnering with an NGO to keep the directory verified
- *[TODO]*

## Acknowledgements

*[TODO: list data sources, organisations, tutorials, your course and instructors.]*

## Licence

*[TODO: choose a licence, e.g. MIT, and add a `LICENSE` file. Ask your course whether there are any rules about how project work may be licensed.]*
