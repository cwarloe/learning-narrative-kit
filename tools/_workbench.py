"""Assertions for check_decks_browser.py's Portland workbench coverage."""

import re

from playwright.sync_api import expect


def unquote(text):
    text = text.strip()
    return (
        text[1:-1]
        if len(text) > 1 and text[0] in "\"'" and text[-1] == text[0]
        else text
    )


def terminal_source(block):
    header, body = block.split("\n---\n", 1)
    objectives = []
    for match in re.finditer(
        r"- id: ([^\n]+)\n\s+label: ([^\n]+)\n\s+trigger: ([^\n]+)", header
    ):
        objectives.append(
            dict(zip(["id", "label", "trigger"], map(unquote, match.groups())))
        )
    commands = {}
    key = None
    lines = []
    for line in body.splitlines():
        if line and not line[0].isspace() and line.endswith(": |"):
            if key is not None:
                commands[key] = "\n".join(lines).rstrip()
            key, lines = unquote(line[:-3]), []
        elif key is not None:
            lines.append(line[2:] if line.startswith("  ") else line)
    if key is not None:
        commands[key] = "\n".join(lines).rstrip()
    return objectives, commands


def check_workbench(page, source, base):
    """Exercise the real Docsify route against its Markdown source."""
    path = "/portland-desk/#/workbench/" + source.stem
    page.goto(base + path, wait_until="domcontentloaded")
    page.locator(".markdown-section h1").wait_for()
    blocks = re.findall(r"```lnk-terminal[^\n]*\n([\s\S]*?)```", source.read_text())
    terminals = page.locator(".lnk-terminal-instance")
    expect(terminals).to_have_count(len(blocks))
    command_count = 0
    for i, block in enumerate(blocks):
        objectives, commands = terminal_source(block)
        term = terminals.nth(i)
        expect(term).to_have_attribute("data-initialized", "true")
        config = term.evaluate("(e)=>JSON.parse(decodeURIComponent(e.dataset.config))")
        actual = term.evaluate(
            "(e)=>JSON.parse(decodeURIComponent(e.dataset.commands))"
        )
        assert (
            config["objectives"] == objectives
        ), "Objective text was truncated or quoted incorrectly"
        assert actual == commands, "Commands or output differ from the source fence"
        inp = term.locator("input")
        for command, output in commands.items():
            inp.fill(command.upper())  # Dictionary matching is case insensitive.
            inp.press("Enter")
            assert (
                term.locator(".lnk-term-output").last.text_content() == output
            ), command
        command_count += len(commands)
        assert term.locator(".lnk-term-obj-pill.completed").count() == len(objectives)
        inp.press("ArrowUp")
        assert inp.input_value() == list(commands)[-1].upper()
        inp.press("ArrowDown")
        assert inp.input_value() == ""
        inp.fill("not-a-real-command <test>")
        inp.press("Enter")
        assert (
            "not-a-real-command <test>"
            in term.locator(".lnk-term-output.error").last.text_content()
        )
        inp.fill("help")
        inp.press("Enter")
        help_text = term.locator(".lnk-term-output").last.text_content()
        assert all(c in help_text for c in commands)
        inp.fill("cls")
        inp.press("Enter")
        assert term.locator(".lnk-term-output-block").count() == 0

    # Native disclosure controls must be operable by keyboard and actually reveal content.
    details = page.locator(".markdown-section details")
    expect(details).to_have_count(
        len(re.findall(r"<details(?:\s|>)", source.read_text()))
    )
    for i in range(details.count()):
        item = details.nth(i)
        summary = item.locator("summary").first
        assert not item.evaluate("(e)=>e.open")
        summary.focus()
        summary.press("Enter")
        assert item.evaluate("(e)=>e.open")
        assert item.evaluate(
            '(e)=>e.innerText.length > e.querySelector("summary").innerText.length'
        )
        summary.press("Enter")
        assert not item.evaluate("(e)=>e.open")

    notes = page.locator(".scratchpad-body textarea")
    expect(notes).to_have_count(source.read_text().count("<textarea"))
    saved = {}
    for i in range(notes.count()):
        note = notes.nth(i)
        value = f'Browser check: {source.stem} / {note.get_attribute("id")}\nRetain this second line.'
        note.fill(value)
        saved[note.get_attribute("id")] = value
    if saved:
        page.reload(wait_until="domcontentloaded")
        page.locator(".scratchpad-body textarea").first.wait_for()
        for note_id, value in saved.items():
            expect(page.locator('[id="' + note_id + '"]')).to_have_value(value)

    # Replay runs against the same parsed objective commands, with a virtual clock.
    if blocks:
        page.clock.install()
        for i, block in enumerate(blocks):
            objectives, _ = terminal_source(block)
            term = page.locator(".lnk-terminal-instance").nth(i)
            expect(term).to_have_attribute("data-initialized", "true")
            replay = term.locator(".lnk-term-replay-btn")
            if replay.count():
                replay.click()
                assert replay.is_disabled(), "Replay should prevent overlapping runs"
                assert term.locator("input").is_disabled()
                duration = sum(len(o["trigger"]) * 45 + 1400 for o in objectives) + 2000
                page.clock.run_for(duration)
                assert term.locator(".lnk-term-obj-pill.completed").count() == len(
                    objectives
                ), "Replay failed"
                assert replay.is_enabled() and term.locator("input").is_enabled()
                assert term.locator(".lnk-term-output-block").count() == len(
                    objectives
                ), "Replay must run each objective once"
    return {
        "path": path,
        "terminals": len(blocks),
        "commands": command_count,
        "reveals": details.count(),
        "scratchpads": len(saved),
    }
