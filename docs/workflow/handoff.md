# Handoffs Between Environments

Use shared files to make work reproducible across conversations, tools, computers, and local/cloud environments. Tool-specific chat history is supporting material.

## Shared foundation

| Source of truth | Purpose |
| --- | --- |
| SPEC.md | Purpose, inputs, outputs, acceptance criteria, exclusions, and important decisions with their reasons |
| src/ and tests/ | Actual code and verification methods |
| pyproject.toml, .python-version, and uv.lock | Python environment settings and resolved dependencies; exclude .venv |
| VERIFICATION.md | What ran, where, by whom, and with what result |
| ENVIRONMENT.md | OS, versions, dependencies, startup commands, and permissions |
| HANDOFF.md | Current state, unfinished work, and the next single task |
| [WORKING_RULES.md](../templates.md#tool-independent-working-rules) ([How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt)) | Shared working rules and reading order |

[WORKING_RULES.md](../templates.md#tool-independent-working-rules) ([How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt)) is a tool-independent project document. Explicitly provide it and the other records by file access, attachment, or pasted text; no automatic loading is assumed. **Ask the tool to summarize the supplied documents before proceeding.**

[Tool-specific instruction files](../templates.md#tool-specific-instruction-files), such as AGENTS.md or CLAUDE.md, are optional adapters. If you use one, keep only references to the shared documents and avoid maintaining a second set of project rules. None is required to follow this guide.

## Before moving

1. Stop running agents and background tasks.
2. Review diffs and check that SPEC.md matches the code.
3. Update verification records, separating failures from checks not run.
4. Record the current state and next single task in HANDOFF.md.
5. With Git, commit or preserve uncommitted changes. Record the branch and commit reference.
6. Check that the transferred files contain no secrets.

If HANDOFF.md is included in the commit that will be created after writing it, you do not need to keep updating a self-referential commit hash. Distinguish the baseline commit from “the next commit containing this record.”

## Transfer methods

| Move | Procedure |
| --- | --- |
| Same computer, another tool | Open the same folder, stopping the previous agent first |
| Another computer, no external service | Transfer the folder or a Git bundle on a secure local medium |
| Another computer, repository sharing authorized | Push to the specified repository and branch, then clone/pull at the destination |
| Local to cloud | Review files being sent; provide code, specification, verification records, and environment setup |
| Cloud to local | Retrieve changes, recreate dependencies, and rerun tests locally |

A push does not transfer uncommitted files. Copying a Git worktree as an ordinary folder can break its Git references. Create a destination worktree using Git's workflow, or transfer the actual files and records appropriately.

## After moving

Project instructions for the AI: [What the working rules mean](../templates.md#tool-independent-working-rules) · [How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md, SPEC.md, ENVIRONMENT.md, VERIFICATION.md, and HANDOFF.md
in that order, using local files or the supplied attachments/text.
If a required document is unavailable, ask me to provide it before proceeding.
Summarize the current objective, code state, last verification,
unfinished work, and next single task.
Report contradictions between the specification and code first.
Do not edit files, add dependencies, or publish anything at this stage.
```

Once the summary is correct, configure the environment, authentication, and permissions again. Set secrets securely in the destination environment; do not restore their values from shared files. For Python projects in this guide, recreate the environment with uv rather than copying .venv:

```sh
uv python install
uv sync --locked
uv run --locked python -m unittest discover -s tests -v
```

Run the tests after they exist. See [Python and uv setup](../python-uv.md#dependencies-and-moving-to-another-computer). Append the destination results.

## Ready to resume

- [ ] The specification and code versions match.
- [ ] Startup and tests can be reproduced.
- [ ] The next task and allowed scope are clear.
- [ ] Work can continue without chat history.
- [ ] Multiple agents are not modifying the same files simultaneously.

Keep unknowns marked as unverified. If tests fail after a move, check Python versions, dependencies, working directory, and OS differences before changing the specification.
