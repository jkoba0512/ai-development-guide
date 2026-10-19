# Implementation and Verification

## Implement a small unit of work

Limit each task to one feature or acceptance criterion. Name the files to change and the boundaries of the work.

Project instructions for the AI: [What the working rules mean](../templates.md#tool-independent-working-rules) · [How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md, SPEC.md, and HANDOFF.md from the project or the supplied contents.
If a required document is unavailable, ask me to provide it before proceeding.
Create src/study_stats.py and tests/test_study_stats.py to satisfy AC-01 through AC-04.
Use only the Python standard library, with no storage or network operations.
Run Python and tests through uv in the existing project environment.
Do not add packages or change project environment files without asking.
Derive expected results from SPEC.md. Check input validation and CLI exit codes.
Run the checks and display a short summary of actual results in this conversation.
Include the commands, who ran them, and pass / fail / not run for each criterion.
Group related checks; include failure details and limitations, without copying full logs.
Do not mark unperformed checks as passed.
Do not create or update a verification record unless I request or agree to it.
If saving would help, explain why and ask whether I want a record.
```

If the AI proposes an extra package, download, or permission expansion, assess whether it is necessary. Do not add it if the specification can be satisfied without it.

## Review the diff

With Git, inspect `git status --short` and `git diff`. New files may not appear in a normal diff, so read them directly as well.

- Are input validation and error behavior implemented?
- Have out-of-scope features been added?
- Are there secrets, external connections, deletion operations, or arbitrary command execution?
- Are dependencies and startup instructions reproducible?
- Which parts can you not yet explain?

Ask for a step-by-step explanation with a short input when you do not understand part of the code.

## Types of verification

| Type | What to check |
| --- | --- |
| Normal cases | Expected inputs produce expected values |
| Boundary values | Zero and the maximum allowed value work correctly |
| Invalid inputs | Empty, malformed, and out-of-range values are rejected |
| Repeatability | The same procedure produces the same result |
| Regression checks | Fixes preserve previously working behavior |

**Let the AI execute checks and display the results. Your job is to review what was checked, failures, and remaining unknowns.** Ask it to include the commands, who ran them, and the result for each acceptance criterion; related checks may be grouped. For a failure, ask it to show the relevant input, actual result, and exit code so it can be reproduced.

“The tests should pass” is not execution evidence. Unperformed checks must remain marked as not run. If the AI cannot execute commands, run them yourself, provide the output, and ask it to explain the results in the conversation.

Review the results displayed by the AI. If you want to keep them, ask the AI to save a summary.

These commands are a reference for the AI, or for you when manual execution is needed:

```sh
uv run --locked python -m unittest discover -s tests -v
uv run --locked python src/study_stats.py 25 50
uv run --locked python src/study_stats.py -1
```

These uv commands work on macOS, Linux, and Windows PowerShell after [environment setup](../python-uv.md). The last command intentionally exercises invalid input; a nonzero exit code is the expected result.

## When a check fails

Ask the AI to show the failing input, expected and actual results, and relevant error, then reproduce the failure with the smallest possible action. Do not change expected values or delete tests to hide failures. A person should decide whether a specification change is needed.

```text
For AC-04, text input returned exit code 0.
Investigate using this reproduction procedure and output.
Keep the acceptance criteria unchanged. After fixing the issue,
rerun the same invalid-input check and the normal cases.
```

## Completion criteria

The work is complete when acceptance criteria map clearly to verification, a person has reviewed the diff, actual results have been displayed and reviewed, and remaining limitations are clear. Save a summary only if requested or agreed. Larger projects also need checks of real user workflows.
