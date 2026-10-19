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
| Handoff (optional extension) | Work can be reproduced and resumed elsewhere | ENVIRONMENT.md and HANDOFF.md |

**The AI drafts code and runs checks; you review the requirements, changes, and actual results.** Ask it to explain unfamiliar terms or code. Keep the specification and code in the same project. If you want to keep the displayed test results, ask for a saved summary.

<span id="reading-order"></span>

## Getting started

Follow these steps in order. Choose **one** tool and interface; you do not need to install all five or buy a subscription. Use the links in the steps, rather than reading every navigation item as a required lesson.

You will need a computer on which you can install an approved tool and uv, internet access for installation and AI use, and a text editor. This guide explains the terminal commands as they appear. If installation is blocked on a school computer, ask for the approved method before proceeding.

1. **Choose a tool.** Check [Costs and student benefits](plans.md) and select an option you can access without paying if you want to stay on a free plan.
2. **Install and sign in.** Use your [chosen tool's setup page](#choose-your-tool-page) below. Complete its **Install and sign in** section before opening a project.
3. **Prepare the practice project.** Open [Common setup](setup.md) and follow it in order. It sends you to the Python/uv manual, brings you back to prepare two starting files, and explains when to open your tool.
4. **Open the folder or start the CLI.** Continue with [Open the folder or start the CLI](setup.md#open-the-folder-or-start-the-cli). Follow only your chosen tool's folder-opening section, then return to Common setup.
5. **Check reading, editing, and execution.** Complete [Run the first-run checks](setup.md#run-the-first-run-checks) and read the actual results on screen.
6. **Build the practice project.** Work through specification, implementation, and verification in the [Practice project](practice.md).
7. **Hand off when needed.** Later, if changing conversations, tools, or computers, use [Handoffs between environments](workflow/handoff.md). Switching tools is not required for the first exercise.

After the practice project, explore [Organize project knowledge with Obsidian](obsidian.md) if you want a place to connect learning notes and prepare AI handoffs. This is an optional extension.

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

- [ ] Know which AI access option you are using and whether any additional billing is enabled.
- [ ] Know which folders, commands, and network operations are allowed.
- [ ] Ask the AI to run checks derived from the specification and interpret the displayed results.
- [ ] Optional next step: resume work in another conversation from the project files.
- [ ] Explain the reasons for AI-generated changes in your own words.

Your first completion point is the working [Practice project](practice.md#4-review-the-short-results-summary). Handoffs and Obsidian are extensions; Templates, Troubleshooting, and Official Sources are references. [Local checks and publication](maintenance.md) is for people maintaining this website, rather than a student exercise.

When submitting work, follow the recipient's AI-use policy. State which tools you used, what you delegated, and what you verified yourself.
