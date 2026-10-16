# Grok Build

Grok Build is a coding agent that works with local code. It is distinct from Grok chat and Grok Learning. This guide covers the official CLI. [Official overview](https://docs.x.ai/build/overview).

## Confirm access conditions

A Grok Free plan does not, by itself, establish free Build access. Review [Costs and student benefits](../plans.md) and the [official pricing table](https://x.ai/pricing), then confirm Build eligibility and limits after signing in. API-key use has a separate billing source from subscriptions; set a budget before using it.

## Setup

1. Find the installation instructions for your OS on the [official setup page](https://docs.x.ai/build/overview).
2. Check the distribution source and script before executing it. The reviewed official installer URL for macOS / Linux / WSL is shown below.
3. In a new terminal, run `grok version` and record the result in ENVIRONMENT.md.
4. Enter the practice folder and use `grok login` for browser authentication.

```text
https://x.ai/cli/install.sh
```

Read the official procedure and choose the correct OS-specific method rather than pasting a URL into a shell. Keep API keys out of conversations and shared configuration. Use environment variables or another secure method only when needed.

Sources for version and authentication commands: [CLI reference](https://docs.x.ai/build/cli/reference).

## Start with limited permissions

Check `grok --help`. On supported versions, start with:

```sh
grok --sandbox read-only
```

Keep Ask mode enabled, then begin with `/plan` and a reading-only request. When implementing, switch to a sandbox profile suitable for changes inside the working folder and review edits and commands. See [Permissions](https://docs.x.ai/build/features/permissions), [Plan mode](https://docs.x.ai/build/features/plan-mode), and [Sandbox](https://docs.x.ai/build/features/sandbox).

**Relevant limitations:** the reviewed documentation states that the sandbox is off by default. Child-process network blocking for read-only / strict is enforced on Linux, not in the same way on macOS. Model API and web-tool networking are separate. Use a practice folder containing no confidential files. [Sandbox limitations](https://docs.x.ai/build/features/sandbox).

## First run and handoff

Complete the [common first-run checks](../setup.md). Use `grok inspect` to inspect discovered settings, rules, and integrations. [Official settings](https://docs.x.ai/build/settings).

Even when using conversation export/import, keep SPEC.md, code, and VERIFICATION.md as the sources of truth. Rerun tests after a move; do not assume settings or permissions transferred. See [Handoffs](../workflow/handoff.md).
