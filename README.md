# Emerald website

The website for the [Emerald](https://github.com/amortimer20/emerald-lang) programming
language, built with [Astro](https://astro.build) and
[Starlight](https://starlight.astro.build).

## Sections

- **About** — `src/content/docs/about.md`.
- **Learn** — `src/content/docs/learn/`, written for this site.
- **Docs** — the Language Reference, Core API, and StdLib API. These pages are written and
  tested in emerald-lang (`docs/language/` and `docs/library/`) and published here by
  `npm run sync`; edit them there, not here.

## Working on the site

The site expects emerald-lang and emerald-vscode checked out beside it:

```text
workspace/
├── emerald-lang/
├── emerald-vscode/
└── emerald-website/
```

```bash
npm install
npm run dev      # syncs the docs, then serves the site at http://localhost:4321
npm run build    # syncs the docs, then builds the static site into dist/
```

`EMERALD_LANG` and `EMERALD_VSCODE` point `npm run sync` at checkouts somewhere else.

`scripts/sync-docs.mjs` copies each page, turns its `# Title` into Starlight frontmatter,
and rewrites its links: a link to another published page becomes a site link, and a link to
anything else in emerald-lang (an example, a conformance case) goes to it on GitHub. Its
section lists decide which API each library page belongs to and the sidebar order; a new
library page missing from them is published under the StdLib API with a warning. Emerald code
is highlighted with emerald-vscode's TextMate grammar.
