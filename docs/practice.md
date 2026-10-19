# Practice: Build a Study-Time Statistics CLI

**Use this page as your route through the first complete project.** You will agree on a specification, ask the AI to implement it, then check and explain the results. Keep this page open when following a linked lesson.

## Before you begin

Complete [Common setup and first-run checks](setup.md). Keep the same `ai-practice` folder, AI tool, and uv environment. You should be able to run `smoke.py` and see `Ready for AI development`.

The new program will accept study-session durations such as 25 and 50 minutes and display their count, total, and average. **CLI** means command-line interface: you run it by entering a command in a terminal.

## 1. Agree on the specification

Open [Write a specification](workflow/specification.md) and complete its five steps. That lesson explains the requirements, supplies the AI prompt, and helps you review the acceptance criteria.

**Return here when:** the study-time specification is saved in `ai-practice/SPEC.md` and you can explain its inputs and expected output. The earlier `smoke.py` file can stay; it is a separate startup check.

## 2. Request implementation

Follow [Implementation and verification → Implement a small unit of work](workflow/implementation.md#implement-a-small-unit-of-work), then **Review the diff** on that page. Use its implementation prompt once.

**Return here when:** `src/study_stats.py` and `tests/test_study_stats.py` exist and you have reviewed what changed. The first file is the program; the second contains checks that compare its behavior with SPEC.md. Ask the AI to explain any code you cannot follow.

## 3. Run normal and invalid-input cases

In the same AI conversation, send:

```text
Run the checks for AC-01 through AC-05 in SPEC.md using the existing uv environment.
Compare actual results with the specification. Review code and dependencies for AC-05;
calculation tests alone do not verify storage or network behavior.
Display a brief summary: commands used, who ran them, and pass / fail / not run
for each criterion. Include failure details and anything you could not check.
Do not change requirements to make tests pass.
Save results only if I request or agree to it. If saving would help, explain why and ask.
```

Review proposed commands and their working folder before approving them. The expected results are:

| Input | Expected output | Exit code |
| --- | --- | --- |
| 25 50 | Count: 2 / Total: 75 min / Average: 37.5 min | 0 |
| 0 | Count: 1 / Total: 0 min / Average: 0.0 min | 0 |
| 1440 | Count: 1 / Total: 1440 min / Average: 1440.0 min | 0 |
| Try separately: no input, -1, 1441, 1.5, abc | An error on standard error | 2 |

An exit code describes how a command finished. Here, **2 is correct for deliberately invalid input**. It does not mean that the test itself failed.

### Commands if you run checks yourself

If your AI cannot execute commands, run these from `ai-practice`, one at a time, then give it the output to explain. They work on macOS, Linux, and Windows PowerShell.

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

Immediately after a program command, use `echo $?` on macOS/Linux or `$LASTEXITCODE` in PowerShell to see its exit code. Do this before the next command.

The last command runs the automated tests. Expect a positive number of tests and `OK`; **“Ran 0 tests” means nothing was checked**. On a failure, use [When a check fails](workflow/implementation.md#when-a-check-fails), then rerun the affected checks.

## 4. Review the short results summary

Read what passed, what failed, and what was not checked. If the AI only says “it should work,” ask it to run the checks or identify what prevents execution. For AC-05, ask how it reviewed the program for extra dependencies, saved data, and network operations. uv's setup files and downloads are separate from the program's behavior.

Ask:

```text
Explain how inputs 25 and 50 produce the average 37.5.
Show which code rejects missing input, negative values, and decimals.
```

**Your first project is complete when** SPEC.md matches the program, you can explain the example, and AC-01 through AC-05 have been checked with actual results. Address failures or missing checks before calling the project complete. If you want to keep the results, ask the AI to save a summary.

### Reference code if you need help

A [reference program](assets/example/study_stats.py) and [reference tests](assets/example/test_study_stats.py) are available for comparison. Save a copy of your work before replacing it. To run the reference version, put the program in `src/study_stats.py` and the tests in `tests/test_study_stats.py`, then use the commands above. Ask the AI to identify which version it tested.

## 5. Hand off to another conversation

**Optional next exercise:** follow [Handoffs between environments](workflow/handoff.md) if you want to change conversations, tools, or computers. You can use the same AI tool; no additional subscription is needed.

You can also explore [Organize project knowledge with Obsidian](obsidian.md). For a later feature such as CSV input, agree on the new requirements in SPEC.md before changing code and tests.
