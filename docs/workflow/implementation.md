# Implementation and Verification

## Implement a small unit of work

Limit each task to one feature or acceptance criterion. Name the files to change and the boundaries of the work.

Working rules: [explanation](../templates.md#tool-independent-working-rules) · [setup](../setup.md#prepare-your-records) · [template](../assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md, SPEC.md, and HANDOFF.md from the project or the supplied contents.
If a required document is unavailable, ask me to provide it before proceeding.
Create src/study_stats.py and tests/test_study_stats.py to satisfy AC-01 through AC-04.
Use only the Python standard library, with no storage or network operations.
Derive expected results from SPEC.md. Check input validation and CLI exit codes.
Report the tests actually run, their results, and checks not performed separately.
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

“The tests should pass” is not execution evidence. Record the command, directory, exit code, output, and who ran it. Leave unperformed checks marked as not run.

For the Python practice project:

```sh
python3 -m unittest discover -s tests -v
python3 src/study_stats.py 25 50
python3 src/study_stats.py -1
```

On Windows, replace `python3` with `py -3`. The last command intentionally exercises invalid input; a nonzero exit code is the expected result.

## When a check fails

Record the input, expected result, actual result, and error. Reproduce the failure with the smallest possible action. Do not change expected values or delete tests to hide failures. A person should decide whether a specification change is needed.

```text
For AC-04, text input returned exit code 0.
Investigate using this reproduction procedure and output.
Keep the acceptance criteria unchanged. After fixing the issue,
rerun the same invalid-input check and the normal cases.
```

## Completion criteria

The work is complete when acceptance criteria map clearly to verification, a person has reviewed the diff, execution records are available, and remaining limitations are in HANDOFF.md. Larger projects also need checks of real user workflows.
