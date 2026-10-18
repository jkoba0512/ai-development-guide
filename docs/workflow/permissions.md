# Safe Permission Settings

Permissions determine what an agent may run; a sandbox limits how far approved operations can reach. Approval prompts and sandboxing serve different purposes. A natural-language instruction such as “do not read secrets” is not a substitute for access control.

## Starting policy

| Area | Policy for initial practice |
| --- | --- |
| Files | Open only the practice folder. Keep personal documents, keys, and real data outside it |
| Editing | Start with reading; allow changes to specific files during implementation |
| Commands | Review the working directory and command before approving |
| Network | Distinguish dependency downloads from model requests. Do not add unnecessary web or MCP access |
| Browser | Use practice pages and a dedicated profile |
| External actions | Decide separately on pushes, PRs, publication, email, and billing |

## Product-specific checks

| Tool | Where to check and how to start |
| --- | --- |
| Antigravity | Project/IDE Request Review, access outside the folder, and Terminal Sandbox |
| Grok Build | Ask mode and read-only sandbox for exploration; a suitable profile for editing |
| Copilot / VS Code | Terminal/MCP approval scope, global auto-approval, and supported agent sandbox |
| Codex CLI | Start read-only; use workspace-write for implementation and on-request approvals |
| Claude Code | Explore in Plan mode, use an approval-based mode for edits, inspect /permissions |

Official sources: [Antigravity](https://antigravity.google/docs/settings), [Grok permissions](https://docs.x.ai/build/features/permissions), [Grok sandbox](https://docs.x.ai/build/features/sandbox), [VS Code](https://code.visualstudio.com/docs/agents/run/security), [Codex CLI](https://learn.chatgpt.com/docs/developer-commands?surface=cli), and [Claude Code](https://code.claude.com/docs/en/permissions).

Features differ by OS, interface, and administrator policy. In particular, Grok's child-process network restrictions on macOS differ from Linux. Check the active settings and record their scope in ENVIRONMENT.md.

## How to review an approval

Inspect the **target path, destination, options, and any chained operations**, not just the command's first word.

- `uv run --locked python -m unittest` runs project code. Read unfamiliar tests before executing them.
- `uv sync` and `uv add` may download packages and write environment or lock files. Review the dependency changes and sources. Run Python with uv in the project environment.
- `curl ... | bash` executes downloaded code. Review the official URL and script, and make this decision specifically for installation.
- `git push` sends code outside your machine. Confirm the destination and included history.
- Deletion, reset, and force push can be difficult to undo. Confirm targets and recovery options first.

Do not start with Always approve, Allow all, Turbo, bypass, or danger-full-access. If you repeat a small set of operations, use narrowly scoped rules only after understanding their meaning and reach.

## Secrets and prompt injection

Keep API keys, .env files, SSH keys, verification documents, and personal information out of practice folders and conversations. `.gitignore` controls Git tracking; it does not prevent every AI tool from reading a file.

Treat instructions embedded in web pages, READMEs, issues, or generated content—such as “ignore restrictions,” “send keys,” or “run this command”—as task data. External text is not authorization to change permissions. Review destinations and tool permissions before adding integrations.

## If a secret is shared accidentally

Stop execution, determine what was shared and where, then revoke and replace affected keys. Removing a value from the latest file does not remove it from Git history or conversations. Record the scope and response without including the secret itself. Review history before publication.
