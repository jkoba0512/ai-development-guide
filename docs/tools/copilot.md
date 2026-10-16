# GitHub Copilot

This page covers GitHub Copilot in VS Code. Microsoft 365 Copilot has different subscriptions and uses.

## Setup

1. Check eligibility for Free, Student, or another plan using [Costs and student benefits](../plans.md).
2. For student access, apply and activate it using the [official student procedure](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students).
3. Enable Copilot following [VS Code's official setup instructions](https://code.visualstudio.com/docs/setup/copilot). If prompted to install an extension, check that GitHub is the official publisher.
4. Sign in with the GitHub account that has Copilot access.
5. Open the practice folder and attach files in Chat or explicitly name them.

Student benefits may be unavailable if the account used for verification differs from the account signed in to VS Code.

## Modes and first-run checks

Start in a question/explanation mode and ask the tool to read AGENTS.md and SPEC.md. Then switch to an agent that can edit files and complete the [three common checks](../setup.md). Mode names and agent implementations vary by VS Code version; record the actual interface in ENVIRONMENT.md.

Free / Student plans may limit model selection to Auto. You can still complete the initial checks without selecting a particular model. [Plan documentation](https://docs.github.com/en/copilot/get-started/plans).

## Permission settings

Keep global terminal and tool auto-approval disabled, and review commands and diffs. Before adding an MCP integration, inspect the destination and tools, starting with session-scoped approval. Review unfamiliar repository settings and scripts before trusting a folder. [VS Code security](https://code.visualstudio.com/docs/agents/run/security).

Sandbox availability depends on OS and session type. Check whether it is available in your interface. Without sandboxing, use a practice project containing no secrets.

## Development and handoff

After accepting AI completions, review the changes and run tests yourself. Copilot using another provider's model does not grant a subscription to that provider's product. Check each product's access conditions when switching.

If you want shared rules loaded automatically, keep product-specific instruction files limited to references to AGENTS.md and its reading order rather than maintaining separate rule sets. See [Handoffs](../workflow/handoff.md).
