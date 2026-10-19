# Troubleshooting

| Symptom | Check first | Next action |
| --- | --- | --- |
| Command not found | New terminal session and installation directory on PATH | Follow the official PATH setup instructions |
| Student benefit unavailable | Verified account matches the signed-in account | Check activation, propagation, and expiry |
| Cannot select a model | Auto-only plan or administrator policy | Use an available model for first-run checks |
| Usage limit reached | Remaining allowance, reset time, and billing settings | Save progress and wait or hand off |
| AI cannot read files | Working folder, attachments, and access scope | Name the file explicitly; add only necessary access |
| Execution approval requested | Command, working directory, and destination | Understand the operation and approve narrowly |
| Installation blocked on school computer | Administrator policy and supported environments | Use an approved method or another allowed environment |
| Tests fail after moving | uv/Python versions, uv.lock, OS, and working directory | Run uv sync --locked; keep .venv local and display the failure details; save only if requested or agreed |
| Conversation becomes confusing | Specification and current-state records | Update HANDOFF.md and start a new conversation |
| Changes missing from Git | Untracked files, ignore rules, or another worktree | Check git status and actual file locations |

## How to report an error to the AI

```text
Goal: [what you were trying to do]
Environment: [OS / shell / tool / uv / Python versions]
Working directory: [folder name without secrets]
Command: [exact command executed]
Expected result: [what should happen]
Actual result: [output and exit code]
Recent change: [files changed]
Investigate from a minimal reproduction without expanding permissions or subscriptions.
```

Redact keys, authentication tokens, and personal information from logs. Keep relevant error wording and line numbers so the cause can still be investigated.

## Local site does not open

Install uv using the [environment manual](python-uv.md), then run `uv sync --locked` in the website repository as described in the README and run MkDocs from the project root. If port 8001 is occupied, use `uv run --locked mkdocs serve --dev-addr 127.0.0.1:8002`. Resolve build errors first; do not remove `--strict` simply to proceed to publication. See [Local checks](maintenance.md).
