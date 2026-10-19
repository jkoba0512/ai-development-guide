# Handoffs Between Environments

**Use this optional lesson when changing conversations, AI tools, or computers.** A handoff gives the next person or AI enough information to continue. You can try it with a new conversation in the same tool; installing another tool is unnecessary.

If you are still building your first program, finish the [Practice project](../practice.md) first.

## Shared foundation

Keep the files that describe the project together:

| File | What the next conversation learns |
| --- | --- |
| SPEC.md | Agreed requirements, acceptance criteria, and reasons for important choices |
| src/ and tests/ | The program and its automated checks |
| pyproject.toml, .python-version, uv.lock | How to recreate the Python environment |
| ENVIRONMENT.md, if available | Your tool, runtime, permissions, and startup commands |
| HANDOFF.md | Current state and the next task; create it below when needed |

Provide the shared [WORKING_RULES.md](../templates.md#tool-independent-working-rules) ([Setup](../setup.md#prepare-your-records) · [Rules template](../assets/templates/WORKING_RULES.md.txt)) too. Explicitly give the next agent file access, attachments, or pasted contents. [Tool-specific instruction files](../templates.md#tool-specific-instruction-files) can point to the common rules.

## Before moving

Ask the current AI to prepare a short handoff:

```text
Create or update HANDOFF.md for the next conversation.
Include the objective, current code state, unresolved questions, and next task.
Refer to SPEC.md for requirements and reasons instead of duplicating them.
State which folder contains the code and how to run it.
Reference saved verification results only if I previously requested or agreed to saving them.
Otherwise say that checks should be rerun at the destination.
Do not invent decisions or test results. Show the note for me to review.
```

Read the note and correct anything inaccurate. The [handoff template](../assets/templates/HANDOFF.md.txt) is available if useful. Let the first agent finish or stop it before another agent edits the same files.

## Transfer methods

| Where you are moving | What to do |
| --- | --- |
| New conversation or tool on the same computer | Open the same ai-practice folder |
| Another computer | Transfer the project files using your approved method; exclude .venv |
| A shared Git repository, if you use Git | Commit the intended files, review them, then push to the agreed destination; clone or pull at the destination |
| A cloud agent | Supply only the intended project files and check its runtime and permissions |
| Back from a cloud agent | Retrieve its changes, review them, and rerun checks locally |

A local folder does not automatically appear in a cloud agent. With Git, a push sends committed history, not unsaved or uncommitted changes. Keep secrets and unrelated files out of the transfer.

## After moving

Open the project in the destination tool and send:

Project instructions: [Explanation](../templates.md#tool-independent-working-rules) · [Setup](../setup.md#prepare-your-records) · [Rules template](../assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md, SPEC.md, and HANDOFF.md from the files or contents I provide.
Also read ENVIRONMENT.md and saved verification results if supplied.
Ask for required content you cannot access; do not assume it was read.
Summarize the objective, code state, open questions, and next task.
Point out contradictions between requirements and code.
Do not edit files or run commands until I have reviewed the summary.
```

Check the summary before continuing. Configure permissions for this session; they may differ from the earlier one.

If you use the **same folder on the same computer**, keep its existing uv environment. For a **different computer or a new project copy**, install uv, open a terminal in the transferred folder, and run:

```sh
uv python install
uv sync --locked
```

After reviewing the code, ask the AI to rerun the tests:

```sh
uv run --locked python -m unittest discover -s tests -v
```

Run this only after tests exist and check that it ran more than zero tests. Review the displayed results. If setup fails, see [Python and uv troubleshooting](../python-uv.md#troubleshooting) before changing requirements.

## Ready to resume

You are ready when the next AI can explain the task from the files, the checks run in the destination environment, and the next change is clear. Update ENVIRONMENT.md if the environment changed. Work with one writer at a time on shared files.

For an optional way to organize these documents, see [Organize project knowledge with Obsidian](../obsidian.md).
