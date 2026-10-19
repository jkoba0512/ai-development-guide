# Antigravity

This page follows the [Getting started](../index.md#getting-started) sequence: install and sign in → prepare a folder → open it → run the first checks. Follow only the page for your chosen tool.

The official documentation describes app, IDE, and CLI entry points. This walkthrough uses the local app / IDE route. If your interface differs, select its tab in [official Getting started](https://antigravity.google/docs/getting-started).

## Install and sign in

1. Review [Costs and student benefits](../plans.md). Individual access has a free option with usage limits.
2. Download the version for your OS from the [official download page](https://antigravity.google/download), checking system requirements.
3. Install and launch the app.
4. Follow the authentication prompts and sign in with the intended Google account. Follow school restrictions.
5. Stop before starting an agent task. You will choose the project folder after preparing it below.

**Checkpoint:** the app opens and shows your signed-in account. Installation and sign-in are not yet a file-reading or execution check. Source: [Official setup](https://antigravity.google/docs/getting-started).

## Prepare the practice folder

If you reached this page from Common setup to open an existing project, skip to [Open the practice folder](#open-the-practice-folder).

Follow [Common setup](../setup.md#prepare-a-working-folder) in order: it covers [Python with uv](../python-uv.md), the `ai-practice` folder, and [starting files](../setup.md#prepare-your-records). When you reach Common setup’s folder-opening step, return directly to [Open the practice folder](#open-the-practice-folder) below.

## Open the practice folder

1. In Antigravity, create or open a project.
2. Use Add Folder or the equivalent folder selector to choose **only `ai-practice`**.
3. Check the project folder path.
4. Start a **Local** conversation in that project. For the first exercise, use the existing folder. If choosing a Git worktree later, confirm its separate editing location.

See [official project setup](https://antigravity.google/docs/getting-started).

### Set permissions before the first request

Select Request Review in project permissions. In the IDE, also use Request Review for terminal auto-execution and enable artifact review. Restrict access outside the project and enable Terminal Sandbox where supported. Names differ by OS and interface. [Official settings](https://antigravity.google/docs/settings).

For this tool's instruction-file names and how they relate to the shared rules, see [Tool-specific instruction files](../templates.md#tool-specific-instruction-files). Automatic discovery is optional for this exercise.

## Run the first-run checks

Continue to [Run the first-run checks](../setup.md#run-the-first-run-checks). Ask the agent to read [WORKING_RULES.md](../templates.md#tool-independent-working-rules) ([How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt)) and SPEC.md first. Review plans and artifacts before applying them; permit folder-scoped edits only for the editing check.

If browser operation becomes necessary, use a practice page and dedicated profile, avoiding pages signed in to personal accounts.

## Continue development

After the checks, follow the [Practice project](../practice.md). Save the specification in SPEC.md and implement small acceptance criteria. When preparing a handoff later, ask the AI to summarize the next task in HANDOFF.md.

When you later change tools, check the actual edited folder and diff and transfer code together with any verification results you chose to save. See [Handoffs](../workflow/handoff.md).
