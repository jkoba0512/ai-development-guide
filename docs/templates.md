# Shared Templates

Use these files when the relevant stage asks for them. Save each download in the practice folder and remove its final `.txt`; if the browser displays text, copy it into an editor file. Replace placeholders only where they apply.

| File | When you use it | Purpose |
| --- | --- | --- |
| [SPEC.md](assets/templates/SPEC.md.txt) | First-run check, then the practice project | What to build, expected results, and important decisions with their reasons |
| [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([Setup](setup.md#prepare-your-records) · [Rules template](assets/templates/WORKING_RULES.md.txt)) | At the start of the first conversation | Instructions for how the AI should work |
| [ENVIRONMENT.md](assets/templates/ENVIRONMENT.md.txt) | After the first-run check | A short note on your tool, Python environment, and startup command |
| [HANDOFF.md](assets/templates/HANDOFF.md.txt) | When you choose to change conversations or environments | Current state and the next task for whoever continues |

[Common setup](setup.md#prepare-your-records) begins with the specification and working rules. Let the AI help prepare the later notes from observed details; review them before saving. Unknown values can stay “unknown,” and inapplicable fields can be omitted. Keep account names and secret values out of these files.

## Tool-independent working rules

[WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) is an ordinary Markdown document, not a special configuration file for any AI product. This guide uses it as the single source of shared project instructions.

Explicitly provide its contents when starting work: ask a tool with file access to read it, attach the file to a conversation, or paste the text into your request. The same method applies to SPEC.md and the other records. A tool that cannot access local files can still use the documents you supply; save its proposed changes yourself.

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
- Results shown in the conversation: “Entered 1.5 and confirmed exit code 2.” Save them only if requested or agreed.
- HANDOFF.md: “The program and tests are implemented. Next, rerun checks in the new environment.”

## Practice example

Use the [reference code](assets/example/study_stats.py) and [tests](assets/example/test_study_stats.py). The [practice project](practice.md) explains how to run them. Check file locations and the version under test before combining them with your own code.

## Updating files from earlier guide versions

If you already created AGENTS.md from an earlier version of this guide, rename it to [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) and update your project references. If it contains tool-specific settings or instructions, review them first. You can retain a short AGENTS.md that points to the shared file as explained in [Tool-specific instruction files](#tool-specific-instruction-files); no other tool-specific file is required.

If you used an earlier version of this guide and already have DECISIONS.md, copy its relevant entries into the **Decisions and reasons** section of SPEC.md. Use SPEC.md for future updates so you do not maintain the same information in two places. A separate decision record is only useful later if the history becomes too long to read comfortably alongside the requirements.
