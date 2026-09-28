#!/usr/bin/env python3
"""Checks every `expression   # → result` line in reference pages against Emerald.

Each such line in an ```emerald block becomes `print(expression)`, run by the
emerald binary, and the printed text must equal the result the page shows
(a shown string's quotes are not printed). A line that starts with `const`,
`var`, or `print(` depends on its block, so check that block as a program
instead. A result shown as `# prints ...` is not checked here.

  python3 scripts/check-examples.py src/content/docs/docs/builtins/types/*.mdx

EMERALD names the binary (default: ../emerald-lang/zig-out/bin/emerald).
"""

import os
import re
import subprocess
import sys
import tempfile

emerald = os.environ.get("EMERALD", "../emerald-lang/zig-out/bin/emerald")
failed = False
for page in sys.argv[1:]:
    text = open(page, encoding="utf-8").read()
    cases = []
    for block in re.findall(r"```emerald\n(.*?)```", text, re.S):
        for line in block.splitlines():
            match = re.match(r"\s*(.*?)\s*#\s*→\s*(.*)$", line)
            if not match or match.group(1).startswith(("const ", "var ", "print(")):
                continue
            cases.append(match.groups())
    with tempfile.NamedTemporaryFile("w", suffix=".em", delete=False, encoding="utf-8") as program:
        program.write("".join(f"print({expression})\n" for expression, _ in cases))
    run = subprocess.run([emerald, "run", program.name], capture_output=True, text=True, encoding="utf-8")
    os.unlink(program.name)
    printed = run.stdout.splitlines()
    if run.returncode != 0 or len(printed) != len(cases):
        print(f"{page}: the examples did not run\n{run.stderr}")
        failed = True
        continue
    mismatches = [(e, shown, got) for (e, shown), got in zip(cases, printed)
                  if not (shown == got or (shown.startswith('"') and shown.endswith('"') and shown[1:-1] == got))]
    for expression, shown, got in mismatches:
        print(f"{page}: {expression}: the page shows {shown}, Emerald prints {got}")
    print(f"{page}: {len(cases)} examples, {len(mismatches)} mismatches")
    failed = failed or bool(mismatches)
sys.exit(1 if failed else 0)
