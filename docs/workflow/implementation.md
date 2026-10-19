# Implementation and Verification

**Start after [Write a specification](specification.md).** You should have an agreed SPEC.md in the same practice folder. On this page, ask the AI to create the program and tests, then review its changes. The [Practice project](../practice.md) is your route through the whole exercise.

## Implement a small unit of work

For this first project, one small task covers the study-time program and its tests. Keep using your existing `ai-practice` conversation and uv environment. Switch from reading-only / Plan mode to the approval-based editing mode described on your [tool setup page](../index.md#choose-your-tool-page).

Project instructions: [What the working rules mean](../templates.md#tool-independent-working-rules) · [How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt).

```text
Read WORKING_RULES.md and the agreed SPEC.md in this project or the contents I provide.
If either is unavailable, ask me to provide it.
Create src/study_stats.py and tests/test_study_stats.py to implement the specification.
Cover AC-01 through AC-04 with automated tests and keep the implementation within AC-05.
Use only the Python standard library, without storage or network operations in the program.
Keep using the existing uv environment. Do not add packages or change environment files.
Derive expected test results from SPEC.md, not from the generated program.
Show what changed and explain how the input becomes the output.
Wait for my review before running the checks.
```

**Expected files:** `src/study_stats.py` is the program. `tests/test_study_stats.py` is a set of automated checks. Tests run the code with known inputs and compare its actual behavior with the specification.

If your interface cannot write files, create those two files yourself from the AI's proposed contents. Keep the folder names and filenames exactly as shown so the practice commands work.

## Review the diff

A **diff** shows what changed between versions of a file. Use your tool's change view to read the proposed edits. With Git, `git diff` shows changes to tracked files; read newly created files directly too. Without Git, open the two files and compare their behavior with SPEC.md.

Check these points, asking the AI for explanations where needed:

- Does the program validate inputs and handle errors as specified?
- Does it calculate the count, total, and average you expect?
- Are the test expectations based on SPEC.md?
- Have extra features, packages, file writes, or network operations appeared?

You do not need to recognize every Python expression immediately. Ask the AI to trace `25 50` through the code and show where invalid inputs are rejected. Review any permission request against its command, folder, and purpose; see [Safe permission settings](permissions.md#how-to-review-an-approval).

**Next: return to [Practice project → Run normal and invalid-input cases](../practice.md#3-run-normal-and-invalid-input-cases).** That section provides the checking prompt and commands. The sections below explain how to interpret the results or fix failures.

## Types of verification

**Verification** means checking actual behavior against the agreed requirements.

| Type | Example in this project |
| --- | --- |
| Normal case | 25 and 50 produce count 2, total 75, and average 37.5 |
| Boundary values | 0 and 1440 are accepted |
| Invalid inputs | Missing input, negatives, decimals, text, and values above 1440 are rejected |
| Repeatability | Repeating the same command gives the same result |
| Regression check | After a fix, earlier working inputs still work |

The AI should display actual results and identify failures and checks not run. If it cannot run commands, execute them yourself and supply the output. Review the results on screen; ask for a saved summary if you want to keep it.

## When a check fails

Ask the AI to show the failing input, expected and actual results, and relevant error. A small reproducible example makes the problem easier to explain. Do not change expected results or delete tests just to make a failure disappear.

For example, if text input wrongly returned exit code 0, send:

```text
For AC-04, text input returned exit code 0 instead of 2.
Investigate the failing case while keeping the agreed requirements unchanged.
Explain the cause and propose a small fix for review.
After the fix is reviewed, rerun the failing check and the normal cases.
Display actual results and anything not checked.
```

If the requirement itself needs to change, agree on that change and its reason in SPEC.md before updating the code and tests.

## Completion criteria

Return to [Practice project → Review the short results summary](../practice.md#4-review-the-short-results-summary). Complete the project when the agreed criteria have been checked, you have reviewed the changes, and you can explain the results. Larger projects will also need checks of real user workflows.
