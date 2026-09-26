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
						{ label: 'Core API', items: [{ autogenerate: { directory: 'docs/core' } }] },
						{ label: 'StdLib API', items: [{ autogenerate: { directory: 'docs/stdlib' } }] },
					],
				},
			],
		}),
	],
});
