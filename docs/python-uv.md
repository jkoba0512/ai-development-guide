# Set Up Python with uv

This guide uses Python for the first-run exercise and the study-duration CLI. **Use uv for those Python exercises.** This guide does not establish the language requirements of every System Design assignment; follow the instructions for each assignment.

Python runs your program. **uv** installs Python, prepares a separate environment for each project, and manages its dependencies. Neither requires an AI subscription.

**Your goal:** create a practice folder where a Python command runs successfully through uv. Do this before asking the AI to write your first program.

## Install uv

Choose the instructions for your OS. These are terminal commands, not messages to the AI. You do not need to install Python separately first.

=== "macOS"
    If Homebrew is already installed:
    ```sh
    brew install uv
    ```
    Otherwise, use the official standalone installer:
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

=== "Windows PowerShell"
    If WinGet is available:
    ```powershell
    winget install --id=astral-sh.uv -e
    ```
    Otherwise, follow the Windows standalone installer in the [official installation instructions](https://docs.astral.sh/uv/getting-started/installation/). On a school-managed computer, use the approved installation method.

=== "Linux / WSL"
    ```sh
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

The standalone installer downloads and executes a script. Check the official source and review the script before running it. Close and reopen your terminal afterward, then run:

```sh
uv --version
```

You should see a version number. If the command is not found, see [Troubleshooting](#troubleshooting). For updates, use the same package manager you installed with; standalone installations support `uv self update`. [Official installation documentation](https://docs.astral.sh/uv/getting-started/installation/).

## Install Python

We use **Python 3.12** as a consistent baseline for this guide. It is a tutorial choice, not a claim that every assignment requires this version.

```sh
uv python install 3.12
```

uv downloads Python if needed. An existing system Python installation does not have to be removed. This setup requires internet access; ask your administrator about proxy settings if downloads are blocked. [Official Python management guide](https://docs.astral.sh/uv/guides/install-python/).

## Create the practice project

Choose a location separate from personal documents and secrets. Open a terminal there.

=== "New practice folder"
    ```sh
    mkdir ai-practice
    cd ai-practice
    uv init --bare --python 3.12 --vcs none --no-workspace
    uv python pin 3.12
    uv sync
    ```

=== "Existing practice folder"
    Open a terminal in your existing `ai-practice` folder.
    If it has no `pyproject.toml`, run:
    ```sh
    uv init --bare --python 3.12 --vcs none --no-workspace
    uv python pin 3.12
    uv sync
    ```
    If `pyproject.toml` already exists, do not initialize again or overwrite it. Review the existing project's Python requirement, then use `uv sync --locked` when its lockfile is present, or `uv sync` for a new project without one.

These uv commands work on macOS, Linux, and Windows PowerShell. `--bare` creates a minimal project rather than a sample application; `--vcs none` avoids creating a Git repository; `--no-workspace` keeps it independent of any parent project. [Official project creation guide](https://docs.astral.sh/uv/concepts/projects/init/).

Create `src` and `tests` folders if they do not already exist:

=== "macOS / Linux"
    ```sh
    mkdir src tests
    ```

=== "Windows PowerShell"
    ```powershell
    mkdir src, tests
    ```

Do not run `uv init` in a clone of this guide's website repository. It already has its own Python project; the student exercise belongs in a separate `ai-practice` folder.

## Understand the environment files

| File or folder | What it means | What you do with it |
| --- | --- | --- |
| pyproject.toml | Project settings, required Python version, and declared dependencies | Keep with the code; review changes |
| .python-version | Python version selected for uv commands | Keep with the code so the next environment knows the choice |
| uv.lock | Exact resolved dependency versions | Keep with the code; do not edit by hand |
| .venv/ | This project's local Python environment | Let uv manage it; do not upload or copy it to another computer |

The `.venv` folder keeps this project's packages separate from other projects. **You do not need to activate it manually.** Run Python through `uv run` so the correct environment is used. The practice program needs no third-party packages, so an empty dependency list is expected. [Project files](https://docs.astral.sh/uv/concepts/projects/layout/).

## Check that Python runs

From inside `ai-practice`, run:

```sh
uv run --locked python --version
uv run --locked python -c "import sys; print(sys.executable)"
uv run --locked python -c "print('Python and uv are ready')"
```

Expected results:

- A Python **3.12.x** version.
- A Python executable inside this project's `.venv`: typically `.venv/bin/python` on macOS/Linux or `.venv\Scripts\python.exe` on Windows.
- The text **Python and uv are ready**.

`uv run` starts a command in the project environment. `--locked` reports an error if project settings and the lockfile disagree, rather than silently changing the lockfile. [Running commands](https://docs.astral.sh/uv/concepts/projects/run/) and [locking and syncing](https://docs.astral.sh/uv/concepts/projects/sync/).

Record `uv --version`, the Python version, and these results when you prepare ENVIRONMENT.md and VERIFICATION.md. Then return to [Common setup → Prepare your records](setup.md#prepare-your-records).

## Run programs and tests

After creating `smoke.py` in the first-run exercise, run:

```sh
uv run --locked python smoke.py
```

After implementing the study-duration program, run:

```sh
uv run --locked python src/study_stats.py 25 50
uv run --locked python -m unittest discover -s tests -v
```

These commands are the same on every OS. The file must exist before you run it. From a new terminal, navigate back to `ai-practice` first; do not create another project each time.

Environment preparation may download Python/packages and create `.venv` or `uv.lock`. That is separate from the practice program's requirement to avoid network access and application data storage. After setup, add `--offline` to prevent uv downloads too, for example `uv run --offline --locked python smoke.py`.

## Keep local environment files out of Git

If you use Git, create or update .gitignore in ai-practice before adding files. Include:

```text
.venv/
__pycache__/
*.py[cod]
.env
```

Keep pyproject.toml, .python-version, and uv.lock under version control. They describe how to rebuild the environment without copying its local files.

## Dependencies and moving to another computer

Do not add packages for the first-run or study-duration exercise. For a later assignment that needs a package, use `uv add PACKAGE_NAME`, replacing PACKAGE_NAME with the approved package name. Review the resulting pyproject.toml and uv.lock changes. Use `uv remove PACKAGE_NAME` to remove it. [Dependency management](https://docs.astral.sh/uv/concepts/projects/dependencies/).

When transferring work, bring the code, shared records, pyproject.toml, .python-version, and uv.lock. Do not transfer .venv. On the destination, install uv and run from the project folder:

```sh
uv python install
uv sync --locked
uv run --locked python -m unittest discover -s tests -v
```

Only run the last command after tests exist. If deliberately changing dependencies, use `uv sync` to update the lockfile, review the changes, and then return to locked runs. Do not drop `--locked` just to hide an unexplained mismatch.

## Troubleshooting

| Symptom | What to do |
| --- | --- |
| uv is not found | Reopen the terminal; follow the installer's PATH instructions. Avoid installing uv repeatedly by different methods |
| Python download fails | Check network/proxy access and school policies; do not disable certificate checks |
| Project already exists | Keep its pyproject.toml; use the existing-project branch above |
| Lockfile is missing | For a new reviewed project, run uv sync once to create it |
| Lockfile is out of date | Review changed settings/dependencies; deliberately run uv sync if those changes are intended |
| Cannot open smoke.py | Check the working directory and whether the file was created |
| Package import fails in the editor | Select the interpreter inside this project's .venv; keep terminal execution through uv |
| Offline run fails | Prepare the environment online first with uv sync --locked, then retry offline |

## Ready for the first exercise

- [ ] uv --version works.
- [ ] uv run --locked python --version shows Python 3.12.x.
- [ ] Python runs from ai-practice/.venv.
- [ ] The one-line check prints Python and uv are ready.
- [ ] You know which files to transfer and why .venv stays local.

Continue with [Prepare your records](setup.md#prepare-your-records), then open the folder in your chosen AI tool and perform the first-run checks.
