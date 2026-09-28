## Emerald website

Every page is written for this site, slowly and for readers learning Emerald. Do not copy or
sync pages from emerald-lang's `docs/`, which are maintainers' notes. Only the Emerald grammar
(`src/generated/`) is generated, by `npm run sync` from emerald-vscode, and not committed.

## Theme

The site uses an Art Deco theme: emerald green, gold, and cream, after the 1920s and the
retro-futurist Deco of BioShock and The Outer Worlds. The approved mockup is
`public/mockups/deco.html`.

- `src/styles/theme.css` sets Starlight's colours for dark mode (the default) and light mode.
  In light mode, gold is too pale to read as text on cream, so links take emerald and gold
  stays in the ornament.
- Limelight is for display headings only: the site title, page titles, and the landing page.
  Josefin Sans is for labels, navigation, and section headings. Body text keeps the system
  font, and code uses JetBrains Mono. The font URL lives in `src/fonts.mjs`.
- The ornament belongs to the frame of the page, such as rules, labels, and code frames.
  Reference pages stay calm and easy to read (see `src/styles/reference.css`).
- The landing page, `src/pages/index.astro`, stands outside Starlight's layout and is always
  dark. Its examples were run with the emerald binary, so keep them in step with it.

## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)
