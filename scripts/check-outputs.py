#!/usr/bin/env python3
"""Checks every example that a page follows with its output.

An ```emerald block followed directly by a ```text title="Output"``` (or "Terminal") block is run
as a program, and everything it prints, errors included, must equal the output block exactly. The
program is saved under the file name the page's messages use, so a diagnostic's `file:line:col`
must match too. A "Terminal" block shows typed input on the prompt's line; give that input with
--input, or give one example its own answers with ```emerald input="Ada|30"``` (`|` separates
lines, and `-` means no input at all). A block titled "emerald test" or "emerald check" is run with that command instead.

  python3 scripts/check-outputs.py src/content/docs/docs/language/variables-and-constants.md variables.em

A page whose examples talk to https://api.example.com needs scripts/http-fixture.py running, with
HTTP_FIXTURE=http://127.0.0.1:8765 set; its examples are skipped, with a note, when it isn't.

EMERALD names the binary (default: the 0.6.0 release installed by mise).
"""

import argparse
import os
import re
import subprocess
import tempfile

parser = argparse.ArgumentParser()
parser.add_argument("page")
parser.add_argument("file_name", help="the file name the page's messages show, such as hello.em")
parser.add_argument("--input", default="Ada\n", help="standard input for programs that ask")
args = parser.parse_args()

emerald = os.environ.get("EMERALD", os.path.expanduser(
    "~/.local/share/mise/installs/github-amortimer20-emerald-lang/0.6.0/emerald"))
text = open(args.page, encoding="utf-8").read()
pairs = re.findall(
    r"```emerald(?: input=\"([^\"]*)\")?\n((?:(?!```).)*?)```[ \t]*\n\s*```text title=\"(Output|Terminal|emerald test|emerald check)\"\n((?:(?!```).)*?)```",
    text, re.S)
fixture = os.environ.get("HTTP_FIXTURE")
site = "https://api.example.com"
skipped = 0
mismatches = 0
for own_input, code, kind, shown in pairs:
    if site in code and not fixture:
        skipped += 1
        continue
    if fixture:
        code = code.replace(site, fixture)
        shown = shown.replace(site, fixture)
    if own_input == "-":
        typed = ""
    else:
        typed = own_input.replace("|", "\n") + "\n" if own_input else args.input
    folder = tempfile.mkdtemp()
    with open(os.path.join(folder, args.file_name), "w", encoding="utf-8") as program:
        program.write(code)
    command = kind.split()[1] if kind.startswith("emerald ") else "run"
    run = subprocess.run([emerald, command, args.file_name], cwd=folder, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", input=typed)
    got = run.stdout
    expected = shown
    if kind == "Terminal":
        # A terminal shows each typed answer, and the Enter after it, on its prompt's line;
        # the program's own output has neither. Remove them in order before comparing.
        for answer in typed.splitlines():
            expected = expected.replace(answer + "\n", "", 1)
    if got.strip() != expected.strip():
        mismatches += 1
        print(f"MISMATCH:\n{code}--- page shows:\n{shown}--- emerald prints:\n{got}")
note = f", {skipped} skipped (no HTTP_FIXTURE)" if skipped else ""
print(f"{args.page}: {len(pairs)} examples with output, {mismatches} mismatches{note}")
raise SystemExit(1 if mismatches else 0)
