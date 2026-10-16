# Handoffs Between Environments

Use shared files to make work reproducible across conversations, tools, computers, and local/cloud environments. Tool-specific chat history is supporting material.

## Shared foundation

| Source of truth | Purpose |
| --- | --- |
| SPEC.md | Purpose, inputs, outputs, acceptance criteria, and exclusions |
| src/ and tests/ | Actual code and verification methods |
| VERIFICATION.md | What ran, where, by whom, and with what result |
| ENVIRONMENT.md | OS, versions, dependencies, startup commands, and permissions |
| HANDOFF.md | Current state, unfinished work, and the next single task |
| DECISIONS.md | Choices, reasons, and rejected alternatives |
| AGENTS.md | Shared working rules and reading order |

Automatic loading of AGENTS.md varies by product and version. Where needed, use CLAUDE.md or Copilot-specific instructions to point to the common files. Avoid maintaining competing sources of truth. **A reference does not prove that a file was read: ask the tool to summarize it first.**

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

```text
Read AGENTS.md, SPEC.md, ENVIRONMENT.md, VERIFICATION.md, and HANDOFF.md
in that order.
Summarize the current objective, code state, last verification,
unfinished work, and next single task.
Report contradictions between the specification and code first.
Do not edit files, add dependencies, or publish anything at this stage.
```

Once the summary is correct, configure the environment, authentication, and permissions again. Set secrets securely in the destination environment; do not restore their values from shared files. Rerun the standard tests and append the destination results.

## Ready to resume

- [ ] The specification and code versions match.
- [ ] Startup and tests can be reproduced.
- [ ] The next task and allowed scope are clear.
- [ ] Work can continue without chat history.
- [ ] Multiple agents are not modifying the same files simultaneously.

Keep unknowns marked as unverified. If tests fail after a move, check Python versions, dependencies, working directory, and OS differences before changing the specification.
