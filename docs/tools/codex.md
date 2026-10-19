# Codex

This page follows the [Getting started](../index.md#getting-started) sequence: install and sign in → prepare a folder → open it → run the first checks. Choose **one interface**, not every Codex surface.

Desktop, CLI, IDE, and cloud access can have different plan requirements. Review [Costs and student benefits](../plans.md) before choosing. The guide does not require a paid subscription.

## Install and sign in

### Desktop route for eligible free accounts

The previously reviewed pricing page includes desktop access for ChatGPT Free subject to rollout. Use the [official quickstart](https://learn.chatgpt.com/docs/quickstart) to install the appropriate app and sign in with your ChatGPT account.

Confirm that your account actually has the relevant local coding interface. If unavailable, choose another free-capable tool; do not create a billed API key just to continue this guide. [Official pricing](https://learn.chatgpt.com/docs/pricing).

### Optional CLI route

Use this route only if you already have suitable CLI access or deliberately choose budgeted API usage. Follow the installation instructions on the [official CLI page](https://learn.chatgpt.com/docs/codex/cli). Reopen the terminal and run:

```sh
codex --version
codex --help
codex login
```

For account-based access, complete browser sign-in with the intended ChatGPT account. `codex login status` checks the authentication mode. API authentication is separate. These login commands do not start a project task. [Official CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

**Checkpoint:** your selected interface starts and authentication is complete. Save the version and interface in ENVIRONMENT.md once created.

## Prepare the practice folder

If you reached this page from Common setup to open an existing project, skip to [Open the practice folder](#open-the-practice-folder).

Follow [Common setup](../setup.md#prepare-a-working-folder) in order: it covers [Python with uv](../python-uv.md), the `ai-practice` folder, and [starting files](../setup.md#prepare-your-records). When you reach Common setup’s folder-opening step, return directly to [Open the practice folder](#open-the-practice-folder) below.

## Open the practice folder

### Desktop app

Use the app's local project/folder selector to open or add **`ai-practice`**. Check its path and start a conversation in that local project. Select reading-first permissions before the initial request. UI labels may differ; follow the [official quickstart](https://learn.chatgpt.com/docs/quickstart) for your interface.

### CLI

From the directory containing `ai-practice`, run:

```sh
cd ai-practice
codex --sandbox read-only --ask-for-approval on-request
```

If already in `ai-practice`, skip the first command. If elsewhere, use the folder's full path first.

For the editing check, restart in the same folder with:

```sh
codex --sandbox workspace-write --ask-for-approval on-request
```

Use `/permissions` to inspect settings. Managed restrictions take precedence. Review exactly what an approval authorizes; do not use unrestricted access or disabled sandboxing as a default. CLI flags do not automatically apply to the desktop or IDE interface. [Official CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

For this tool's instruction-file names and how they relate to the shared rules, see [Tool-specific instruction files](../templates.md#tool-specific-instruction-files). Automatic discovery is optional for this exercise.

## Run the first-run checks

Follow [Run the first-run checks](../setup.md#run-the-first-run-checks), reading [WORKING_RULES.md](../templates.md#tool-independent-working-rules) ([How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt)) and SPEC.md before editing. Ask the AI to identify who performed each check in its displayed results.

Check usage in the account dashboard or supported CLI commands such as `/status`. Additional credits and API billing are separate decisions. [Official pricing](https://learn.chatgpt.com/docs/pricing).

## Continue development

Proceed to the [Practice project](../practice.md). When moving between local and cloud work later, record directories, branches, and dependencies. Retrieve cloud changes, rerun tests locally, and update HANDOFF.md. See [Handoffs](../workflow/handoff.md).
