# Shared Templates

Save the linked text files, remove the final `.txt` to make them Markdown files, and place them in the root of your practice project. If your browser displays the contents, use “Save as.” Replace bracketed placeholders with actual values.

| File | Purpose |
| --- | --- |
| [SPEC.md](assets/templates/SPEC.md.txt) | Purpose, inputs, outputs, acceptance criteria, and decisions with their reasons |
| [ENVIRONMENT.md](assets/templates/ENVIRONMENT.md.txt) | Environment, authentication method, billing, permissions, and reproduction steps |
| [VERIFICATION.md](assets/templates/VERIFICATION.md.txt) | Short AI-written summary of checks, results, failures, and checks not run |
| [HANDOFF.md](assets/templates/HANDOFF.md.txt) | Current state and information needed to resume |
| [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) | Shared working rules |

These are blank starting templates. Mark unknowns as unverified; do not mark checks as passed unless they ran. You do not need to record account names or secret values.

VERIFICATION.md is normally written by the AI after it runs checks. You review the summary rather than transcribing commands and output. If the AI cannot run commands, give it your actual terminal results to summarize. Keep failures and checks not run visible; full logs are unnecessary for this exercise.

## Tool-independent working rules

[WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) is an ordinary Markdown document, not a special configuration file for any AI product. This guide uses it as the single source of shared project instructions.

Explicitly provide its contents when starting work: ask a tool with file access to read it, attach the file to a conversation, or paste the text into your request. The same method applies to SPEC.md and the other records. A tool that cannot access local files can still use the documents you supply; save its proposed changes yourself.

If you already created AGENTS.md from an earlier version of this guide, rename it to [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) and update your project references. If it contains tool-specific settings or instructions, review them first. You can retain a short AGENTS.md that points to the shared file as explained below; no other tool-specific file is required.

If you used an earlier version of this guide and already have DECISIONS.md, copy its relevant entries into the **Decisions and reasons** section of SPEC.md. Use SPEC.md for future updates so you do not maintain the same information in two places. A separate decision record is only useful later if the history becomes too long to read comfortably alongside the requirements.

## Tool-specific instruction files

The shared [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) serves the same general purpose as CLAUDE.md or AGENTS.md: it tells an AI agent how to work on your project. The difference is **how the instructions reach the agent**. This guide's shared filename has no assumed automatic discovery; supported tool-specific files are discovered according to the tool's rules.

These are project-level examples, checked against official documentation on **October 18, 2026**. They are not an exhaustive list. Support depends on the interface, version, settings, and file location. Some filenames are supported by several tools.

| Tool | Project instruction file or location | How it is used / official source |
| --- | --- | --- |
| Codex | `AGENTS.md` in the project root | Codex discovers project instructions before work; nested instructions can refine their scope. The filename is **AGENTS.md**, with an **S**, not AGENT.md. [Official instructions](https://learn.chatgpt.com/docs/agent-configuration/agents-md) |
| Claude Code | `CLAUDE.md` in the project root (or `.claude/CLAUDE.md`) | Loaded as project instructions at session start. Current versions also support AGENTS.md under documented conditions; check the installed version and Project instructions setting. [Official memory documentation](https://code.claude.com/docs/en/memory) |
| GitHub Copilot in VS Code | `.github/copilot-instructions.md` | Project-wide instructions for Copilot sessions; support and application depend on the session and instruction-file settings. [Official VS Code instructions](https://code.visualstudio.com/docs/agent-customization/custom-instructions) |
| Antigravity | `AGENTS.md` or `GEMINI.md`; modular rules in `.agents/rules/*.md` | Supports workspace and directory rules. Modular rule files need activation metadata; a Markdown file placed arbitrarily in the project is not equivalent. [Official rules](https://antigravity.google/docs/rules) |
| Grok Build | `AGENTS.md`; also supports `CLAUDE.md` and `.grok/rules/*.md` | Discovers project rules in the directory tree. Use `grok inspect` to check discovered files. [Official project rules](https://docs.x.ai/build/features/project-rules) |

### What should you do in this exercise?

**Keep using the shared working rules and explicitly provide them when starting a conversation. You do not need to create all the files in the table.** Use the [explanation](templates.md#tool-independent-working-rules), [setup instructions](setup.md#prepare-your-records), and [template](assets/templates/WORKING_RULES.md.txt) for the shared file. SPEC.md still holds requirements and their reasons; the instruction file describes how the AI should work.

If you later want your chosen tool to discover instructions automatically, add a small tool-specific file that points to the shared rules. Keep the actual rules in one place. For example, put this in `ai-practice/AGENTS.md` for Codex:

Shared file reference: [What the working rules mean](templates.md#tool-independent-working-rules) · [How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt).

```markdown
# Project instructions

Before starting work, read WORKING_RULES.md in this project root and follow it.
If you cannot access it, ask the user to provide its contents before proceeding.
```

This is an instruction to read another file, **not a guaranteed file import**. Check that the agent actually reads the shared rules. For Claude Code, an explicit import is supported: put this in `ai-practice/CLAUDE.md` to load the shared file alongside it:

Shared file reference: [What the working rules mean](templates.md#tool-independent-working-rules) · [How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt).

```markdown
@WORKING_RULES.md
```

The `@` import syntax here is specific to Claude Code; do not assume it has the same meaning in other tools. Before resuming, ask the agent to summarize the rules and identify the files it read. If you already have a tool-specific file, review and update it rather than overwriting it or creating conflicting instructions.

These documents guide behavior; they do not themselves enforce a sandbox or grant permissions. Configure [safe permissions](workflow/permissions.md) separately.

## What belongs where

- SPEC.md: “Reject decimal inputs.” Include the reason in its Decisions and reasons section.
- Code: convert to integers and check the permitted range.
- VERIFICATION.md: “Entered 1.5 and confirmed exit code 2.”
- HANDOFF.md: “Invalid-input checks passed. Next, run the same tests in another environment.”

## Practice example

Use the [reference code](assets/example/study_stats.py) and [tests](assets/example/test_study_stats.py). The [practice project](practice.md) explains how to run them. Check file locations and the version under test before combining them with your own code.
