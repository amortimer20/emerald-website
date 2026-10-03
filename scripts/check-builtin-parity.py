#!/usr/bin/env python3
"""Checks the reference pages against Emerald's editor catalog, in both directions.

The editor's completion and hover read `src/builtins.json` in emerald-lang; these
pages are written by hand. This keeps the two describing the same members:

- every catalog member links to a page that exists, at its own <Member> entry
  (or, on a page with no <Member> entries, such as a language page, a heading);
- every <Member> on a page the catalog links to is either in the catalog, linked
  to that same anchor, or declared in Emerald's prelude (whose `##` comments the
  editor reads instead).

  python3 scripts/check-builtin-parity.py

EMERALD_LANG names the emerald-lang checkout (default: ../emerald-lang).
"""

import json
import os
import re
import sys
from pathlib import Path

emerald_lang = Path(os.environ.get("EMERALD_LANG", "../emerald-lang"))
docs = Path("src/content/docs/docs")
catalog = json.loads((emerald_lang / "src/builtins.json").read_text(encoding="utf-8"))
prelude = (emerald_lang / "src/prelude.em").read_text(encoding="utf-8")

# Members the prelude declares, by owning type: the editor documents these from
# their `##` comments, so a page may describe them without a catalog entry.
prelude_members = set()
owner = None
for line in prelude.splitlines():
    declared = re.match(r"(?:class|struct|enum|trait)\s+([A-Z]\w*)", line)
    if declared:
        owner = declared.group(1)
        continue
    if line.startswith("}"):
        owner = None
    member = re.match(r"\s*(?:func|var|const)\s+(?:([A-Z]\w*)\.)?([a-z_]\w*[?!]?)", line)
    if member:
        prelude_members.add((member.group(1) or owner, member.group(2)))


def page_file(path):
    base = docs / path.strip("/")
    for candidate in (base.with_suffix(".md"), base.with_suffix(".mdx"), base / "index.md", base / "index.mdx"):
        if candidate.is_file():
            return candidate
    return None


def slug(heading):
    # Starlight's heading ids (github-slugger): lowercase, punctuation dropped,
    # spaces become hyphens.
    text = re.sub(r"[`*_]", "", heading).strip().lower()
    text = re.sub(r"[^\w\- ]", "", text)
    return text.replace(" ", "-")


pages = {}


def anchors(file):
    if file not in pages:
        text = file.read_text(encoding="utf-8")
        members = {}
        for tag in re.findall(r"<Member\s([^>]*)>", text):
            attributes = dict(re.findall(r'(\w+)="([^"]*)"', tag))
            name = attributes["name"]
            members[attributes.get("id", re.sub(r"[?!]", "", name))] = (attributes.get("owner", "").rstrip("."), name)
        headings = {slug(h) for h in re.findall(r"^#{2,4}\s+(.*)$", text, re.M)}
        title = re.search(r"^title:\s*(.*)$", text, re.M).group(1).strip()
        # An entry without its own owner belongs to the type the page is named for.
        members = {anchor: (owner or title, name) for anchor, (owner, name) in members.items()}
        pages[file] = (members, headings)
    return pages[file]


problems = []
linked = {}  # page file -> anchors the catalog links to on it
for member in catalog["members"]:
    owner = member.get("owner")
    label = f"{owner}.{member['name']}" if owner and owner != "*" else member["name"]
    for signature in member["signatures"]:
        page = signature.get("page")
        if not page:
            problems.append(f"{label}: no page")
            continue
        path, _, anchor = page.partition("#")
        file = page_file(path)
        if file is None:
            problems.append(f"{label}: links to {page}, but there is no page at {path}")
            continue
        members, headings = anchors(file)
        if members and anchor not in members:
            # A reference page describes each member in its own <Member> entry.
            problems.append(f"{label}: links to {page}, but {file} has no <Member> with id {anchor!r}")
        elif not members and anchor not in headings:
            problems.append(f"{label}: links to {page}, but {file} has no heading #{anchor}")
        linked.setdefault(file, set()).add(anchor)

for file, targets in sorted(linked.items()):
    members, _ = anchors(file)
    for anchor, (owner, name) in sorted(members.items()):
        # A capitalized entry is the type's constructor, documented with the type.
        if anchor not in targets and (owner, name) not in prelude_members and not name[0].isupper():
            problems.append(f"{file}: `{name}` (#{anchor}) is in neither the catalog nor the prelude")

for problem in problems:
    print(problem)
count = sum(len(m["signatures"]) for m in catalog["members"])
print(f"{len(catalog['members'])} catalog members ({count} signatures) against {len(linked)} pages: "
      f"{len(problems)} problem{'' if len(problems) == 1 else 's'}")
sys.exit(1 if problems else 0)
