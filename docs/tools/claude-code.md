# Claude Code

Claude chat and Claude Code do not have identical free-access conditions. Confirm that your plan includes Code or that you have budgeted usage-based access. See [Costs and student benefits](../plans.md) and [Claude's official pricing](https://claude.com/pricing).

## Setup

Choose the method for your OS in the [official overview](https://code.claude.com/docs/en/overview). For example, the reviewed documentation provides these commands for an existing Homebrew installation on macOS or WinGet on Windows:

=== "macOS / Homebrew"
    ```sh
    brew install --cask claude-code
    ```

=== "Windows / WinGet"
    ```powershell
    winget install Anthropic.ClaudeCode
    ```

For Linux / WSL or native installers, read the corresponding official tab and check the source of scripts before executing them. Check for updates regularly with Homebrew / WinGet installations.

In a new terminal, run `claude --version`, then start `claude` from the practice folder. Confirm the billing source during initial login. If `ANTHROPIC_API_KEY` is already set, check whether it enables API billing instead of subscription usage. [Official setup and authentication](https://code.claude.com/docs/en/overview).

## Initial permissions

Start in Plan mode to inspect reading scope and the proposed plan. Use an approval-based mode such as Default when moving to edits. Inspect rules with `/permissions`, avoiding broad command permissions and bypass modes as defaults. [Permissions](https://code.claude.com/docs/en/permissions).

Plan mode is not the same as OS-level isolation. Check shell, network, and sandbox permissions too. See [Safe permission settings](../workflow/permissions.md).

## First run and handoff

Complete the [common first-run checks](../setup.md). If using CLAUDE.md, keep it focused on references to the shared AGENTS.md, SPEC.md, VERIFICATION.md, and HANDOFF.md. Confirm in the first response that the files were actually read.

Even if moving conversations between interfaces is supported, save code and verification records first. When switching to a different AI tool, resume from the shared files. See [Handoff steps](../workflow/handoff.md).
