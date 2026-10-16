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
| Tests fail after moving | Python/dependency versions, OS, and working directory | Align environments and append failure evidence |
| Conversation becomes confusing | Specification and current-state records | Update HANDOFF.md and start a new conversation |
| Changes missing from Git | Untracked files, ignore rules, or another worktree | Check git status and actual file locations |

## How to report an error to the AI

```text
Goal: [what you were trying to do]
Environment: [OS / shell / tool / Python versions]
Working directory: [folder name without secrets]
Command: [exact command executed]
Expected result: [what should happen]
Actual result: [output and exit code]
Recent change: [files changed]
Investigate from a minimal reproduction without expanding permissions or subscriptions.
```

Redact keys, authentication tokens, and personal information from logs. Keep relevant error wording and line numbers so the cause can still be investigated.

## Local site does not open

Install dependencies using the README instructions and run MkDocs from the project root. If port 8000 is occupied, use `python -m mkdocs serve --dev-addr 127.0.0.1:8001`. Resolve build errors first; do not remove `--strict` simply to proceed to publication. See [Local checks](maintenance.md).
