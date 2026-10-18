# Grok Build

This page follows the [Getting started](../index.md#getting-started) sequence: install and sign in → prepare a folder → open it → run the first checks. It covers the official CLI, which works with local code. Grok chat and Grok Learning are separate products. [Official overview](https://docs.x.ai/build/overview).

## Install and sign in

1. Review [Costs and student benefits](../plans.md) and the [official pricing table](https://x.ai/pricing). A Grok Free plan alone does not establish free Build access. If Build requires paid access for your account and you want a free route, choose another tool.
2. Use the installation instructions for your OS on the [official setup page](https://docs.x.ai/build/overview). Review the source and script before executing it.
3. Open a new terminal and run the following commands to check installation and sign in. You do not need to start a coding session yet.

```sh
grok version
grok login
```

The reviewed macOS / Linux / WSL installer URL is `https://x.ai/cli/install.sh`. Use the official OS-specific procedure rather than pasting the URL alone into a shell.

Complete browser authentication and confirm the account's Build access. API-key use has separate billing; do not set it up as a workaround for unavailable free access. Keep keys out of conversations and shared files. Source: [CLI reference](https://docs.x.ai/build/cli/reference).

**Checkpoint:** the version command works and authentication is complete. Save the version in ENVIRONMENT.md once you create that file.

## Prepare the practice folder

Follow [Common setup](../setup.md#prepare-a-working-folder) to create `ai-practice`, prepare [Python with uv](../python-uv.md), and [prepare the five records](../setup.md#prepare-your-records). Return here afterward.

## Open the practice folder

From the directory containing `ai-practice`, run:

```sh
cd ai-practice
grok --sandbox read-only
```

If already inside `ai-practice`, skip `cd ai-practice`. If elsewhere, navigate using its full path first. Check `grok --help` if your installed version rejects an option.

Keep **Ask** mode enabled. Enter `/plan`, then send the reading request from the common checks. For implementation, restart with an appropriate folder-scoped sandbox such as `grok --sandbox workspace` and retain Ask mode; review the requested changes and commands. [CLI reference](https://docs.x.ai/build/cli/reference), [Permissions](https://docs.x.ai/build/features/permissions), [Plan mode](https://docs.x.ai/build/features/plan-mode), [Sandbox](https://docs.x.ai/build/features/sandbox).

The reviewed sandbox documentation states that it is off by default. Child-process network blocking for read-only / strict differs between Linux and macOS; model API and web-tool networking are separate. Use a practice folder without confidential files. [Sandbox limitations](https://docs.x.ai/build/features/sandbox).

For this tool's instruction-file names and how they relate to the shared rules, see [Tool-specific instruction files](../templates.md#tool-specific-instruction-files). Automatic discovery is optional for this exercise.

## Run the first-run checks

Return to [Run the first-run checks](../setup.md#run-the-first-run-checks). Start with reading, then allow the small edit and verify execution.

Within the practice directory, `grok inspect` shows discovered settings, rules, and integrations. [Official settings](https://docs.x.ai/build/settings).

## Continue development

Proceed to the [Practice project](../practice.md). When changing conversations or tools later, keep SPEC.md, code, and VERIFICATION.md as the sources of truth even when using chat export/import. Rerun tests after moving; do not assume permissions transferred. See [Handoffs](../workflow/handoff.md).
