# Codex

Codex is available through desktop, CLI, IDE, cloud, and other surfaces. **The entry points available on a free plan may differ from those available through paid plans or API access.** First review [official pricing](https://learn.chatgpt.com/docs/pricing) and the [comparison](../plans.md).

## Try the free plan

The reviewed pricing page includes Codex in ChatGPT Free, with desktop-app availability subject to rollout. Install the official app using the [official quickstart](https://learn.chatgpt.com/docs/quickstart) and sign in with your ChatGPT account. If the feature is unavailable, check rollout status or choose another accessible tool rather than creating an API key based on an assumption that CLI access is also free.

## Use the CLI

Choose a subscription that includes CLI access or budgeted API usage. Follow Install Codex on the [official CLI page](https://learn.chatgpt.com/docs/codex/cli) for installation instructions appropriate to your OS.

After installation, reopen your terminal and run:

```sh
codex --version
codex --help
```

Enter the practice folder and follow initial authentication instructions. For subscription access, choose ChatGPT sign-in and distinguish it from API authentication.

## Safe starting settings

On supported CLI versions, begin with reading:

```sh
codex --sandbox read-only --ask-for-approval on-request
```

For implementation, allow writes inside the working folder:

```sh
codex --sandbox workspace-write --ask-for-approval on-request
```

Use `/permissions` to inspect the active settings. Organization restrictions take precedence in managed environments. Do not make unrestricted access or disabled approvals/sandboxing your initial configuration. [Official CLI reference](https://learn.chatgpt.com/docs/developer-commands?surface=cli).

The reading-first command sets initial permissions. If a later approval requests writing, review exactly what it would authorize.

## First run and development

Read AGENTS.md and SPEC.md and complete the [common first-run checks](../setup.md). In desktop or IDE interfaces, check the UI permission controls. CLI flags do not automatically apply to other interfaces.

Check usage through your account dashboard and supported CLI commands such as `/status`. Decide separately about additional credits and API billing. [Official pricing and usage](https://learn.chatgpt.com/docs/pricing).

## Handoff

Record the working directory, branch, and dependencies in both local and cloud environments. Import cloud changes, rerun tests locally, and update HANDOFF.md. Do not depend solely on conversation-resume features. See [Common handoff steps](../workflow/handoff.md).
