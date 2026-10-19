# Optional Extension: Organize Project Knowledge with Obsidian

Read this page **after completing the [Practice project](practice.md)**, if you want to organize discussions, learning notes, or information for another AI conversation. The basic exercise works with your usual editor. Obsidian is an optional way to view and edit the same Markdown files.

## When it helps

Obsidian is useful when you want to connect a requirement to an explanation, find an earlier discussion, or prepare a short handoff instead of repeating a long conversation. For one small task, your existing editor may be enough.

Obsidian stores notes as local Markdown text files in a **vault**, which is an ordinary folder. Other editors and local agents can work with those files too. Obsidian refreshes notes when files change externally. [Official storage explanation](https://help.obsidian.md/Files+and+folders/How+Obsidian+stores+data).

The app is free to use without an account. Sync and Publish are optional paid services; neither is needed for this workflow. [Official pricing](https://obsidian.md/pricing).

## Try it with your existing project

1. Install Obsidian from its [official download page](https://obsidian.md/download).
2. In the vault chooser, select **Open folder as vault** and choose your existing `ai-practice` folder. Keep one copy of the project files rather than copying them into a second notes folder. [Official vault instructions](https://help.obsidian.md/Getting+started/Create+a+vault).
3. Open SPEC.md. Read its requirements and decisions. If you already prepared HANDOFF.md, open it to see the next task; the example below shows how to create one when you need it.
4. If useful, create a learning note with a question, your explanation, and a link to the relevant project document. Keep agreed requirements in SPEC.md.

For this introduction, the built-in editor, search, and links are enough. Plugin setup and automation can be explored separately after you are comfortable with this workflow.

Obsidian creates an `.obsidian` settings folder. It is app configuration, not the project specification or an AI instruction file. Keep running code and tests through uv from your project terminal, as in the [Python setup guide](python-uv.md).

## Example: carry a useful discussion into the next conversation

Suppose one AI helped you decide why 0 minutes is valid, and you now want another AI to implement the program.

1. Review the discussion and confirm the requirement and reason in SPEC.md.
2. When ready to save a handoff, ask the first AI:

```text
Summarize the agreed objective, important decisions, open questions,
and next task in HANDOFF.md. Refer to SPEC.md instead of duplicating its requirements.
Do not present assumptions as agreed decisions.
```

3. Open HANDOFF.md in Obsidian and check that it accurately represents your decisions.
4. Stop the first agent's work. Start the next conversation in the same project folder, or transfer the project as described in [Handoffs between environments](workflow/handoff.md).
5. Use the [resume prompt](workflow/handoff.md#after-moving). Ask the next AI to summarize the supplied documents before changing code.

The shared [WORKING_RULES.md](templates.md#tool-independent-working-rules) ([How to save the file](setup.md#prepare-your-records) · [Download the rules template](assets/templates/WORKING_RULES.md.txt)) still provides project working instructions. Opening a vault does not automatically deliver its contents to every agent: explicitly provide the needed files by local access, attachment, or pasted text.

Verification results stay in the conversation unless you ask or agree to save them. If you want a result included in the handoff, ask for that specific summary; otherwise rerun checks in the next environment.

## Keep sharing simple

- Use ordinary Markdown links when files will also be read on GitHub or in other editors. Obsidian supports these as well as its own Wikilinks. [Official linking guide](https://help.obsidian.md/Linking+notes+and+files/Internal+links).
- Give agents access to the practice project, rather than a personal vault containing unrelated notes.
- Use one writer at a time for a shared file. Obsidian is the place to organize notes; it does not coordinate agent tasks or resolve simultaneous edits.
- For agents on different computers or in the cloud, transfer the intended files explicitly. A local vault does not by itself make files available elsewhere.

You can stop here with the existing files. Add notes when they help you understand or resume the work, rather than making a record of every conversation.
