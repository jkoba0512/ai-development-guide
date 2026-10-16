# Practice: Build a Study-Time Statistics CLI

Complete a small Python development cycle without external APIs or additional packages. Use the same specification and checks with any of the five tools.

## Before you begin

Complete [Getting started](index.md#getting-started) through the [first-run checks](setup.md#run-the-first-run-checks). You should have one installed and signed-in tool, a prepared `ai-practice` folder, the shared records, Python, and recorded smoke-check results.

Keep using that folder and tool. You do not need to install another tool or buy a subscription for this project.

## 1. Agree on the specification

Update the SPEC.md already in your practice folder using the requirements below. If you need a fresh copy, save the [specification template](assets/templates/SPEC.md.txt) and remove its final `.txt`. Keep the earlier smoke-check results in VERIFICATION.md.

- Purpose: show the count, total, and average of study-session durations.
- Input: one or more integer minute values from 0 through 1440.
- Output: one line in the format `Count: 2 / Total: 75 min / Average: 37.5 min`.
- Invalid input: an error on standard error, with exit code 2.
- Out of scope: file storage, networking, authentication, and additional packages.
- Acceptance criteria: [AC-01 through AC-05 on the specification page](workflow/specification.md).

A runnable [reference implementation](assets/example/study_stats.py) and [reference tests](assets/example/test_study_stats.py) are available. First ask the AI to implement your agreed specification, then compare when needed. Avoid saving two competing implementations in the same location; record which version was verified.

## 2. Request implementation

In your prepared `ai-practice` folder, keep the shared records and ask the AI to read SPEC.md and AGENTS.md, then implement `src/study_stats.py` and `tests/test_study_stats.py`. Use the [implementation prompt](workflow/implementation.md).

Review the changes yourself. Confirm handling of no input, malformed input, and out-of-range values. Check that failed numeric conversion is not silently ignored.

## 3. Run normal and invalid-input cases

=== "macOS / Linux"
    ```sh
    python3 src/study_stats.py 25 50
    python3 src/study_stats.py 0
    python3 src/study_stats.py 1440
    python3 src/study_stats.py
    python3 src/study_stats.py -1
    python3 src/study_stats.py 1441
    python3 src/study_stats.py 1.5
    python3 src/study_stats.py abc
    python3 -m unittest discover -s tests -v
    ```

=== "Windows PowerShell"
    ```powershell
    py -3 src/study_stats.py 25 50
    py -3 src/study_stats.py 0
    py -3 src/study_stats.py 1440
    py -3 src/study_stats.py
    py -3 src/study_stats.py -1
    py -3 src/study_stats.py 1441
    py -3 src/study_stats.py 1.5
    py -3 src/study_stats.py abc
    py -3 -m unittest discover -s tests -v
    ```

Successful cases return exit code 0; invalid inputs return 2. Immediately after a command, check `echo $?` on macOS/Linux or `$LASTEXITCODE` in PowerShell. Check before running another command.

| Input | Expected result |
| --- | --- |
| 25 50 | Count: 2 / Total: 75 min / Average: 37.5 min |
| 0 | Count: 1 / Total: 0 min / Average: 0.0 min |
| 1440 | Count: 1 / Total: 1440 min / Average: 1440.0 min |
| None, -1, 1441, 1.5, abc | An explanation on standard error and exit code 2 |

Save the distributed implementation to `src/study_stats.py` and the tests to `tests/test_study_stats.py` to run the reference version. The tests also work in the distributed folder layout. Their expected values come from the specification; they do not cover every attack or OS.

## 4. Record results and explanations

Record the command and actual result for each acceptance criterion in VERIFICATION.md. To check for storage and networking, review the code and compare the folder before and after execution. Record the method used; passing these tests alone does not prove an absence of network access.

Ask the AI to explain the following, then check its explanation yourself:

```text
Explain the processing steps from entering 25 and 50
to displaying an average of 37.5.
Also identify which checks reject no input, negative values, and decimals.
```

## 5. Hand off to another conversation

Write the implementation status, verification results, and next task—such as considering an output-format change—in HANDOFF.md. Stop the previous conversation. In a new conversation or another tool, use the [resume prompt](workflow/handoff.md) and rerun the same tests.

For an extension such as CSV input, update the specification, error cases, and tests first. You do not need to add a UI, storage, and external integrations all at once.
