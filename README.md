# Emerald website

The website for the [Emerald](https://github.com/amortimer20/emerald-lang) programming
language, built with [Astro](https://astro.build) and
[Starlight](https://starlight.astro.build).

## Sections

- **About** — `src/content/docs/about.md`.
- **Learn** — `src/content/docs/learn/`.
- **Docs** — `src/content/docs/docs/`: the Language Reference, Built-ins, and Standard Library.

Every page is written for this site. emerald-lang's own `docs/` are maintainers' notes and
are not published here.

## Working on the site

The site expects emerald-vscode checked out beside it, for its Emerald grammar:

```text
workspace/
├── emerald-vscode/
└── emerald-website/
```

```bash
npm install
npm run dev      # copies the grammar, then serves the site at http://localhost:4321
npm run build    # copies the grammar, then builds the static site into dist/
```

`EMERALD_VSCODE` points `npm run sync` at a checkout somewhere else.
