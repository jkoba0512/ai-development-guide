# Claude Code

This page follows the [Getting started](../index.md#getting-started) sequence: install and sign in → prepare a folder → open it → run the first checks. This walkthrough uses the **CLI**.

Claude chat's free allowance does not establish free Claude Code access. Check [Costs and student benefits](../plans.md) and [official pricing](https://claude.com/pricing). If Code is unavailable under your existing access and you want a free route, choose another tool. Buying a plan is optional.

## Install and sign in

Choose the method for your OS in the [official overview](https://code.claude.com/docs/en/overview). For example, the reviewed instructions support:

=== "macOS / existing Homebrew"
    ```sh
    brew install --cask claude-code
    ```

=== "Windows / WinGet"
    ```powershell
    winget install Anthropic.ClaudeCode
    ```

For Linux / WSL or native installers, use the corresponding official instructions and review script sources. Check updates regularly with Homebrew / WinGet installations.

Reopen the terminal, then check installation and sign in without starting a project session:

```sh
claude --version
claude auth login
```

Follow the browser authentication prompts. Confirm the intended account and billing source. If `ANTHROPIC_API_KEY` is already set, check whether it selects API billing instead of subscription access. Use `claude auth status` to inspect authentication without sharing secret values. [Official CLI reference](https://code.claude.com/docs/en/cli-reference).

**Checkpoint:** the version command works and authentication is complete. Save those details in ENVIRONMENT.md once created.

## Prepare the practice folder

Follow [Common setup](../setup.md#prepare-a-working-folder) to create `ai-practice`, check Python, and [prepare the six records](../setup.md#prepare-your-records). Return here afterward.

## Open the practice folder

From the directory containing `ai-practice`, run:

```sh
cd ai-practice
claude
```

If already inside `ai-practice`, skip the first command. If elsewhere, navigate using the full path first. Confirm the displayed project path and select **Plan** mode before sending your first request.

For the editing check, switch to an approval-based mode such as Default. Inspect rules with `/permissions`, avoiding broad permissions and bypass modes. Plan mode is not OS-level isolation; also inspect shell, network, and sandbox permissions. [Permissions](https://code.claude.com/docs/en/permissions).

## Run the first-run checks

Return to [Run the first-run checks](../setup.md#run-the-first-run-checks). Read AGENTS.md and SPEC.md first, then perform the small-edit and execution checks.

If using CLAUDE.md, point it to the shared records and confirm that they were read. Creating tool-specific instructions is not required for the first exercise.

## Continue development

Proceed to the [Practice project](../practice.md). Save code and verification records before moving conversations between interfaces. For another tool, resume from the shared files. See [Handoffs](../workflow/handoff.md).
