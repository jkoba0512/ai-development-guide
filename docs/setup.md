# Common Setup and First-Run Checks

## Create a working folder

Create an `ai-practice` folder separate from personal documents and secrets. Open only that folder in your AI tool. The folder where terminal commands run is called the working directory.

=== "macOS / Linux"
    ```sh
    mkdir ai-practice
    cd ai-practice
    python3 --version
    git --version
    ```

=== "Windows PowerShell"
    ```powershell
    mkdir ai-practice
    cd ai-practice
    py -3 --version
    git --version
    ```

The Python example assumes Python 3.11 or later. Record the displayed version, OS, shell, and tool versions in ENVIRONMENT.md. If you are not using Git yet, keep file history manually.

## Prepare the initial files

Save SPEC.md, ENVIRONMENT.md, VERIFICATION.md, and HANDOFF.md from the [templates](templates.md). AGENTS.md is the source of shared working rules. Do not assume your tool reads it automatically; explicitly ask it to read the file at the start.

```text
ai-practice/
├── SPEC.md
├── ENVIRONMENT.md
├── VERIFICATION.md
├── HANDOFF.md
├── AGENTS.md
├── src/
└── tests/
```

If using Git, initialize with `git init`. Create a `.gitignore` to exclude secrets before adding files. Review `git status` and `git diff`, then stage only the intended files and make your first commit. You do not need a GitHub account or a push to use Git locally.

## Check three capabilities separately

### 1. Reading

After installing and signing in, use settings that prioritize reading and send:

```text
Read AGENTS.md and SPEC.md in this folder. Explain the purpose and file structure.
Do not modify files, install dependencies, or publish anything at this stage.
Report the name of any file you could not read and the reason.
```

Compare the response with the actual file names and contents. A text response does not establish that file editing or command execution works.

### 2. A small edit

```text
Create only smoke.py. It should print "Ready for AI development" when run.
Use Python without external packages or network access.
After writing the file, show its contents and explain how to run it.
```

Read the change, then run it yourself:

=== "macOS / Linux"
    ```sh
    python3 smoke.py
    ```

=== "Windows PowerShell"
    ```powershell
    py -3 smoke.py
    ```

The expected output is `Ready for AI development`. Record the directory, command, actual output, and pass/fail result in VERIFICATION.md.

### 3. Execution by the AI tool

Ask the AI tool to run the same command. Review the command and working directory before approving it. If execution is unavailable with that service or configuration, recording “executed by a person” is sufficient. A permissions error does not require enabling unrestricted access.

## Local and cloud environments differ

Local files do not necessarily appear automatically in a cloud environment. If integration is needed, check the repository, branch, files being sent, and runtime. Try it with a practice project containing no secrets. After importing cloud changes, verify the code again locally.

“Started the app,” “signed in,” “read files,” “edited files,” and “executed code” are separate checks. Also review [Safe permission settings](workflow/permissions.md).
