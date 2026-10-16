# Write a Specification

A specification defines what must be true for the work to be complete. Review the AI's assumptions and save the agreed requirements in SPEC.md before implementation.

## Decide these six things first

| Item | Example: study-time statistics CLI |
| --- | --- |
| Purpose | Check the total and average duration of several study sessions |
| User and operation | Enter durations in minutes in a terminal |
| Input | One or more integers from 0 through 1440 |
| Output | Count, total minutes, average minutes to one decimal place |
| Invalid input | No input, negatives, values above the limit, decimals, and text produce errors |
| Out of scope | Login, storage, cloud connections, and charts |

“Make it useful” or “make it look good” does not establish completion criteria. Define concrete inputs, outputs, and exclusions.

## Ask the AI for a draft

```text
I want a small Python CLI that summarizes study durations.
Read the project working rules in WORKING_RULES.md or the contents provided with this request.
If those contents are unavailable, ask me to provide them before proceeding.
Then draft SPEC.md without implementing the program.
Include purpose, inputs, outputs, invalid-input behavior, exclusions,
and acceptance criteria.
List unclear points as questions or open decisions instead of silently assuming answers.
No external APIs, persistent storage, or additional packages are needed.
```

The working rules can be read from a local file, attached, or pasted into the conversation. This prompt does not require any product-specific instruction file or automatic loading. If the tool cannot save files, copy the agreed draft into SPEC.md yourself.

Review the draft for unrequested storage, authentication, or paid APIs. Save the agreed version in SPEC.md and record important choices and their reasons in DECISIONS.md.

## Connect acceptance criteria to tests

| ID | Action | Expected result |
| --- | --- | --- |
| AC-01 | Enter 25 and 50 | Count 2, total 75, average 37.5 |
| AC-02 | Enter 0 | Count 1, total 0, average 0.0 |
| AC-03 | Enter 1440 | Successful completion |
| AC-04 | No input / negative / 1441 / decimal / text | Error message and a nonzero exit code |
| AC-05 | Run normally | No file creation, network access, or additional dependencies |

Derive expected results from the specification, rather than reverse-engineering them from generated code. If acceptance criteria change, update the specification and the decision record first.

## Ready for implementation

Proceed when you can explain the inputs, outputs, and error behavior, each acceptance criterion has a verification method, and open decisions identify an owner and next action. Continue with [Implementation and verification](implementation.md) and the [templates](../templates.md).
