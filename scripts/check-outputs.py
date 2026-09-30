#!/usr/bin/env python3
"""Checks every example that a page follows with its output.

An ```emerald block followed directly by a ```text title="Output"``` (or "Terminal") block is run
as a program, and everything it prints, errors included, must equal the output block exactly. The
program is saved under the file name the page's messages use, so a diagnostic's `file:line:col`
must match too. A "Terminal" block shows typed input on the prompt's line; give that input with
--input. A block titled "emerald test" or "emerald check" is run with that command instead.

  python3 scripts/check-outputs.py src/content/docs/docs/language/variables-and-constants.md variables.em

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
    r"```emerald\n((?:(?!```).)*?)```[ \t]*\n\s*```text title=\"(Output|Terminal|emerald test|emerald check)\"\n((?:(?!```).)*?)```",
    text, re.S)
mismatches = 0
for code, kind, shown in pairs:
    folder = tempfile.mkdtemp()
    with open(os.path.join(folder, args.file_name), "w", encoding="utf-8") as program:
        program.write(code)
    command = kind.split()[1] if kind.startswith("emerald ") else "run"
    run = subprocess.run([emerald, command, args.file_name], cwd=folder, stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", input=args.input)
    got = run.stdout
    expected = shown
    if kind == "Terminal":
        # A terminal shows each typed answer, and the Enter after it, on its prompt's line;
        # the program's own output has neither. Remove them in order before comparing.
        for answer in args.input.splitlines():
            expected = expected.replace(answer + "\n", "", 1)
    if got.strip() != expected.strip():
        mismatches += 1
        print(f"MISMATCH:\n{code}--- page shows:\n{shown}--- emerald prints:\n{got}")
print(f"{args.page}: {len(pairs)} examples with output, {mismatches} mismatches")
raise SystemExit(1 if mismatches else 0)
