# AI Development Practice Guide for Students

An English guide to Antigravity, Grok Build, GitHub Copilot, Codex, and Claude Code. Specifications and code form a shared foundation for handing work between tools and environments. Verification results are displayed in the conversation; saving them is optional and requires the user's request or agreement. Rerun checks after a move when no results were saved. Created for students enrolled in System Design; the examples can also be used independently.

- Start here: [Getting started](docs/index.md#getting-started)
- Costs and student benefits: [Official-source findings](docs/plans.md), checked on 2026-10-06
- Shared instructions: [Tool-independent working rules](docs/templates.md#tool-independent-working-rules)
- Python environment: [Set up Python with uv](docs/python-uv.md)
- Practice: [Complete a small development cycle](docs/practice.md)
- Maintenance: [Local checks and publication](docs/maintenance.md)
- Validation: [Local verification record](VALIDATION.md)
- Screenshots: [Desktop](artifacts/preview-desktop.png) / [Mobile](artifacts/preview-mobile.png)

## Read locally

For the student exercises, start with [Set up Python with uv](docs/python-uv.md). The commands below are for **building this website repository**, not for initializing a student's practice project.

Install uv using the manual, then run from this repository's root:

```sh
uv python install
uv sync --locked
uv run --locked python scripts/check_docs.py
uv run --locked mkdocs build --strict
uv run --locked python -m unittest discover -s docs/assets/example -v
uv run --locked mkdocs serve --dev-addr 127.0.0.1:8001
```

These commands work on macOS, Linux, and Windows PowerShell. No manual virtual-environment activation is needed. Open http://127.0.0.1:8001/ai-development-guide/ in your browser; stop with Ctrl+C. Generated HTML is stored in `site/`.

The website uses Python 3.12 and dependencies locked in uv.lock. pyproject.toml declares the project; requirements.txt is a generated compatibility export, not the primary environment definition.

## Project structure

```text
docs/                    Guide, official sources, and downloadable templates
docs/assets/templates/   Specification, environment, verification, and handoff templates
docs/assets/example/     Runnable Python example and tests
mkdocs.yml               Material for MkDocs and English search configuration
pyproject.toml           Website dependencies and migration constraints
.python-version          Python 3.12 selection for uv
uv.lock                  Resolved website dependency versions
requirements.txt         Generated compatibility export from uv.lock
.github/workflows/       Active GitHub Pages workflow with manual dispatch only
deployment/              Reusable draft of the deployment workflow
scripts/check_docs.py    Navigation, internal link, and template checks
scripts/check_preview.py Optional local browser checks
artifacts/               Screenshots from local verification
VALIDATION.md            Verification results for this guide
```

## Repository and publication status

Repository: [jkoba0512/ai-development-guide](https://github.com/jkoba0512/ai-development-guide).

Live website: https://jkoba0512.github.io/ai-development-guide/

The repository is public and the guide is published through GitHub Pages. The live pages, downloads, English search, dark mode, and mobile layout have been verified.

The active workflow is stored at `.github/workflows/pages.yml`. It runs local-equivalent checks, builds the site, and deploys through GitHub Pages when manually dispatched. A push alone does not deploy the site. Keep `.venv/` and generated `site/` out of Git.

External links and product setup instructions are based on official documentation research. Paid subscriptions, student verification, and hands-on operation of the five products have not been tested on the reader's behalf.

The English edition was prepared on 2026-10-13. Product findings retain their original verification date of 2026-10-06; translation is not a new pricing review.
