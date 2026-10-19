# Official Sources and Update History

## Research scope

Product information was checked on **2026-10-06** by opening official pricing, setup, and permission documentation. Individual subscriptions, student verification, regional checkout, and hands-on operation of the five products were not tested. Where support indicators were missing from retrieved pricing-table text, the guide leaves eligibility as a checkout/account check.

“No mention found” does not establish that an offer does not exist. Check official signup information for newly introduced or limited offers. Search snippets and third-party comparison articles were not used as the sole basis for findings.

The guide was translated into English on **2026-10-13**. Translation did not include a new product-terms review. Japan-specific findings remain explicitly identified and should not be interpreted as worldwide offers.

## Setup-flow review

The setup sequence was revised to separate installation and authentication from project startup. The official Antigravity setup, VS Code setup, Grok CLI, Codex CLI, and Claude Code CLI references were reopened to check these steps. In particular, standalone login commands let CLI users authenticate before creating or opening the practice folder. This review did not recheck prices or student offers; those findings retain their 2026-10-06 verification date.

## Sources

| Category | Official page | What was checked |
| --- | --- | --- |
| Antigravity | [Pricing](https://antigravity.google/pricing) | Free Individual access and Pro/Ultra limits |
| Antigravity | [Getting started](https://antigravity.google/docs/getting-started) | App/IDE/CLI entry points and projects |
| Antigravity | [Settings](https://antigravity.google/docs/settings) | Review, sandbox, and access outside folders |
| Google student offer | [Japan announcement](https://blog.google/intl/ja-jp/company-news/technology/gemini-student-offer-google-ai/) | Japan-specific free Plus and discounted Pro |
| Google student offer | [Student signup](https://gemini.google/students/) | Entry point for regional offer checks |
| Grok | [Pricing](https://x.ai/pricing) | Free / SuperGrok / Plus and Build comparison |
| Grok Build | [Overview](https://docs.x.ai/build/overview) | CLI installation, browser authentication, API |
| Grok Build | [CLI reference](https://docs.x.ai/build/cli/reference) | Version, login, and sandbox startup |
| Grok Build | [Settings](https://docs.x.ai/build/settings) | Configuration scopes and inspect |
| Grok Build | [Permissions](https://docs.x.ai/build/features/permissions) | Ask and automatic approval modes |
| Grok Build | [Sandbox](https://docs.x.ai/build/features/sandbox) | Profiles, OS differences, network restrictions |
| Grok Build | [Plan mode](https://docs.x.ai/build/features/plan-mode) | Planning and review |
| Copilot | [Plans](https://docs.github.com/en/copilot/get-started/plans) | Free / Student / paid plans and model selection |
| Copilot | [Student activation](https://docs.github.com/en/copilot/how-tos/copilot-on-github/set-up-copilot/enable-copilot/set-up-for-students) | Verification and eligibility reevaluation |
| Copilot | [Official student announcement](https://github.com/orgs/community/discussions/189268) | June 1 update in the original post: 200 credits |
| Copilot | [Billing](https://docs.github.com/en/copilot/concepts/billing-and-usage/individuals/billing) | Tokens and AI credits |
| VS Code | [Copilot setup](https://code.visualstudio.com/docs/setup/copilot) | Installation and sign-in |
| VS Code | [Security](https://code.visualstudio.com/docs/agents/run/security) | Approvals and agent sandbox |
| Codex | [Pricing](https://learn.chatgpt.com/docs/pricing) | Free entry point, Plus, separate API billing, Edu |
| Codex | [Quickstart](https://learn.chatgpt.com/docs/quickstart) | Getting started |
| Codex | [CLI](https://learn.chatgpt.com/docs/codex/cli) | Official CLI installation entry point |
| Codex | [Developer commands](https://learn.chatgpt.com/docs/developer-commands?surface=cli) | Startup flags and /permissions |
| Claude | [Pricing](https://claude.com/pricing) | Pro monthly/annual billing, Code, Education |
| Claude | [Education](https://claude.com/solutions/education) | Institutional access |
| Claude Code | [Overview](https://code.claude.com/docs/en/overview) | OS-specific setup, authentication, API selection |
| Claude Code | [CLI reference](https://code.claude.com/docs/en/cli-reference) | Standalone authentication and CLI startup |
| Claude Code | [Permissions](https://code.claude.com/docs/en/permissions) | Modes and approvals |
| Material | [Getting started](https://squidfunk.github.io/mkdocs-material/getting-started/) | Local setup |
| Material | [Publishing](https://squidfunk.github.io/mkdocs-material/publishing-your-site/) | GitHub Pages publication |
| GitHub Pages | [Creating a site](https://docs.github.com/en/pages/getting-started-with-github-pages/creating-a-github-pages-site) | Publication settings |

The older Codex documentation URLs on developers.openai.com redirected to learn.chatgpt.com during research; the guide links to the destinations.

## Python and uv environment sources

The environment instructions were checked against Astral's official documentation on 2026-10-18. This review covers setup and execution, not a new check of AI-product prices or student benefits.

| Official page | Use in this guide |
| --- | --- |
| [Install uv](https://docs.astral.sh/uv/getting-started/installation/) | OS-specific installation and version check |
| [Manage Python](https://docs.astral.sh/uv/guides/install-python/) | uv-managed Python installation |
| [Create projects](https://docs.astral.sh/uv/concepts/projects/init/) | Minimal practice project |
| [Project files](https://docs.astral.sh/uv/concepts/projects/layout/) | pyproject.toml, lockfile, and environment |
| [Run commands](https://docs.astral.sh/uv/concepts/projects/run/) | Execute Python through uv |
| [Lock and sync](https://docs.astral.sh/uv/concepts/projects/sync/) | Locked setup and reproduction |
| [Manage dependencies](https://docs.astral.sh/uv/concepts/projects/dependencies/) | Explicit dependency changes |
| [GitHub Actions](https://docs.astral.sh/uv/guides/integration/github/) | uv-based website build |

## Project instruction-file sources

Instruction-file names and discovery behavior were checked on 2026-10-18. This review does not recheck prices or student benefits.

| Tool | Official source |
| --- | --- |
| Codex | [Custom instructions with AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Claude Code | [Project instructions, memory, and file imports](https://code.claude.com/docs/en/memory) |
| Copilot in VS Code | [Custom instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) |
| Antigravity | [Rules and activation](https://antigravity.google/docs/rules) |
| Grok Build | [Project rules and discovery](https://docs.x.ai/build/features/project-rules) |

## Optional Obsidian extension sources

Reviewed on 2026-10-19 for the optional extension. This does not update the earlier AI-product pricing review.

| Official page | Use in this guide |
| --- | --- |
| [Data storage](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data) | Local Markdown files, vaults, and app settings |
| [Create or open a vault](https://help.obsidian.md/Getting+started/Create+a+vault) | Open the existing practice folder |
| [Internal links](https://help.obsidian.md/Linking+notes+and+files/Internal+links) | Markdown links for portability |
| [Pricing](https://obsidian.md/pricing) | Free app and optional paid services |

## Unverified items

- Final regional prices, taxes, and checkout conditions shown to individual accounts in Japan.
- Individual student eligibility, verification outcomes, and displayed renewal dates.
- Additional Antigravity allowance through the Google AI Plus student offer.
- Detailed general free allowance for Grok Build and eligibility under each plan.
- Actual product UI behavior, active permissions, and sandbox enforcement in each user's environment.
- Sample execution on Windows / Linux hardware.

## Update history

| Date | Change |
| --- | --- |
| 2026-10-06 | Initial edition: official research for five products, shared development/verification/handoff workflow, and MkDocs structure. No external publication |
| 2026-10-13 | English edition: translated documentation, prompts, templates, code messages, and configuration. Original research date retained |
| 2026-10-17 | Made shared working instructions tool-independent through [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) and explicit document sharing; updated prompts, templates, and handoff guidance |
| 2026-10-18 | Added Python/uv environment setup; standardized Python execution and website builds on uv |
