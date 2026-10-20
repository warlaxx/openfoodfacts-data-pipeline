# Project context for Claude

See [README.md](README.md) for what this project is and [ROADMAP.md](ROADMAP.md) for
its milestones, decisions and current status.

## Who this is for

Abdallah is a Java/Spring Boot integration developer (Amiltone, on assignment at Prosol since
21 September 2026: Databricks → Fabric flows with Azure Functions, Key Vault, OpCon, Terraform,
GitHub Actions). This repository is a **learning and portfolio project** to become a data
platform engineer. Python and PySpark are new to them.

## Golden rule

You may write infrastructure, CI, tooling, docs and the dashboard. **Do not implement the
transformations** (`bronze/`, `silver/`, `gold/`, `quality/` functions marked « À toi de jouer »).
Explain, review, ask questions, suggest tests, point at docs — but let Abdallah write that code.

## Current state — 21 October 2026

Milestone 0 (skeleton) is done: package layout, Spark + Delta session, sample downloader,
pytest with a passing Delta smoke test, ruff, Makefile, GitHub Actions CI. Transformation
modules are stubs raising `NotImplementedError`. Next: week 1 (Python basics) and week 2
(exploration of the sample).

## How to run

Python 3.12 and Java 21. `make install`, `make sample`, `make test`, `make lint`.
`spark.py` forces `PYSPARK_PYTHON` to the venv interpreter (the system `python3` is 3.10).

## Tracking

- Backlog: Linear, team ABD, project [openfoodfacts-data-pipeline](https://linear.app/abdallah-abdallaoui-maane/project/openfoodfacts-data-pipeline-c1987c0287b5) (labels in the `OFF` group: Code, Apprentissage, Montée en compétence, Carrière).
- Documentation: Notion page [Open Food Facts Pipeline](https://app.notion.com/p/3ffa88cf47be8132a908ea8c75547838) (private for now); log each doc update in its « Journal de la documentation ».
- Mentor: the `data-engineer-mentor` agent in `.claude/agents/` reviews progress and opens
  skill-gap issues in Linear (label `Montée en compétence`).

When you finish a piece of work, update the « Current state » paragraph above, the matching
checkboxes in ROADMAP.md, and the Linear issue.
