// @ts-check
import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';
import { FONTS } from './src/fonts.mjs';

// The Art Deco syntax themes, in the colours of the landing page's code.
function decoTheme(name) {
	return JSON.parse(readFileSync(new URL(`./src/themes/${name}.json`, import.meta.url), 'utf8'));
}

// Written by `npm run sync` (scripts/sync-grammar.mjs) from emerald-vscode.
function emeraldGrammar() {
	try {
		return JSON.parse(readFileSync(new URL('./src/generated/emerald.tmLanguage.json', import.meta.url), 'utf8'));
	} catch {
		throw new Error('The Emerald grammar is missing: run `npm run sync` first.');
	}
}

export default defineConfig({
	integrations: [
		starlight({
			title: 'Emerald',
			logo: { src: './src/assets/emerald-deco.svg' },
			description: 'A programming language for learning to program.',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/amortimer20/emerald-lang' }],
			head: [
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.googleapis.com' } },
				{ tag: 'link', attrs: { rel: 'preconnect', href: 'https://fonts.gstatic.com', crossorigin: true } },
				{ tag: 'link', attrs: { rel: 'stylesheet', href: FONTS } },
			],
			customCss: ['./src/styles/theme.css', './src/styles/reference.css'],
			expressiveCode: {
				themes: [decoTheme('deco-dark'), decoTheme('deco-light')],
				shiki: { langs: [emeraldGrammar()] },
				styleOverrides: { borderRadius: '0.3rem', frames: { frameBoxShadowCssValue: 'none' } },
			},
			sidebar: [
				{ label: 'About', slug: 'about' },
				{ label: 'Install', slug: 'install' },
				{
					label: 'Docs',
					items: [
						{ label: 'Language Reference', items: [{ autogenerate: { directory: 'docs/language' } }] },
						{
							label: 'Built-ins',
							items: [
								{ label: 'Overview', slug: 'docs/builtins' },
								{ label: 'Functions', collapsed: true, items: [{ autogenerate: { directory: 'docs/builtins/functions' } }] },
								{ label: 'Types', collapsed: true, items: [{ autogenerate: { directory: 'docs/builtins/types' } }] },
								{ label: 'Traits', collapsed: true, items: [{ autogenerate: { directory: 'docs/builtins/traits' } }] },
								{ label: 'Errors', collapsed: true, items: [{ autogenerate: { directory: 'docs/builtins/errors' } }] },
							],
						},
						{
							label: 'Standard Library',
							items: [
								{ label: 'Overview', slug: 'docs/library' },
								{ label: 'Math, Program, and Random', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/program' } }] },
								{ label: 'Files', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/files' } }] },
								{ label: 'Dates and Times', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/dates-and-times' } }] },
								{ label: 'Regular Expressions', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/regex' } }] },
								{ label: 'Console', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/console' } }] },
								{ label: 'JSON', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/json' } }] },
								{ label: 'CSV', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/csv' } }] },
								{ label: 'Base64 and Digest', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/encoding' } }] },
								{ label: 'HTTP', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/http' } }] },
								{ label: 'Tasks and Channels', collapsed: true, items: [{ autogenerate: { directory: 'docs/library/tasks' } }] },
							],
						},
					],
				},
			],
		}),
	],
});
