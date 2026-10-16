# Common Setup and First-Run Checks

Use this page **after installing your chosen development tool and signing in**. You only need one tool. If you have not installed it yet, return to [Getting started](index.md#getting-started) and follow its tool setup page through **Install and sign in**.

A command-line interface (CLI) is started by typing a command in a terminal. An app or editor uses a project or folder selector.

Here, “your development tool” means the app, editor, or CLI you selected: Antigravity, Grok Build, GitHub Copilot in VS Code, Codex, or Claude Code.

## Prepare a working folder

Create an `ai-practice` folder separate from personal documents and secrets. At this stage, use your file manager or terminal; you do not need an AI agent to create the folder. The folder where terminal commands run is called the working directory.

Choose a location you can find again. Open a terminal in that location, then run:

=== "macOS / Linux"
    ```sh
    mkdir ai-practice
    cd ai-practice
    mkdir src tests
    ```

=== "Windows PowerShell"
    ```powershell
    mkdir ai-practice
    cd ai-practice
    mkdir src, tests
    ```

If the folder already exists, open it instead of creating it again. These commands leave the terminal inside `ai-practice`; do not repeat `cd ai-practice` from inside it.

### Check Python for the practice example

The smoke check and practice project use Python 3.11 or later. In your terminal, run:

=== "macOS / Linux"
    ```sh
    python3 --version
    ```

=== "Windows PowerShell"
    ```powershell
    py -3 --version
    ```

If Python is missing or too old, use your school's approved installation method or the [official Python downloads](https://www.python.org/downloads/), reopen the terminal, and check the version again. Installing an AI tool does not necessarily install Python.

Git is optional for the first checks. If using it, verify `git --version`. Record the OS, shell, Python version, and selected tool version once ENVIRONMENT.md is ready.

## Prepare your records

Save the six files from [Shared templates](templates.md) into `ai-practice`. Each download ends in `.md.txt`: remove the final `.txt` so, for example, `SPEC.md.txt` becomes `SPEC.md`.

Use a text editor to fill in the starting records; the AI tool does not need to be running yet.

- **SPEC.md:** write “First-run check: create a Python script that prints Ready for AI development. No external packages or network access.”
- **ENVIRONMENT.md:** record the environment, selected tool/interface, account access type, and available permission settings. Do not include secret values.
- **VERIFICATION.md:** leave results marked as not run until you execute them.
- **HANDOFF.md:** set the next task to “Complete the reading, editing, and execution checks.”
- **[WORKING_RULES.md](templates.md#tool-independent-working-rules) ([setup](setup.md#prepare-your-records) · [template](assets/templates/WORKING_RULES.md.txt)):** read and keep the shared working rules.
- **DECISIONS.md:** leave it ready for later decisions.

Your folder should now look like this:

Working rules: [explanation](templates.md#tool-independent-working-rules) · [setup](setup.md#prepare-your-records) · [template](assets/templates/WORKING_RULES.md.txt).

```text
ai-practice/
├── SPEC.md
├── ENVIRONMENT.md
├── VERIFICATION.md
├── HANDOFF.md
├── WORKING_RULES.md
├── DECISIONS.md
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

Follow the linked tool instructions to start the session and set permissions **before sending the first request**. Confirm that its project/folder display points to `ai-practice`. [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([setup](setup.md#prepare-your-records) · [template](assets/templates/WORKING_RULES.md.txt)) is an ordinary project document with no assumed automatic loading. Explicitly ask the tool to read it. If the interface cannot access local files, attach or paste its contents and the requested project records before sending the task.

## Run the first-run checks

Before starting, confirm that:

- [ ] Your chosen tool is installed and signed in with the intended account.
- [ ] Python 3.11 or later is available.
- [ ] The six records are saved under ai-practice.
- [ ] The tool is open in that folder, with reading-first permissions.
- [ ] No paid subscription is needed for your selected free route; any paid route was chosen deliberately.

### Reading

Send this request in the conversation you just opened:

Working rules: [explanation](templates.md#tool-independent-working-rules) · [setup](setup.md#prepare-your-records) · [template](assets/templates/WORKING_RULES.md.txt).

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
After writing the file, show its contents and explain how to run it.
```

Read the change. Open a terminal in `ai-practice`, or use the editor's integrated terminal and confirm its working directory. Run:

=== "macOS / Linux"
    ```sh
    python3 smoke.py
    ```

=== "Windows PowerShell"
    ```powershell
    py -3 smoke.py
    ```

Expected output: `Ready for AI development`. Record the directory, command, output, and pass/fail result in VERIFICATION.md.

### Execution by the AI tool

Ask the AI to run the same command. Review the command and working directory before approving it. If execution is unavailable with your tool or settings, record “executed by a person.” A permissions error does not require unrestricted access.

If your selected interface cannot edit local files, use its proposed code to create smoke.py yourself and record that you performed the edit. You can complete the learning exercise without purchasing another plan.

## Continue to the practice project

After reading, editing, and execution have been checked and recorded, continue to the [Practice project](practice.md). Replace the smoke-check specification with the agreed study-time CLI specification there. Keep verification history so the two checks are distinguishable.

A [handoff](workflow/handoff.md) is useful later when you change conversations, tools, or computers. You do not need to switch tools during the first exercise.

## Local and cloud environments differ

This initial flow uses a local folder. Local files do not automatically appear in a cloud environment. Before using cloud integration, check the repository, branch, files being sent, and runtime. Use a project without secrets, then verify imported changes again locally.

“Installed,” “signed in,” “opened the folder,” “read files,” “edited files,” and “executed code” are separate milestones. See [Safe permission settings](workflow/permissions.md).
