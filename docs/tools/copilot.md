# GitHub Copilot

This page follows the [Getting started](../index.md#getting-started) sequence: install and sign in → prepare a folder → open it → run the first checks. It covers GitHub Copilot in **VS Code**. Microsoft 365 Copilot has different subscriptions and uses.

## Install and sign in

1. Check Free or Student eligibility using [Costs and student benefits](../plans.md). You do not need to buy a plan for this guide.
2. If claiming student access, apply and activate it using the [official student procedure](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students).
3. Install and open VS Code using its [official setup instructions](https://code.visualstudio.com/docs/setup/copilot).
4. Enable Copilot. If prompted to install an extension, check the official GitHub publisher.
5. Sign in with the GitHub account that has Copilot access.

Student benefits may be unavailable if the verified account differs from the account signed in to VS Code.

**Checkpoint:** VS Code opens and Copilot is signed in. Do not send a project request until the practice folder is ready.

## Prepare the practice folder

Follow [Common setup](../setup.md#prepare-a-working-folder) to create `ai-practice`, check Python, and [prepare the six records](../setup.md#prepare-your-records). Return here afterward.

## Open the practice folder

1. In VS Code, choose **File → Open Folder** and select **`ai-practice`**.
2. Check that Explorer shows SPEC.md, WORKING_RULES.md, and the other records.
3. Open Copilot Chat.
4. Attach WORKING_RULES.md and SPEC.md, or explicitly name them in your first request.

Review unfamiliar repository settings and scripts before trusting a folder.

### Set permissions before the first request

Keep global terminal and tool auto-approval disabled. Review commands and diffs. If adding MCP later, inspect the destination and tools and begin with session-scoped approval. Sandbox availability depends on OS and session type; check the active interface. [VS Code security](https://code.visualstudio.com/docs/agents/run/security).

## Run the first-run checks

Start in a question/explanation mode, then follow [Run the first-run checks](../setup.md#run-the-first-run-checks). Switch to an editing agent for the small-edit stage. If that interface cannot edit or run files, perform the operation yourself and record who did it.

Mode names vary by version. Record the actual interface in ENVIRONMENT.md. Free / Student model selection may be Auto-only; a specific model is not required for these checks. [Plan documentation](https://docs.github.com/en/copilot/get-started/plans).

## Continue development

Proceed to the [Practice project](../practice.md). Review accepted completions and run tests yourself. Using another provider's model within Copilot does not grant a subscription to that provider's product.

For later [handoffs](../workflow/handoff.md), point product-specific instruction files to the common WORKING_RULES.md and reading order rather than maintaining separate rule sets.
