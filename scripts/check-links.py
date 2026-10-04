#!/usr/bin/env python3
"""Checks every internal link and anchor in the built site (run `npm run build` first).

  python3 scripts/check-links.py

Each `<a href>` that stays on the site must reach a page that was built, and a `#fragment`
must be an id on that page. External links are not fetched.
"""

import glob
import os
import sys
from html.parser import HTMLParser
from urllib.parse import unquote, urlparse

dist = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "dist")


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links = set(), []

    def handle_starttag(self, tag, attrs):
        attributes = dict(attrs)
        if "id" in attributes:
            self.ids.add(attributes["id"])
        if tag == "a" and attributes.get("href"):
            self.links.append(attributes["href"])


pages = {}
for file in glob.glob(f"{dist}/**/*.html", recursive=True):
    page = Page()
    with open(file, encoding="utf-8") as handle:
        page.feed(handle.read())
    route = "/" + os.path.relpath(file, dist).replace("index.html", "").replace(os.sep, "/")
    pages[route] = page


def resolve(base, href):
    parts = urlparse(href)
    if parts.scheme or parts.netloc:
        return None
    path = unquote(parts.path) or base
    if not path.startswith("/"):
        joined = os.path.normpath(os.path.join(base, path)).replace(os.sep, "/")
        path = joined + "/" if path.endswith("/") and not joined.endswith("/") else joined
    if not path.endswith("/") and not os.path.splitext(path)[1]:
        path += "/"
    return path, parts.fragment


problems = []
checked = 0
for route, page in sorted(pages.items()):
    for href in page.links:
        target = resolve(route, href)
        if target is None:
            continue
        path, fragment = target
        checked += 1
        if path not in pages:
            if not os.path.exists(dist + path.rstrip("/")):
                problems.append(f"{route}: {href} has no page at {path}")
        elif fragment and fragment not in pages[path].ids:
            problems.append(f"{route}: {href} has no #{fragment} on {path}")

for problem in problems:
    print(problem)
print(f"{len(pages)} pages, {checked} internal links, {len(problems)} broken")
sys.exit(1 if problems else 0)
