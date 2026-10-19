# Local Verification Record

## English edition — 2026-10-13

Scope: translate the guide, templates, prompts, configuration, sample messages, and project documentation into English. Product research retains its original date of 2026-10-06.

All English-edition checks passed locally.

| Check | Result |
| --- | --- |
| Source-language scan | No Japanese text in README, validation record, configuration, guide, templates, sample code, scripts, or deployment draft |
| Internal links and navigation | Passed: 17 pages and 6 templates |
| Sample tests | Passed: all 9 tests, including translated CLI output and error messages |
| Strict build | Passed: generated English HTML in site/ |
| Local preview | Served on http://127.0.0.1:8001/; port 8000 was already in use |
| HTTP checks | All 17 pages and 9 static assets returned HTTP 200 |
| English interface | Checked pages use html lang=en; navigation and theme controls are English |
| English search | Query "handoff" returned visible results |
| Dark mode and mobile layout | Passed; no document-wide overflow at 390×844 |
| Browser errors | No JavaScript page errors on checked pages |
| Screenshots | Regenerated desktop and mobile images and reviewed both |

Commands used:

```sh
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python scripts/check_docs.py
PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s docs/assets/example -v
.venv/bin/python -m mkdocs build --strict
.venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8001
GUIDE_PREVIEW_URL=http://127.0.0.1:8001 uv run --python .venv/bin/python --with playwright python scripts/check_preview.py
```

External publication remains unperformed.

## Initial edition — 2026-10-06 (Asia/Tokyo)

The original local files were checked before Git initialization.

### Environment

- macOS 26.6.2 / arm64
- Python 3.12.11 in .venv
- MkDocs 1.6.1 / Material for MkDocs 9.7.6
- All 29 dependencies pinned in requirements.txt
- Local Google Chrome, checked headlessly with Playwright

### Original results

| Check | Command / method | Result |
| --- | --- | --- |
| Internal links, navigation, templates | .venv/bin/python scripts/check_docs.py | Passed: 17 pages, relative links, 6 templates |
| Sample tests | PYTHONDONTWRITEBYTECODE=1 .venv/bin/python -m unittest discover -s docs/assets/example -v | Passed: 9 tests covering normal, boundary, and invalid inputs, CLI exit codes, and repeatability |
| Strict build | .venv/bin/python -m mkdocs build --strict | Passed: exit code 0, generated site/ |
| Local serving | .venv/bin/python -m mkdocs serve --dev-addr 127.0.0.1:8000 | Passed: loopback only |
| All pages and downloads | scripts/check_preview.py | 17 pages and 9 static assets returned HTTP 200 |
| Original-language search | Browser search for the original handoff term | Passed: 9 relevant results |
| Dark mode | Browser toggle | Passed |
| Mobile width | Practice page at 390×844 | Passed: no document-wide horizontal overflow |
| JavaScript | pageerror event monitoring | No exceptions on checked pages |
| Visual review | Two screenshots in artifacts/ | Navigation, tables, code, and text layout checked |

### Browser check

Start a loopback preview, then run:

```sh
uv run --python .venv/bin/python --with playwright python scripts/check_preview.py
```

The script defaults to http://127.0.0.1:8000/. Set GUIDE_PREVIEW_URL to another local URL if that port is occupied. It currently uses the macOS Google Chrome executable path. For another OS, change the browser path or install a browser following Playwright's official instructions.

Screenshots are regenerated for the English edition:

- [Desktop](artifacts/preview-desktop.png)
- [Mobile](artifacts/preview-mobile.png)

### Corrections during original verification

- Saved templates as .md.txt so the site serves raw text; documented removing .txt when saving.
- Changed the browser navigation wait from networkidle to load because live-reload traffic continues.
- Waited for search initialization before entering a query and then waited for visible results.

## Limitations and checks not performed

- Official product documentation was researched, but subscriptions, student verification, and hands-on operation of the five products were not tested.
- Account-specific regional checkout prices, student eligibility, and renewal terms are unverified.
- Grok Build's free allowance and extra Antigravity allowance through Google's student offer remain unverified in the guide.
- No hands-on Windows / Linux execution or assistive-technology accessibility review.
- No comprehensive external-link monitoring.
- Material prints an advisory about MkDocs 2.0 on startup; this project uses pinned MkDocs 1.6.1.
- At the time of the initial and English-edition checks, no GitHub Pages configuration, workflow execution, remote creation, push, or external publication had been performed. See the publication update below.
- The draft workflow remains at deployment/pages.yml.example, outside GitHub Actions' active workflow path.

## Repository upload and deployment attempt

- Uploaded the guide and manual Pages workflow to jkoba0512/ai-development-guide, branch main.
- Local internal-link checks, all 9 sample tests, and the strict build passed.
- GitHub rejected Pages activation with HTTP 422: the current plan does not support GitHub Pages for this private repository.
- At this attempt, no website had been deployed. Publication awaited the owner's repository visibility or plan decision.

## Publication verification

- The owner changed the repository to public; public visibility was confirmed through the GitHub API.
- Enabled GitHub Pages with build_type=workflow and HTTPS enforced.
- Published https://jkoba0512.github.io/ai-development-guide/.
- Initial successful deployment: https://github.com/jkoba0512/ai-development-guide/actions/runs/38858349854.
- GitHub Actions passed dependency installation, internal-link checks, all 9 sample tests, strict build, artifact upload, and deployment.
- Ran scripts/check_preview.py against the public URL: all 17 pages and 9 static assets returned HTTP 200.
- Confirmed English search, dark mode, mobile layout, and no JavaScript page errors.
- Refreshed the desktop/mobile screenshots from the live site.
- Updated README and site maintenance instructions to reflect publication.
- Product pricing research remains dated 2026-10-06; deployment did not include a new product-terms review.

## Getting-started sequence revision

- Replaced the reading list with an ordered getting-started workflow: choose a tool, install and sign in, prepare the folder and records, open the folder or start the CLI, run first checks, build the practice project, and hand off only when needed.
- Updated all five tool pages with matching stages and return links to common setup.
- Added explicit app/editor folder-opening instructions and CLI login/startup commands, with working-directory guidance.
- Clarified Python prerequisites, optional Git, and preparing all six records with a text editor before the first agent task.
- Updated the practice project to use the existing folder and records rather than an empty new folder.
- Reopened official setup/CLI documentation to check authentication steps. Product pricing findings retain the original verification date.
- Internal-link and section-anchor checks passed for all 17 pages; strict build passed.
- Local browser checks passed for 17 pages, 9 static assets, English search, dark mode, and mobile layout.
- Clicked all 8 getting-started links and all 5 tool routes in the local browser; destination URLs and section IDs matched.
- Refreshed preview screenshots and reviewed the homepage layout.

## Tool-independent working instructions

- Replaced the shared AGENTS.md template with WORKING_RULES.md, an ordinary Markdown project document.
- Updated specification, implementation, first-run, practice, and handoff prompts, along with tool pages and the downloadable handoff template.
- Documented explicit reading, attachments, and pasted text, including what to do when a required document is unavailable.
- Kept product instruction files only as optional adapters; added migration guidance for existing practice folders.
- Updated template-presence checks and the browser-check download route.
- Local internal-link checks and strict build passed.
- Local browser verification passed for all 17 pages, 9 assets including the new template, English search, dark mode, and mobile layout.
- Refreshed preview screenshots. Product access and pricing findings were not changed.

## Working-rules reminder links

- Added explanation, setup, and download links beside shared working-rules references across the guide.
- Kept copyable prompts and folder trees plain; placed reference links immediately before them.
- Included absolute guide links in the downloadable handoff template so they remain usable outside the site.
- Internal file/section-link checks and the strict build passed.

## Specification exercise explanation

- Rewrote the specification page as a guided exercise with a clear purpose and saved deliverable.
- Defined CLI, exit code, standard error, acceptance criterion, and boundary checks in context.
- Explained the 25-and-50 example calculation and the distinction between criteria and tests.
- Added actions for drafting, reviewing, saving, and later executing checks, plus a readiness checklist.
- Preserved working-rules reference links and existing section anchors.
- Internal-link checks and strict build passed. No sample implementation changed.

## Beginner-facing project document explanations

- Added concrete contents examples for the specification and decision record, explaining what each file is for.
- Explained Markdown as editable text and distinguished project documents from executable programs.
- Described the first exercise by its actual file and output rather than unexplained smoke-check terminology.
- Explained how to provide project instructions to the AI and what each reference link does.
- Replaced terse working-rules link labels across the guide with descriptive labels.
- Internal-link checks and the strict build passed.

## Python and uv environment setup — 2026-10-18

- Added an English Python/uv setup manual and linked it from getting started, common setup, tool pages, and practice.
- Described Python as the language for this guide's exercises, without asserting language requirements for all System Design assignments.
- Standardized student execution on uv run --locked and documented Python 3.12, isolated environments, lockfiles, dependencies, offline runs, and handoffs.
- Added pyproject.toml, .python-version, and uv.lock for this website; preserved all 29 previously verified package versions. requirements.txt is now a compatibility export.
- Converted both active and draft Pages workflows to uv installation, locked synchronization, checks, tests, and build.
- Verified the documented student flow in the Git-ignored .local-checks/uv-student folder using uv 0.11.1 and Python 3.12.11: initialization, version pinning, sync, environment path, one-line execution, offline startup program, normal/invalid CLI inputs, and all 9 reference tests passed.
- The isolated student project declares no third-party dependencies.
- uv sync --locked, internal links (18 pages and 6 templates), and uv-based strict build passed for the website.
- Browser verification passed: 18 pages, 9 static assets, English search, dark mode, and mobile layout; no JavaScript page errors.
- Replaced a fixed browser delay with a search-initialization readiness check after an initial timing-related failure.
- OS-specific installer instructions were checked against official Astral documentation; a fresh uv install and native Windows student setup were not executed. No system Python installation was removed.

## Keep requirements and reasons together

- Merged decision notes into SPEC.md with a Decisions and reasons section and an example.
- Updated setup, prompts, handoffs, templates, and checks to use five shared records.
- Kept the old decision-template URL available with migration instructions.
- Relative-link checks and the strict MkDocs build passed.

## Explain tool-specific instruction files

- Added an official-source comparison for all five tools and corrected the Codex filename to AGENTS.md.
- Explained explicit shared-rule delivery, optional tool-specific pointers, and Claude Code imports without assuming cross-tool import syntax.
- Added discovery links from setup, specification, tool pages, and handoffs. No instruction files were created in the guide repository.
- Official-document review covers instruction discovery only, not pricing or student benefits.

## Simplify verification records

- Made AI execution and concise AI-written verification summaries the default. Students review results, failures, and checks not run.
- Retained manual execution and copyable summaries for interfaces without execution or file access.
- Updated first-run checks, practice, implementation, specification, environment guidance, and shared templates.
- Grouped checks are allowed; relevant failure evidence and honest not-run status remain required.

## Make verification recording optional

- Removed VERIFICATION.md from required setup, folder trees, reading prompts, and completion criteria.
- Default workflow displays checks and actual results in the conversation for student review.
- Saving or updating results requires a user request or agreement; AI recommendations explain why and ask first.
- Retained an optional template and updated handoffs to read saved results only if supplied, otherwise rerun checks.
- Relative links and the strict MkDocs build passed; the optional download remains available.

## Remove unnecessary recording explanations

- Removed the Optional verification record section and the specification-page paragraph about creating files or transcribing output.
- Removed links to the deleted section and shortened repeated recording explanations.
- Kept a brief instruction to review displayed results and request a saved summary if wanted.

## Optional Obsidian extension

- Added an English extension after the basic practice, separate from required setup.
- Explained opening the existing project as a vault, reviewing an AI handoff, and sharing selected Markdown files.
- Kept plugins/automation outside the introduction and verification saving optional.
- Added official storage, vault, linking, and pricing sources reviewed on 2026-10-19.
- Updated navigation, related-page links, and preview coverage for 19 pages.
- Relative-link checks, strict build, and local browser checks passed (19 pages, search, dark mode, mobile layout, no page errors).

## Clarify the specification exercise flow

- Reorganized the page into five actions: understand the task, request a draft, review requirements/reasons, check acceptance criteria, and save the agreed file.
- Removed duplicate preview documents and instructions to write requirements manually before requesting an AI draft.
- Kept concrete examples, all five acceptance criteria, uv usage, and a clear next step.
- Preserved earlier section URLs with anchor markers. Verification results remain displayed in conversation, with saving by request.
- Relative links, strict build, and local browser checks of the five steps, existing anchors, and mobile layout passed.

## Full student-progression review — 2026-10-19

Read all 19 pages and the downloadable templates and sample code. This was an editorial and executable-workflow review, not a fresh product pricing review or a student usability study.

| Pages reviewed | Findings and changes |
| --- | --- |
| Introduction, costs | Separated the first completion point from optional handoffs; explained choosing one accessible route without claiming every student offer |
| Five tool pages | Clarified the transition into Common setup and the exact return to folder-opening; kept existing product setup mechanics and dated official references |
| Common setup, Python/uv | Added terminal/working-directory explanations, staged file preparation, explicit return points, and a short AI-assisted environment note after execution |
| Specification | Kept the five-step lesson; clarified permission to save and the transition to code review before execution |
| Implementation, practice | Removed duplicated specification writing and premature tests; used practice as the route page, split code review from execution, and explained exit code 2 and zero-test output |
| Permissions, troubleshooting | Explained unfamiliar terms at use and separated website-maintenance troubleshooting from student commands |
| Templates, handoffs | Reduced template burden; introduced HANDOFF.md only at a chosen move, provided a short creation prompt, and clarified reusing versus recreating uv environments |
| Obsidian | Adjusted the example for students who have not created a handoff yet; kept this an optional extension |
| Maintenance, official sources | Marked site build/publication as maintainer work and retained original product verification dates |

The initial documents are SPEC.md and the shared working rules. ENVIRONMENT.md is prepared after first-run checks; HANDOFF.md at an actual handoff. Verification results remain displayed in conversation and are saved only when requested or agreed. Git, additional AI tools, Obsidian, and website publication are outside the first-project requirement.

Validation results:

- Internal navigation, relative links, downloadable templates, and the strict MkDocs build passed.
- Browser checks passed for all 19 pages at desktop and mobile widths, all 8 referenced static assets, search indexing, English search, dark mode, and absence of page errors.
- Created a fresh isolated uv project using the documented init/pin/sync sequence. The Python environment checks and smoke.py command passed without extra dependencies.
- The reference CLI produced the expected outputs for 25/50, 0, and 1440, and rejected all five documented invalid-input cases with exit code 2. All 9 automated tests passed.
- Transferred code and environment descriptions without .venv, recreated the environment with uv, and passed all 9 tests again.
- No VERIFICATION.md or premature HANDOFF.md was required by the initial workflow. The handoff file was introduced only for the transfer check.
- Command execution was tested on macOS. Fresh Windows/Linux installations, actual five-product permissions, student access outcomes, and a live student usability trial remain untested.
