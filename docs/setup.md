# Common Setup and First-Run Checks

**Start here after installing and signing in to one AI development tool.** On this page you will prepare a folder, give the AI its instructions, and check that it can help you create and run one small program.

Follow the sections in order. After each linked setup task, return to the place indicated below. If you have not installed a tool, choose one from [Getting started](index.md#choose-your-tool-page).

## Prepare a working folder

Follow [Set up Python with uv](python-uv.md) through **Check that Python runs**. This creates the `ai-practice` folder and checks its Python environment. Then return to [Prepare your records](#prepare-your-records) below.

If you already completed that environment check, continue below; keep using the same folder.

## Prepare your records

Start with **two Markdown files** in `ai-practice`. Markdown (`.md`) is editable text with headings and lists. Use the text editor in your chosen development tool, or another plain-text editor.

1. Create `SPEC.md` and paste this starting description:

    ```markdown
    # First-run check

    Create a Python file named smoke.py that prints Ready for AI development.
    Use the existing uv environment, without extra packages or network operations in the program.
    ```

2. Save the [working-rules template](assets/templates/WORKING_RULES.md.txt) as [WORKING_RULES.md](templates.md#tool-independent-working-rules) in the same folder. Remove the final `.txt` from the download name, and read its contents. References: [How to save the file](#prepare-your-records) · [What the rules mean](templates.md#tool-independent-working-rules).

If a download opens as text in your browser, use **Save as**, or copy the text into a new editor file. Check the saved filename: it should end in `.md`, not `.md.txt` or `.md.txt.txt`. “Project root” means the top level of `ai-practice`, alongside `pyproject.toml`.

Your starting folder should contain:

Project instructions: [Explanation](templates.md#tool-independent-working-rules) · [Setup](#prepare-your-records) · [Rules template](assets/templates/WORKING_RULES.md.txt).

```text
ai-practice/
├── SPEC.md
├── WORKING_RULES.md
├── pyproject.toml
├── .python-version
├── uv.lock
├── .venv/
├── src/
└── tests/
```

SPEC.md describes **what to build**. The working rules tell the AI **how to work**. [Shared templates](templates.md) also provides environment and handoff files for later stages; prepare them when you reach those stages.

## Open the folder or start the CLI

An app uses a folder selector. A **CLI** (command-line interface) starts from a terminal. Choose only the row for the tool you installed:

| Your tool | Open the project and set permissions |
| --- | --- |
| Antigravity | [Open the practice folder](tools/antigravity.md#open-the-practice-folder) |
| GitHub Copilot in VS Code | [Open the practice folder](tools/copilot.md#open-the-practice-folder) |
| Codex app or CLI | [Open the practice folder](tools/codex.md#open-the-practice-folder) |
| Grok Build | [Open the practice folder](tools/grok-build.md#open-the-practice-folder) |
| Claude Code | [Open the practice folder](tools/claude-code.md#open-the-practice-folder) |

**Read that section, open only `ai-practice`, set its permissions, then return to [Run the first-run checks](#run-the-first-run-checks) below.** Keep personal documents and unrelated folders outside the project.

For a CLI, navigate to `ai-practice` before starting the agent. If the terminal is in the folder containing it, enter `cd ai-practice`. If it is elsewhere, use the full path, quoted if it contains spaces. Check the current folder with `pwd` on macOS/Linux or `Get-Location` in PowerShell. See [terminal basics](python-uv.md#before-you-type-commands) if this is unfamiliar.

[Tool-specific instruction filenames](templates.md#tool-specific-instruction-files), such as CLAUDE.md or AGENTS.md, are explained separately. Here, explicitly ask the AI to read the shared rules rather than assuming automatic loading.

## Run the first-run checks

You are ready when your tool is signed in, Python runs through uv, and the two starting files are saved in `ai-practice`.

### Reading

Send this request in your AI conversation:

Project instructions: [Explanation](templates.md#tool-independent-working-rules) · [Setup](#prepare-your-records) · [Rules template](assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md and SPEC.md in this project, or the contents I provide.
If you cannot access either, ask me to attach or paste it.
Explain what the first-run program should do and which folder we are using.
Do not modify files or run commands yet.
```

Check that the reply describes the print-only program and the correct folder. If the tool cannot access local files, attach the documents or paste their contents, then ask again.

### A small edit

Switch from reading-only / Plan mode to the approval-based editing mode described on your tool's setup page. If this restarts the session, provide the starting files again and repeat the reading request. Then send:

```text
Create smoke.py in the project root. It should print "Ready for AI development".
Use Python without external packages or network operations in the program.
Keep pyproject.toml, uv.lock, and .python-version unchanged.
Show the file's contents before running it.
```

Open the file and check that it prints the requested message. If the tool cannot save files, copy its proposed code into `ai-practice/smoke.py` yourself.

### Execution by the AI tool

Ask the AI to run this command from `ai-practice` and display the actual result. Review the command and folder before approving execution:

```sh
uv run --locked python smoke.py
```

Expected output:

```text
Ready for AI development
```

If the tool cannot execute commands, run this in your terminal and paste the result into the conversation. Ask it to explain any error. See [Troubleshooting](troubleshooting.md) rather than widening permissions without understanding the problem.

**Checkpoint:** you have checked reading, editing, and execution. Save results only if you want a summary later.

### Keep a short environment note

ENVIRONMENT.md tells your future self or another AI how to run this project. Ask the AI to prepare it after the checks:

```text
Create a short ENVIRONMENT.md with the OS, uv and Python versions,
chosen AI tool/interface, practice folder, and the command used to run smoke.py.
Use only observed details or information I provide. Mark unknowns as unknown.
Ask me which account access type I use: free, student, institutional, or paid.
Do not include account names, keys, or other secrets.
```

Review the note. If the tool cannot save it, copy the summary into `ai-practice/ENVIRONMENT.md`. The [environment template](assets/templates/ENVIRONMENT.md.txt) is available if useful; fill only what applies.

## Continue to the practice project

**Next: [Practice project](practice.md).** Keep the same folder, tool, and Python environment. You will replace the small first-run specification with the study-time program's requirements.

Later, use [Handoffs](workflow/handoff.md) when changing conversations, tools, or computers. That is when HANDOFF.md becomes useful.

## Local and cloud environments differ

This exercise uses files on your computer. A cloud agent runs elsewhere and needs the intended files supplied separately. If you use one later, check which repository and files it receives, then verify its changes locally. See [Safe permission settings](workflow/permissions.md).

Git is optional for this exercise. If you choose it later, follow the [environment file guidance](python-uv.md#keep-local-environment-files-out-of-git) before adding files. Publishing this guide is covered separately for maintainers in [Local checks and publication](maintenance.md).
