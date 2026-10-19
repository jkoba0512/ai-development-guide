# Local Checks and Publication Preparation

**For guide maintainers.** Students can use the published pages directly; building or publishing this website is separate from the Python practice project.

This guide uses Material for MkDocs and is published at https://jkoba0512.github.io/ai-development-guide/. The active deployment workflow is in `.github/workflows/pages.yml`; deploy updates manually after completing the local checks below.

## Build locally

Install uv using [Python and uv setup](python-uv.md#install-uv). This repository already contains pyproject.toml, .python-version, and uv.lock. Do not run uv init here. Run from the repository root:

```sh
uv python install
uv sync --locked
uv run --locked python scripts/check_docs.py
uv run --locked mkdocs build --strict
uv run --locked python -m unittest discover -s docs/assets/example -v
uv run --locked mkdocs serve --dev-addr 127.0.0.1:8001
```

Open http://127.0.0.1:8001/ai-development-guide/. The same commands work in PowerShell.

The final command keeps running. Open the site in a browser and check navigation, English search, tables, code blocks, dark mode, and template downloads. Stop with Ctrl+C. Binding only to loopback keeps this preview local.

`check_docs.py` checks internal file links, heading fragments, navigation entries, and template presence. It does not automatically establish external URL availability or pricing accuracy.

Official references: [Material getting started](https://squidfunk.github.io/mkdocs-material/getting-started/) and [publishing](https://squidfunk.github.io/mkdocs-material/publishing-your-site/).

## Checks when updating

1. Reopen official pages for changing prices and benefits.
2. Check region, deadlines, reverification, renewal billing, and supported environments.
3. Append the verification date and changes to [sources.md](sources.md).
4. Keep the comparison and tool pages consistent.
5. Run internal-link checks and a strict build, then inspect representative pages in a browser.

When deliberately updating website dependencies, review pyproject.toml (including the migration constraints retaining previously verified versions), regenerate uv.lock with uv lock, and run uv sync --locked. Repeat the checks above. requirements.txt is a compatibility export; refresh it with:

```sh
uv export --locked --no-hashes --no-emit-project --output-file requirements.txt
```

Do not edit the exported requirements.txt instead of the project definition. If a price or benefit cannot be established, mark it as unverified instead of guessing.

## Publish or update GitHub Pages

The repository and site URL are configured for this project. For updates, complete the local checks, commit and push the intended files, then manually dispatch the Pages workflow. For a new copy of the guide, use the full setup procedure below.

1. Review content, downloads, and history for publication. Check repository visibility and Pages eligibility.
2. Create a remote repository and decide its owner, name, and public URL.
3. Set `site_url: https://OWNER.github.io/REPOSITORY/` in mkdocs.yml. Use the appropriate URL for a user site or other arrangement.
4. Copy `deployment/pages.yml.example` to `.github/workflows/pages.yml`. Recheck recommended action versions in official documentation.
5. In GitHub Settings → Pages → Build and deployment, select GitHub Actions.
6. Commit and push only the files intended for publication.
7. Dispatch the workflow manually in GitHub Actions. A push alone does not trigger this workflow.
8. Check relative paths, search, and downloads at the public URL.

The build job has contents: read permission. The deploy job has pages: write and id-token: write. Review restrictions can also be configured on the `github-pages` environment. [GitHub Pages documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site).

## Before publication

- [ ] Content and history contain no personal information, secrets, verification documents, or real private data.
- [ ] Unverified conditions are not presented as established facts.
- [ ] Dependencies can be reinstalled at the same versions.
- [ ] Internal links, strict build, and sample tests pass.
- [ ] Copyright, distribution licensing, and citations have been reviewed and any required policy decided.
- [ ] The destination and deployment permissions are understood.
