# AI Development Practice Guide for Students

An English guide to Antigravity, Grok Build, GitHub Copilot, Codex, and Claude Code. Specifications, code, and verification records form a shared foundation for handing work between tools and environments. Created for students enrolled in System Design; the examples can also be used independently.

- Start here: [Getting started](docs/index.md#getting-started)
- Costs and student benefits: [Official-source findings](docs/plans.md), checked on 2026-10-06
- Shared instructions: [Tool-independent working rules](docs/templates.md#tool-independent-working-rules)
- Practice: [Complete a small development cycle](docs/practice.md)
- Maintenance: [Local checks and publication](docs/maintenance.md)
- Validation: [Local verification record](VALIDATION.md)
- Screenshots: [Desktop](artifacts/preview-desktop.png) / [Mobile](artifacts/preview-mobile.png)

## Read locally

Use Python 3.11 or later. Run these commands from the project root:

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m mkdocs build --strict
python -m mkdocs serve --dev-addr 127.0.0.1:8000
```

On Windows PowerShell, create the environment with `py -3 -m venv .venv` and activate it with `.venv\Scripts\Activate.ps1`. If activation is unavailable, invoke Python directly, for example `.venv\Scripts\python.exe -m pip install -r requirements.txt`.

Open http://127.0.0.1:8000/ in your browser. Stop the server with Ctrl+C. Generated HTML is stored in `site/`.

With uv installed, you can use `uv venv` and `uv pip install -r requirements.txt`.

## Project structure

```text
docs/                    Guide, official sources, and downloadable templates
docs/assets/templates/   Specification, environment, verification, and handoff templates
docs/assets/example/     Runnable Python example and tests
mkdocs.yml               Material for MkDocs and English search configuration
requirements.txt         All dependency versions from the verified local environment
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
