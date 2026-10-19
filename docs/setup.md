# Common Setup and First-Run Checks

Use this page **after installing your chosen development tool and signing in**. You only need one tool. If you have not installed it yet, return to [Getting started](index.md#getting-started) and follow its tool setup page through **Install and sign in**.

A command-line interface (CLI) is started by typing a command in a terminal. An app or editor uses a project or folder selector.

Here, “your development tool” means the app, editor, or CLI you selected: Antigravity, Grok Build, GitHub Copilot in VS Code, Codex, or Claude Code.

## Prepare a working folder

This guide's first-run exercise and practice project use **Python 3.12 managed with uv**. Follow [Set up Python with uv](python-uv.md) now. It explains how to install uv and Python, create a separate `ai-practice` folder, prepare its environment, and check execution.

If you already created the folder, follow the manual's [existing-project instructions](python-uv.md#create-the-practice-project) instead of creating it again. Return here after the environment check. You do not need an AI agent to perform these steps.

### Check Python for the practice example

From the prepared `ai-practice` folder, run:

```sh
uv --version
uv run --locked python --version
```

The second command should show Python 3.12.x. Follow the [environment manual](python-uv.md#check-that-python-runs) if it fails. Installing an AI tool does not prepare this Python environment automatically.

Git is optional. If using it, verify `git --version`. Record uv, Python, OS, shell, and tool versions once ENVIRONMENT.md is ready.

## Prepare your records

Save the four core files from [Shared templates](templates.md) into `ai-practice`. Each download ends in `.md.txt`: remove the final `.txt` so, for example, `SPEC.md.txt` becomes `SPEC.md`.

Use a text editor to fill in the starting records; the AI tool does not need to be running yet.

- **SPEC.md:** write “First-run check: create a Python script that prints Ready for AI development. No external packages or network access.” Keep important choices and their reasons in the same file.
- **ENVIRONMENT.md:** record the environment, selected tool/interface, account access type, and available permission settings. Do not include secret values.
- **HANDOFF.md:** set the next task to “Complete the reading, editing, and execution checks.”
- **[WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)):** read and keep the shared working rules.

Your folder should now look like this:

Project instructions for the AI: [What the working rules mean](templates.md#tool-independent-working-rules) · [How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt).

```text
ai-practice/
├── SPEC.md
├── ENVIRONMENT.md
├── HANDOFF.md
├── WORKING_RULES.md
├── pyproject.toml
├── .python-version
├── uv.lock
├── .venv/
├── src/
└── tests/
```

If using Git, initialize with `git init` from this folder. Create a `.gitignore` to exclude secrets before adding files. Review `git status` and `git diff`, then stage only the intended files and make your first commit. You do not need a GitHub account or a push to use Git locally.

## Open the folder or start the CLI

**Open the `ai-practice` folder in your chosen development tool. If you use a command-line tool, navigate to that folder before starting it.** Do not select your entire home directory or a parent folder containing unrelated files.

| Interface | What to do | Detailed instructions |
| --- | --- | --- |
| Antigravity app / IDE | Create or open a project containing only ai-practice, then start a local conversation | [Antigravity](tools/antigravity.md#open-the-practice-folder) |
| GitHub Copilot in VS Code | Open ai-practice with File → Open Folder, then open Copilot Chat | [Copilot](tools/copilot.md#open-the-practice-folder) |
| Codex desktop app | Open or add ai-practice as the local project, then start a conversation | [Codex](tools/codex.md#open-the-practice-folder) |
| Grok Build CLI | Enter ai-practice in the terminal, then start grok with limited permissions | [Grok Build](tools/grok-build.md#open-the-practice-folder) |
| Codex CLI | Enter ai-practice, then start codex with read-only permissions | [Codex](tools/codex.md#open-the-practice-folder) |
| Claude Code CLI | Enter ai-practice, then start claude and select Plan mode | [Claude Code](tools/claude-code.md#open-the-practice-folder) |

For a new terminal, first locate the folder. From the directory containing `ai-practice`, run `cd ai-practice`. From elsewhere, use its full path, quoted if it contains spaces. If already inside it, skip that command. Check the working directory with `pwd` on macOS/Linux or `Get-Location` in PowerShell.

Follow the linked tool instructions to start the session and set permissions **before sending the first request**. Confirm that its project/folder display points to `ai-practice`. [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) is an ordinary project document with no assumed automatic loading. Explicitly ask the tool to read it. If the interface cannot access local files, attach or paste its contents and the requested project records before sending the task.

For an explanation of filenames such as CLAUDE.md, AGENTS.md, and .github/copilot-instructions.md, see [Tool-specific instruction files](templates.md#tool-specific-instruction-files). They are optional for this exercise; keep using the explicit reading request below.

## Run the first-run checks

Before starting, confirm that:

- [ ] Your chosen tool is installed and signed in with the intended account.
- [ ] The [Python and uv environment check](python-uv.md#check-that-python-runs) passes in ai-practice.
- [ ] The four core files are saved under ai-practice.
- [ ] The tool is open in that folder, with reading-first permissions.
- [ ] No paid subscription is needed for your selected free route; any paid route was chosen deliberately.

### Reading

Send this request in the conversation you just opened:

Project instructions for the AI: [What the working rules mean](templates.md#tool-independent-working-rules) · [How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt).

```text
Read the project working rules (WORKING_RULES.md) and SPEC.md, using the local files
or the contents I have attached or pasted. If either is unavailable, ask me to provide it.
Then explain the purpose and file structure.
Do not modify files, install dependencies, or publish anything at this stage.
Report the name of any file you could not read and the reason.
```

Compare the response with the actual files. A text response does not establish that editing or execution works.

### A small edit

Once reading works, switch from reading-only / Plan mode to the tool's approval-based editing mode, as described on its setup page. Allow changes inside `ai-practice`, then request:

```text
Create only smoke.py. It should print "Ready for AI development" when run.
Use Python without external packages or network access.
Run Python through uv, using the existing project environment.
Do not change pyproject.toml, uv.lock, or .python-version for this task.
After writing the file, show its contents and explain how to run it.
```

Read the change. Then ask the AI to run the following command from `ai-practice` and display its actual result in the conversation. Review the command and working directory before approving it:

```sh
uv run --locked python smoke.py
```

This command is the same on macOS, Linux, and Windows PowerShell.

Expected output: `Ready for AI development`. Read the result on screen. Saving an execution record is optional: ask for one if you need it. If the AI thinks a record would help, it should explain why and ask before saving.

### Execution by the AI tool

The AI normally performs the execution above and displays the result. If execution is unavailable with your tool or settings, run the command yourself and paste the output into the conversation. Ask the AI to explain it and identify it as “executed by a person.” A permissions error does not require unrestricted access.

If your selected interface cannot edit local files, use its proposed code to create smoke.py yourself and tell the AI that you performed the edit. You can complete the learning exercise without purchasing another plan.

## Continue to the practice project

After reading, editing, and execution have been checked, continue to the [Practice project](practice.md). Replace the specification for the small `smoke.py` startup exercise with the agreed study-time CLI specification there. If you chose to save results, keep the earlier check distinguishable from the new project.

A [handoff](workflow/handoff.md) is useful later when you change conversations, tools, or computers. You do not need to switch tools during the first exercise.

## Local and cloud environments differ

This initial flow uses a local folder. Local files do not automatically appear in a cloud environment. Before using cloud integration, check the repository, branch, files being sent, and runtime. Use a project without secrets, then verify imported changes again locally.

“Installed,” “signed in,” “opened the folder,” “read files,” “edited files,” and “executed code” are separate milestones. See [Safe permission settings](workflow/permissions.md).
