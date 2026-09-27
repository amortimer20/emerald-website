// @ts-check
import { readFileSync } from 'node:fs';
import { defineConfig } from 'astro/config';
import starlight from '@astrojs/starlight';

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
			logo: { src: './src/assets/emerald.svg' },
			description: 'A programming language for learning to program.',
			social: [{ icon: 'github', label: 'GitHub', href: 'https://github.com/amortimer20/emerald-lang' }],
			expressiveCode: {
				shiki: { langs: [emeraldGrammar()] },
			},
			sidebar: [
				{ label: 'About', slug: 'about' },
				{ label: 'Learn', items: [{ autogenerate: { directory: 'learn' } }] },
				{
					label: 'Docs',
					items: [
						{ label: 'Language Reference', items: [{ autogenerate: { directory: 'docs/language' } }] },
						{
							label: 'Core API',
							items: [
								{ label: 'Overview', slug: 'docs/core' },
								{ label: 'Built-in Functions', collapsed: true, items: [{ autogenerate: { directory: 'docs/core/functions' } }] },
								{ label: 'Types', collapsed: true, items: [{ autogenerate: { directory: 'docs/core/types' } }] },
								{ label: 'Traits', collapsed: true, items: [{ autogenerate: { directory: 'docs/core/traits' } }] },
								{ label: 'Errors', collapsed: true, items: [{ autogenerate: { directory: 'docs/core/errors' } }] },
								{ label: 'Namespaces', collapsed: true, items: [{ autogenerate: { directory: 'docs/core/namespaces' } }] },
							],
						},
						{
							label: 'StdLib API',
							items: [
								{ label: 'Overview', slug: 'docs/stdlib' },
								{ label: 'Files', collapsed: true, items: [{ autogenerate: { directory: 'docs/stdlib/files' } }] },
								{ label: 'Dates and Times', collapsed: true, items: [{ autogenerate: { directory: 'docs/stdlib/dates-and-times' } }] },
								{ label: 'Regular Expressions', collapsed: true, items: [{ autogenerate: { directory: 'docs/stdlib/regex' } }] },
								{ label: 'Console', collapsed: true, items: [{ autogenerate: { directory: 'docs/stdlib/console' } }] },
								{ label: 'JSON', collapsed: true, items: [{ autogenerate: { directory: 'docs/stdlib/json' } }] },
							],
						},
					],
				},
			],
		}),
	],
});
