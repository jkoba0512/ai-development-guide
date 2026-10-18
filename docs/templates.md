# Shared Templates

Save the linked text files, remove the final `.txt` to make them Markdown files, and place them in the root of your practice project. If your browser displays the contents, use “Save as.” Replace bracketed placeholders with actual values.

| File | Purpose |
| --- | --- |
| [SPEC.md](assets/templates/SPEC.md.txt) | Purpose, inputs, outputs, acceptance criteria, and decisions with their reasons |
| [ENVIRONMENT.md](assets/templates/ENVIRONMENT.md.txt) | Environment, authentication method, billing, permissions, and reproduction steps |
| [VERIFICATION.md](assets/templates/VERIFICATION.md.txt) | Who ran each command, exit codes, and actual results |
| [HANDOFF.md](assets/templates/HANDOFF.md.txt) | Current state and information needed to resume |
| [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) | Shared working rules |

These are blank starting templates. Mark unknowns as unverified; do not mark checks as passed unless they ran. You do not need to record account names or secret values.

## Tool-independent working rules

[WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) is an ordinary Markdown document, not a special configuration file for any AI product. This guide uses it as the single source of shared project instructions.

Explicitly provide its contents when starting work: ask a tool with file access to read it, attach the file to a conversation, or paste the text into your request. The same method applies to SPEC.md and the other records. A tool that cannot access local files can still use the documents you supply; save its proposed changes yourself.

If you already created AGENTS.md from an earlier version of this guide, rename it to [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) and update your project references. No other tool-specific file is required.

If you used an earlier version of this guide and already have DECISIONS.md, copy its relevant entries into the **Decisions and reasons** section of SPEC.md. Use SPEC.md for future updates so you do not maintain the same information in two places. A separate decision record is only useful later if the history becomes too long to read comfortably alongside the requirements.

## What belongs where

- SPEC.md: “Reject decimal inputs.” Include the reason in its Decisions and reasons section.
- Code: convert to integers and check the permitted range.
- VERIFICATION.md: “Entered 1.5 and confirmed exit code 2.”
- HANDOFF.md: “Invalid-input checks passed. Next, run the same tests in another environment.”

## Practice example

Use the [reference code](assets/example/study_stats.py) and [tests](assets/example/test_study_stats.py). The [practice project](practice.md) explains how to run them. Check file locations and the version under test before combining them with your own code.
