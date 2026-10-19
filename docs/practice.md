# Practice: Build a Study-Time Statistics CLI

Complete a small Python development cycle without external APIs or additional packages. Use the same specification and checks with any of the five tools.

## Before you begin

Complete [Getting started](index.md#getting-started) through the [first-run checks](setup.md#run-the-first-run-checks). You should have one installed and signed-in tool, a prepared `ai-practice` folder, the shared records, a [Python environment prepared with uv](python-uv.md), and a successful initial `smoke.py` exercise (the program that prints `Ready for AI development`).

Keep using that folder and tool. You do not need to install another tool or buy a subscription for this project.

## 1. Agree on the specification

Update the SPEC.md already in your practice folder using the requirements below. If you need a fresh copy, save the [specification template](assets/templates/SPEC.md.txt) and remove its final `.txt`. If you chose to save results from running `smoke.py`, keep them; saving results is not a prerequisite for this project.

- Purpose: show the count, total, and average of study-session durations.
- Input: one or more integer minute values from 0 through 1440.
- Output: one line in the format `Count: 2 / Total: 75 min / Average: 37.5 min`.
- Invalid input: an error on standard error, with exit code 2.
- Out of scope: file storage, networking, authentication, and additional packages.
- Acceptance criteria: [AC-01 through AC-05 on the specification page](workflow/specification.md).

A runnable [reference implementation](assets/example/study_stats.py) and [reference tests](assets/example/test_study_stats.py) are available. First ask the AI to implement your agreed specification, then compare when needed. Avoid saving two competing implementations in the same location; ask the AI to identify which version it checked in its on-screen summary.

## 2. Request implementation

In your prepared `ai-practice` folder, keep the shared records and ask the AI to read SPEC.md and [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)), then implement `src/study_stats.py` and `tests/test_study_stats.py`. Use the [implementation prompt](workflow/implementation.md).

Review the changes yourself. Confirm handling of no input, malformed input, and out-of-range values. Check that failed numeric conversion is not silently ignored.

## 3. Run normal and invalid-input cases

**Ask the AI to run the checks and display the results. You do not need to type every command, transcribe output, or create a verification file.** Review the proposed commands and permissions before execution.

```text
Run the checks for AC-01 through AC-05 in SPEC.md using the existing uv environment.
Compare actual results with the specification. Review code and dependencies for AC-05;
calculation tests alone do not verify storage or network behavior.
Display a brief summary in this conversation: what was checked, commands used,
who ran them, and pass / fail / not run for each criterion. Group related checks.
Include short failure details and anything you could not check.
Do not mark a check as passed unless you actually performed it.
Do not change requirements to make tests pass.
Do not create or update a verification record unless I request or agree to it.
If saving would help, explain why and ask whether I want a record.
```

If the AI cannot execute commands, run the commands below from ai-practice and paste the terminal results into the conversation. Ask the AI to explain the results on screen and identify you as the person who ran them. These commands are also a reference for reviewing what the AI runs; they work on macOS, Linux, and Windows PowerShell.

```sh
uv run --locked python src/study_stats.py 25 50
uv run --locked python src/study_stats.py 0
uv run --locked python src/study_stats.py 1440
uv run --locked python src/study_stats.py
uv run --locked python src/study_stats.py -1
uv run --locked python src/study_stats.py 1441
uv run --locked python src/study_stats.py 1.5
uv run --locked python src/study_stats.py abc
uv run --locked python -m unittest discover -s tests -v
```

Successful cases return exit code 0; invalid inputs return 2. The AI should capture these automatically. If you run the commands yourself, immediately after each command check `echo $?` on macOS/Linux or `$LASTEXITCODE` in PowerShell. Check before running another command.

| Input | Expected result |
| --- | --- |
| 25 50 | Count: 2 / Total: 75 min / Average: 37.5 min |
| 0 | Count: 1 / Total: 0 min / Average: 0.0 min |
| 1440 | Count: 1 / Total: 1440 min / Average: 1440.0 min |
| None, -1, 1441, 1.5, abc | An explanation on standard error and exit code 2 |

Save the distributed implementation to `src/study_stats.py` and the tests to `tests/test_study_stats.py` to run the reference version. The tests also work in the distributed folder layout. Their expected values come from the specification; they do not cover every attack or OS.

## 4. Review the short results summary

Read the AI's results in the conversation. Check **what was tested, whether anything failed, and what remains unverified**. Ask about anything you do not understand. You do not need to copy full logs or fill in a detailed form for every input. One short summary can cover related checks, provided the acceptance-criterion results are clear. Saving it is optional. Ask the AI to save it if you need it later; if the AI recommends saving, it should explain why and ask first.

For example, a summary might say “AC-01–AC-04: pass; automated CLI tests checked normal, boundary, and invalid inputs. AC-05: not run; code review still needed.” This is an illustration, not a result to copy as evidence. The actual summary must describe your own run.

Ask the AI to include a brief method and finding for AC-05. uv's environment setup creates project metadata and may download Python; those setup operations are separate from the program's behavior. After setup, add `--offline` to uv run if you also want to prohibit uv downloads. To check the program for storage and networking, ask the AI to review the code and compare the folder before and after execution. Have it summarize the method used; passing these tests alone does not prove an absence of network access.

Ask the AI to explain the following, then check its explanation yourself:

```text
Explain the processing steps from entering 25 and 50
to displaying an average of 37.5.
Also identify which checks reject no input, negative values, and decimals.
```

## 5. Hand off to another conversation

Write the implementation status and next task—such as considering an output-format change—in HANDOFF.md. Include verification results only if you requested or agreed to saving them. Otherwise, note that no results were saved and plan to rerun checks. Stop the previous conversation. In a new conversation or another tool, use the [resume prompt](workflow/handoff.md) and rerun the same tests.

For an extension such as CSV input, update the specification, error cases, and tests first. You do not need to add a UI, storage, and external integrations all at once.
