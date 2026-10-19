# Write a Specification

**On this page, you and the AI will prepare SPEC.md for a small study-time program.** SPEC.md is the specification: it describes what to build, the reasons for important choices, and the results the program must produce.

You will follow this sequence: **understand the task → ask for a draft → review the requirements → check the acceptance criteria → save the agreed specification**. Implementation comes next.

## Before you begin

Complete the [first-run checks](../setup.md#run-the-first-run-checks), then keep using the same `ai-practice` folder and AI tool. The earlier `smoke.py` program only checked that you could create and run a Python file. This exercise starts a new program.

Open `ai-practice/SPEC.md` in your editor. It is a Markdown text document: you read and edit it, rather than run it as a program. If it is missing, [download the specification template](../assets/templates/SPEC.md.txt), save it in `ai-practice`, and remove the final `.txt`.

Keep the existing file for now. After reviewing the new draft, you will replace its first-run description with the study-time specification.

<span id="decide-these-six-things-first"></span>

## 1. Understand what you are going to build

Imagine that you studied for **25 minutes**, then **50 minutes**. You want a program that summarizes those two sessions:

```text
Input: 25 50
Output: Count: 2 / Total: 75 min / Average: 37.5 min
```

This is a **command-line program (CLI)**: you use it by entering a command in a terminal. The following requirements are already chosen for this exercise. Read them so you can check the AI's draft; you do not need to write a separate requirements document first.

| Part of the specification | Requirement for this exercise |
| --- | --- |
| Purpose and user | Help a student summarize study-session durations |
| Input | One or more integers in minutes, each from 0 through 1440; each number is one session |
| Output | Session count, total minutes, and average minutes to one decimal place, in the format above |
| Successful completion | Return exit code 0 |
| Invalid input | Reject missing input, negative values, values above 1440, decimals, and text; show an error on standard error and return exit code 2 |
| Out of scope | Accounts, saved study data, network access, charts, and additional packages |

An **exit code** is a number returned when a program finishes: here, 0 means success and 2 means invalid input. **Standard error** is the output channel used for error messages.

**Before continuing:** make sure you understand what each of the numbers 2, 75, and 37.5 in the example represents. Ask the AI to explain anything unfamiliar.

<span id="ask-the-ai-for-a-draft"></span>

## 2. Ask the AI to draft SPEC.md

Use the conversation for your `ai-practice` project. Paste the request below into the AI's chat input. For a CLI tool, enter it in the AI conversation rather than at the operating system's shell prompt.

The shared [WORKING_RULES.md](../templates.md#tool-independent-working-rules) tells the AI **how to work**, while SPEC.md describes **what to build**. Provide the rules through file access, attachment, or pasted text. References: [How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt). For names such as CLAUDE.md and AGENTS.md, see [Tool-specific instruction files](../templates.md#tool-specific-instruction-files).

```text
I want a small Python CLI that summarizes study durations.
Read the project working rules in WORKING_RULES.md or the contents provided with this request.
If those contents are unavailable, ask me to provide them before proceeding.

Show a draft specification in this conversation for me to review.
Do not implement the program or run its tests yet.
Use the existing uv-managed Python project; no additional packages are needed.

Requirements:
- Input: one or more integer durations in minutes, each from 0 through 1440.
- Each number represents one study session.
- Output format for input 25 50:
  Count: 2 / Total: 75 min / Average: 37.5 min
- Show the average to one decimal place. Successful execution returns exit code 0.
- Missing input, negatives, values above 1440, decimals, and text are invalid.
- Invalid input produces an error on standard error and exit code 2.
- No accounts, persistent storage, network access, charts, or additional packages.

Organize the draft into purpose and users, inputs, outputs, invalid-input behavior,
out of scope, acceptance criteria, decisions and reasons, and open decisions.
For acceptance criteria, include concrete inputs, expected results, and verification methods.
Keep important choices and their reasons in the same document.
Ask about unclear points instead of silently choosing an answer.
Label proposed reasons for my review; do not present them as decisions I already made.
Wait for my review before saving the agreed draft to SPEC.md.
```

**You should now have:** a draft shown in the conversation. Read it before asking for code.

## 3. Review the requirements and their reasons

Compare the draft with the requirements in step 1. Check that it uses minutes, accepts only the specified integers, gives the required output, and handles invalid inputs. Ask the AI to correct additions such as login or a database.

Also review **Decisions and reasons** in the same draft. This section explains why an important requirement was chosen. For example:

```markdown
## Decisions and reasons

Decision: allow 0 minutes.
Reason: a planned session may end without any recorded study time.
Alternative considered: accept only positive durations.
Affected criterion: AC-02 — entering 0 must succeed.
```

This is a possible reason for the exercise's choice. Accept it only if it matches your intention, or ask for it to be changed. Keep the requirement and its reason together in SPEC.md.

If the AI asks a question, answer it. Resolve questions that affect implementation; put genuinely deferred questions under **Open decisions** with a next action. If there are none, write “None.”

**You should now have:** a draft whose requirements and important reasons you can explain in your own words.

<span id="connect-acceptance-criteria-to-tests"></span>

## 4. Check how you will judge the program

An **acceptance criterion** is a condition the program must satisfy before the work is complete. **AC** is short for acceptance criterion; AC-01 and AC-02 are labels you can refer to later in tests or discussions.

Start with the expected result for 25 and 50. Calculate it before any code exists:

1. Two durations mean a session count of **2**.
2. 25 + 50 gives **75 minutes** in total.
3. 75 / 2 gives an average of **37.5 minutes**.

An automated test will later compare the program's actual output with this expectation. **The specification defines the correct result; the test checks it.**

Ask the AI to make sure the draft's Acceptance criteria section covers this table:

| ID | Input or behavior to check | Expected result | Verification after implementation |
| --- | --- | --- | --- |
| AC-01 | Enter 25 and 50 | Count 2, total 75, average 37.5; exit code 0 | Run the CLI and compare the output; include an automated test |
| AC-02 | Enter 0 | Count 1, total 0, average 0.0; exit code 0 | Test the minimum allowed value |
| AC-03 | Enter 1440 | Count 1, total 1440, average 1440.0; exit code 0 | Test the maximum allowed value |
| AC-04 | Try each separately: no input, -1, 1441, 1.5, and abc | Error on standard error and exit code 2 for each case | Include a test for each invalid input |
| AC-05 | Run the program normally | No application data files created, no network access, and no additional package dependencies | Review code and dependencies; inspect the folder before and after running |

AC-02 and AC-03 are **boundary checks**, covering the ends of the permitted range. AC-05 concerns the program itself after [uv environment setup](../python-uv.md). Files and downloads created while preparing the environment are separate. Passing calculation tests alone does not establish that a program avoids storage or network access.

**You should now have:** concrete completion checks in the draft. These are planned checks, not passed test results.

<span id="ready-for-implementation"></span>

## 5. Save the agreed specification and continue

After reviewing the draft, allow it to edit SPEC.md in the practice folder using your tool's approval-based editing mode. Then ask:

```text
Save the specification we reviewed to SPEC.md in the practice folder,
replacing the earlier first-run description.
Keep the requirements, acceptance criteria, decisions and reasons,
and any open decisions together in that file.
Do not implement the program yet.
```

If your tool cannot save files, copy the reviewed draft into `ai-practice/SPEC.md` yourself. Open the saved file and check that it contains the agreed version.

Before continuing, confirm:

- [ ] SPEC.md is saved in the practice folder.
- [ ] You can explain the inputs, output, invalid-input behavior, and important choices.
- [ ] AC-01 through AC-05 describe expected results and ways to check them.
- [ ] Questions affecting implementation are resolved.

**Next:** follow [Implementation and verification](implementation.md) to create and review the code. Then return to [Practice project → Run normal and invalid-input cases](../practice.md#3-run-normal-and-invalid-input-cases) to ask the AI to run checks and show actual results.

If a later test fails, compare the code with the agreed specification. For example, an average of 75 for inputs 25 and 50 indicates an implementation problem. If you intentionally change a requirement, update that requirement and its reason in SPEC.md before changing the tests.
