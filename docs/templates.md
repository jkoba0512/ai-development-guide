# Shared Templates

Save the linked text files, remove the final `.txt` to make them Markdown files, and place them in the root of your practice project. If your browser displays the contents, use “Save as.” Replace bracketed placeholders with actual values.

| File | Purpose |
| --- | --- |
| [SPEC.md](assets/templates/SPEC.md.txt) | Purpose, inputs, outputs, and acceptance criteria |
| [ENVIRONMENT.md](assets/templates/ENVIRONMENT.md.txt) | Environment, authentication method, billing, permissions, and reproduction steps |
| [VERIFICATION.md](assets/templates/VERIFICATION.md.txt) | Who ran each command, exit codes, and actual results |
| [HANDOFF.md](assets/templates/HANDOFF.md.txt) | Current state and information needed to resume |
| [DECISIONS.md](assets/templates/DECISIONS.md.txt) | Reasons and consequences of decisions |
| [AGENTS.md](assets/templates/AGENTS.md.txt) | Shared working rules |

These are blank starting templates. Mark unknowns as unverified; do not mark checks as passed unless they ran. You do not need to record account names or secret values.

## What belongs where

- SPEC.md: “Reject decimal inputs.”
- Code: convert to integers and check the permitted range.
- VERIFICATION.md: “Entered 1.5 and confirmed exit code 2.”
- HANDOFF.md: “Invalid-input checks passed. Next, run the same tests in another environment.”

## Practice example

Use the [reference code](assets/example/study_stats.py) and [tests](assets/example/test_study_stats.py). The [practice project](practice.md) explains how to run them. Check file locations and the version under test before combining them with your own code.
