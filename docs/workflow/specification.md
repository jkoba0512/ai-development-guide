# Write a Specification

Before asking AI to write code, decide **what the program should do and how you will judge whether it works**. Write those decisions in SPEC.md. This document is your specification.

For example, “summarize my study time” leaves many questions unanswered: Are the numbers minutes or hours? Are decimals allowed? What happens if nothing is entered? If you leave these choices to the AI, it may build something different from what you intended.

**Your task on this page:** prepare and review SPEC.md. You are not implementing the program or running its tests yet.

## Before you begin

Complete the [first-run checks](../setup.md#run-the-first-run-checks), then keep using the same practice folder and chosen tool.

In that earlier exercise, you created `smoke.py`, a tiny program that prints **Ready for AI development**. Its purpose was simply to confirm that you could create and run a Python file. Now you are starting a different task: designing the study-duration program.

Use **SPEC.md** for both the program's requirements and the reasons behind important choices. Save it directly in your practice folder (for example, `ai-practice/SPEC.md`). If you created it during Common Setup, open that existing file. The following sections show example contents and provide a template if the file is missing.

SPEC.md is an ordinary text document. The `.md` extension means Markdown: you can edit the contents as text and use headings and lists to organize them. Open it in your editor to read or edit it; you do not run it as a Python program or terminal command.

### SPEC.md: describe what the program must do

SPEC is short for specification. This file tells you and the AI **what to build and what counts as a correct result**.

A short example of its contents looks like this:

```markdown
# Study-duration program

Purpose: summarize my study sessions.
Input: one or more integer durations in minutes, from 0 through 1440.
Output: the session count, total minutes, and average to one decimal place.
Invalid input: show an error and return exit code 2.
Completion check: entering 25 and 50 gives count 2, total 75, and average 37.5.
```

This is a preview, not the complete specification. The next sections help you fill in the details. If you already have SPEC.md from the first-run exercise, update that file for the study-duration program. If it is missing, [download the specification template](../assets/templates/SPEC.md.txt), save it in your practice folder, and remove the final `.txt`.

### In the same SPEC.md, explain important choices

Add a **Decisions and reasons** section to SPEC.md. It explains **why** you chose an important requirement, especially when another reasonable choice was possible. Keeping the requirement and its reason in one file makes them easier to read together.

For example:

```markdown
## Decisions and reasons

Decision: allow a study duration of 0 minutes.
Reason: a planned session may end without any recorded study time.
Alternative considered: reject 0 and accept only positive durations.
Effect on the specification: entering 0 must succeed with count 1, total 0, and average 0.0.
```

You do not need to record every small detail. Add an entry in this section when you make a meaningful choice or change a requirement. This helps you explain your work and prevents the next AI conversation from guessing the reason. The specification template includes this section; no separate decision file is needed for this exercise.

### Give the AI your project instructions

[WORKING_RULES.md](../templates.md#tool-independent-working-rules) contains **instructions for how the AI should work on your project**. It is not the program's specification. For example, the instructions can tell the AI:

```text
Ask about missing requirements before implementing.
Do not change agreed completion criteria without asking.
Do not add features or dependencies outside the agreed scope.
Report which checks you actually ran and which you did not run.
```

Read these instructions yourself, then ask your tool to read the file, attach it, or paste its contents into the conversation. Merely saving the file does not guarantee that an AI tool has read it.

Use these links when you need a reminder:

- [What the working rules mean](../templates.md#tool-independent-working-rules): explains the purpose of the instructions and how to provide them to any tool.
- [How to save the file in your project](../setup.md#prepare-your-records): shows when and where to create it.
- [Download the working-rules template](../assets/templates/WORKING_RULES.md.txt): provides the actual text to save. Remove the final `.txt` from the downloaded filename.

For the difference between the shared rules and automatically discovered files such as CLAUDE.md or AGENTS.md, see [Tool-specific instruction files](../templates.md#tool-specific-instruction-files). You do not need to create a tool-specific file for this exercise.

**What to do now:** open SPEC.md in your editor, and make sure the AI has received the project instructions. Continue below to decide the new program's requirements. You will save the reviewed specification before asking for code.

## Decide these six things first

For this exercise, imagine that you studied for 25 minutes and then 50 minutes. You want to enter those durations and see how many sessions you recorded, their total duration, and their average.

We will make a small **command-line program (CLI)**: a program you run by typing a command in a terminal.

Read the example decisions below. They are choices for this exercise, not universal rules for all programs.

| Question you must answer | Decision for this exercise |
| --- | --- |
| Purpose: what problem are we solving? | Summarize the durations of study sessions |
| User and operation: who uses it, and how? | A student enters durations in minutes in a terminal |
| Input: what values are allowed? | One or more integers from 0 through 1440; each number is one session |
| Output: what should be shown? | Session count, total minutes, and average minutes to one decimal place |
| Invalid input: what should happen if a value is not allowed? | Show an error on standard error and finish with exit code 2 |
| Out of scope: what are we deliberately leaving out? | Accounts, file storage, network access, charts, and additional packages |

An **exit code** is a number a program returns when it finishes. In this exercise, 0 means success and 2 means invalid input. **Standard error** is the output channel used for error messages.

For example, allowing 0 means a session with no recorded study time is valid. Allowing 1440 sets the maximum duration of one session to one day. You could make different choices in another project, but you must state them before implementation.

**What to do now:** put these decisions into the corresponding sections of SPEC.md. If a choice is unclear, write it under Open decisions instead of leaving it for the AI to guess.

## Ask the AI for a draft

Open your chosen tool's conversation for the practice folder. Paste the following request into its chat input. For a CLI tool, enter it in the AI conversation, not at the operating system's shell prompt.

Project instructions for the AI: [What the working rules mean](../templates.md#tool-independent-working-rules) · [How to save the file](../setup.md#prepare-your-records) · [Download the rules template](../assets/templates/WORKING_RULES.md.txt).

```text
I want a small Python CLI that summarizes study durations.
Read the project working rules in WORKING_RULES.md or the contents provided with this request.
If those contents are unavailable, ask me to provide them before proceeding.

Draft SPEC.md without implementing the program.
Use the existing uv-managed Python project; no dependency additions are needed.
For this exercise:
- Input is one or more integer durations in minutes, each from 0 through 1440.
- Output is the session count, total minutes, and average minutes to one decimal place.
- Successful execution returns exit code 0.
- Missing input, negatives, values above 1440, decimals, and text are invalid.
- Invalid input produces an error on standard error and exit code 2.
- No external APIs, persistent storage, or additional packages are needed.

Include purpose, inputs, outputs, invalid-input behavior, exclusions,
and acceptance criteria with concrete inputs, expected results, and verification methods.
Include a Decisions and reasons section in SPEC.md for important choices,
their reasons, alternatives considered, and affected acceptance criteria.
List any remaining unclear points as questions or open decisions.
```

The working rules can be read from a local file, attached, or pasted into the conversation. No product-specific instruction file or automatic loading is required.

Read the AI's draft yourself. Check it against the decisions above. If it adds login, storage, charts, or a paid API, ask it to remove those additions. If it asks a question, answer it or record it as an open decision.

If the tool cannot save files, copy the reviewed draft into SPEC.md yourself. **An AI response in a conversation is not the saved specification until you put it in the project file.**

## Connect acceptance criteria to tests

An **acceptance criterion** is a condition the program must satisfy before you call the work complete. “The program works” is too vague. “Entering 25 and 50 produces count 2, total 75, and average 37.5” is something you can actually check.

**AC** stands for acceptance criterion. AC-01 and AC-02 are labels that let you refer to a condition in the specification, a test, or a verification record.

### Work through one example

For the input 25 and 50, calculate the expected result yourself:

1. There are two numbers, so the session count is **2**.
2. Add them: 25 + 50 = **75 minutes**.
3. Divide the total by the count: 75 / 2 = **37.5 minutes**.

You now know what a correct implementation must produce, even though the program does not exist yet. Save this as AC-01 in SPEC.md.

Later, a test will run the program with these inputs and compare its actual output with that expected result. The **criterion states what must be true**; the **test checks whether it is true**.

### Write checks for other situations

A program can work with 25 and 50 but still fail on an empty input or a boundary value. Add checks for those situations too.

| ID | Input or behavior to check | Expected result | How to verify it after implementation |
| --- | --- | --- | --- |
| AC-01 | Enter 25 and 50 | Count 2, total 75, average 37.5; exit code 0 | Run the CLI and compare the output; include an automated test |
| AC-02 | Enter 0 | Count 1, total 0, average 0.0; exit code 0 | Check the minimum allowed value manually or with a test |
| AC-03 | Enter 1440 | Count 1, total 1440, average 1440.0; exit code 0 | Check the maximum allowed value manually or with a test |
| AC-04 | Try each separately: no input, -1, 1441, 1.5, and abc | Error on standard error and exit code 2 for each case | Run each invalid input separately; include tests for each |
| AC-05 | Run the program normally | No application data files created, no network access, and no additional package dependencies | Review the code and dependencies; inspect the folder before and after running |

AC-02 and AC-03 are **boundary checks**: they test the ends of the allowed range. AC-04 checks that the program rejects invalid inputs instead of silently using them. AC-05 concerns the program's behavior after [uv environment preparation](../python-uv.md), not the environment files or downloads created during setup. AC-05 checks the scope of the implementation; a correct numeric answer alone does not establish that it avoids storage or networking.

**What to do now:** add this table to the Acceptance criteria section of SPEC.md. You are planning the checks, not claiming that they have passed.

### Use the criteria after implementation

After the program is implemented, you will use AC-01 like this:

```text
Input: 25 50
Expected output: Count: 2 / Total: 75 min / Average: 37.5 min
Expected exit code: 0
```

Ask the AI to run the program, compare actual results with these expectations, and display a summary of AC-01 and the other criteria in the conversation. Review which criteria passed, failed, or were not run. Related checks can share one short summary; full logs are unnecessary. Save it only if you request or agree to a record. If the AI cannot execute commands, run them yourself and give it the results to summarize. The [Practice project](../practice.md#3-run-normal-and-invalid-input-cases) gives the execution commands.

An automated test performs a comparison for you; it does not decide what the correct answer should be. For AC-05, review is also necessary: a passing calculation test does not prove that no network access occurs.

For example, if generated code prints an average of 75 for 25 and 50, do not change AC-01 to expect 75 just to make the test pass. The calculation above shows that the implementation needs correction.

If you intentionally change a requirement, update the requirement and its reason together in SPEC.md first. Then update the corresponding tests.

## Ready for implementation

Before moving on, check that:

- [ ] SPEC.md is saved in the practice folder, not only in the conversation.
- [ ] You can explain the permitted inputs, expected output, and invalid-input behavior.
- [ ] Each acceptance criterion has a concrete expected result and a verification method.
- [ ] You understand why 25 and 50 should produce an average of 37.5.
- [ ] Questions affecting implementation are resolved; deferred questions have an owner and next action.
- [ ] You have not marked planned checks as passed.

Your deliverable from this page is **the reviewed SPEC.md, including acceptance criteria and important decisions with their reasons**. Next, follow [Implementation and verification](implementation.md) to ask the AI to write code and perform the planned checks.
