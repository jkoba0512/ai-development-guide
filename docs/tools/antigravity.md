# Antigravity

Google's development environment has several entry points, including Antigravity 2.0, IDE, and CLI in the reviewed documentation. This guide starts with the app opening a local folder. If your interface differs, record the surface you use and select the corresponding tab in [Getting started](https://antigravity.google/docs/getting-started).

## Setup

1. Review [Costs and student benefits](../plans.md). Individual access is free but has usage limits.
2. Download the version for your OS from the [official download page](https://antigravity.google/download), checking system requirements.
3. Start the app and follow the instructions to authenticate with your Google account. Follow any school restrictions.
4. Create a project and associate only the practice folder using Add Folder or the equivalent option.
5. Start a Local conversation. If you select a Git worktree, confirm that its editing location differs from the original folder.

Source for installation and project operations: [Official setup](https://antigravity.google/docs/getting-started).

## Initial settings

Select Request Review in the project's permission settings. In the IDE interface, also use Request Review for terminal auto-execution and enable artifact review. Restrict access outside the project and enable Terminal Sandbox where supported. Setting names differ by OS and interface. [Official settings](https://antigravity.google/docs/settings).

## First-run checks

Complete the [three common checks](../setup.md). Review plans and artifacts before applying them. If browser operation becomes necessary, use a practice page and dedicated profile, avoiding pages signed in to personal accounts.

## Development and handoff

Save the specification to SPEC.md, then implement and verify small acceptance criteria. Move important plans stored only in conversations or artifact views into HANDOFF.md. Before changing tools, check the actual edited folder and Git diff, and transfer code together with verification records. See [Common handoff steps](../workflow/handoff.md).

**First-run completion:** the correct folder is readable, smoke.py can be reviewed, you or the AI can execute it and obtain the expected output, and the execution owner is recorded.
