# AI Development Practice Guide for Students

This guide was created for students enrolled in the **System Design** course.

Learn to define a specification, review changes, and verify behavior while using AI for assistance. Start with whichever of Antigravity, Grok Build, GitHub Copilot, Codex, or Claude Code fits your access and budget. You can start with a free option. Paid subscriptions are optional.

!!! info "Free access and usage limits"
    **No paid subscription is required to use this guide.** Free plans and student benefits may have usage limits or eligibility requirements. Information was last verified on **October 6, 2026**. Check the [official sources](sources.md) for current conditions.

## What you will learn

| Stage | What you check yourself | What you keep |
| --- | --- | --- |
| Setup | Official distribution source and correct account | Environment and subscription notes |
| First run | Reading, editing, and execution work | A short first-run check |
| Specification | Inputs, outputs, and completion criteria | SPEC.md |
| Implementation | Changes match the specification | Code and diffs |
| Verification | Normal, boundary, and invalid inputs behave correctly | Tests and results displayed in the conversation |
| Handoff | Work can be reproduced and resumed elsewhere | ENVIRONMENT.md and HANDOFF.md |

**Keep the specification and code in the same project.** Verification results are displayed in the conversation; saving them is optional. If you need them for a submission or handoff, ask for a saved summary. If the AI recommends saving, it should explain why and ask first. When no results were saved, rerun checks after moving to another conversation or tool.

<span id="reading-order"></span>

## Getting started

Follow these steps in order. Choose **one** tool and interface; you do not need to install all five or buy a subscription.

1. **Choose a tool.** Check [Costs and student benefits](plans.md) and select an option you can access without paying if you want to stay on a free plan.
2. **Install and sign in.** Use your [chosen tool's setup page](#choose-your-tool-page) below. Complete its **Install and sign in** section before opening a project.
3. **Prepare Python, the folder, and records.** Follow [Set up Python with uv](python-uv.md) to install uv and Python and create ai-practice. Then [prepare your records](setup.md#prepare-your-records) with a text editor; no agent task is needed yet.
4. **Open the folder or start the CLI.** Follow [Open the folder or start the CLI](setup.md#open-the-folder-or-start-the-cli), then the matching tool instructions. Confirm the project path and set reading-first permissions.
5. **Check reading, editing, and execution.** Complete [Run the first-run checks](setup.md#run-the-first-run-checks) and read the actual results on screen.
6. **Build the practice project.** Work through specification, implementation, and verification in the [Practice project](practice.md).
7. **Hand off when needed.** Later, if changing conversations, tools, or computers, use [Handoffs between environments](workflow/handoff.md). Switching tools is not required for the first exercise.

### Choose your tool page

Start with **Install and sign in** on just one of these pages. Each then directs you to the shared folder preparation, explains how to start in that folder, and returns you to the first-run checks.

| Selected tool | Setup route |
| --- | --- |
| Antigravity | [App / IDE](tools/antigravity.md#install-and-sign-in) |
| Grok Build | [CLI](tools/grok-build.md#install-and-sign-in) |
| GitHub Copilot | [VS Code](tools/copilot.md#install-and-sign-in) |
| Codex | [Desktop, or optional CLI with suitable access](tools/codex.md#install-and-sign-in) |
| Claude Code | [CLI with suitable access](tools/claude-code.md#install-and-sign-in) |

If you are new to programming or terminals, begin by reading errors and actual results with the AI's help. The Python examples use [uv-managed environments](python-uv.md). They are learning exercises, not a statement that every System Design assignment uses Python. The same workflow applies to web apps, research scripts, and personal projects.

## Your first completion goals

- [ ] Explain your plan and additional billing settings.
- [ ] Know which folders, commands, and network operations are allowed.
- [ ] Run tests derived from acceptance criteria.
- [ ] Resume work in another conversation by rereading the project files.
- [ ] Explain the reasons for AI-generated changes in your own words.

When submitting work, follow the recipient's AI-use policy. Record which tools you used, what you delegated, and what you verified yourself.
