// Copies Emerald's reference documentation into the site. The pages are
// written and tested in the emerald-lang repository, next to the behavior
// they describe; this site only publishes them, so nothing under the
// generated directories below is edited or committed here.
//
//   EMERALD_LANG    the emerald-lang checkout (default: ../emerald-lang)
//   EMERALD_VSCODE  the emerald-vscode checkout (default: ../emerald-vscode),
//                   whose TextMate grammar highlights ```emerald blocks

import { mkdir, readFile, readdir, rm, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const site = fileURLToPath(new URL('..', import.meta.url));
const emeraldLang = path.resolve(site, process.env.EMERALD_LANG ?? '../emerald-lang');
const emeraldVscode = path.resolve(site, process.env.EMERALD_VSCODE ?? '../emerald-vscode');
const repository = 'https://github.com/amortimer20/emerald-lang';

const contentRoot = path.join(site, 'src/content/docs');
const generatedGrammar = path.join(site, 'src/generated/emerald.tmLanguage.json');

// Each section's pages, in sidebar order. A README becomes its section's
// first page. A library page missing from both API lists is published under
// the StdLib API with a warning, so a new library is never silently dropped.
const sections = [
	{
		output: 'docs/language',
		source: 'docs/language',
		pages: ['README', 'core', 'types-and-optionals', 'collections-and-ranges', 'objects-and-traits', 'errors-tests-and-projects', 'diagnostics'],
	},
	{
		output: 'docs/core',
		source: 'docs/library',
		pages: ['README', 'inventory', 'prelude', 'int', 'float', 'string', 'list', 'dict', 'set', 'tuples', 'range', 'bytes', 'math', 'random', 'program', 'errors'],
	},
	{
		output: 'docs/stdlib',
		source: 'docs/library',
		pages: ['file', 'path', 'dates-and-times', 'date', 'time', 'date-time', 'instant', 'duration', 'time-zone', 'stopwatch', 'regex', 'console'],
		catchAll: true,
	},
];

// Where each published page's source is, and the page it becomes:
// "docs/library/list.md" -> "docs/core/list".
const published = new Map();

async function plan() {
	for (const section of sections) {
		for (const page of section.pages) {
			published.set(`${section.source}/${page}.md`, pageSlug(section, page));
		}
	}
	const library = await readdir(path.join(emeraldLang, 'docs/library'));
	const stdlib = sections.find((section) => section.catchAll);
	for (const file of library.filter((name) => name.endsWith('.md')).sort()) {
		const source = `docs/library/${file}`;
		if (published.has(source)) continue;
		const page = file.slice(0, -'.md'.length);
		console.warn(`sync-docs: ${source} is in neither API list; publishing it under the StdLib API`);
		stdlib.pages.push(page);
		published.set(source, pageSlug(stdlib, page));
	}
}

function pageSlug(section, page) {
	return page === 'README' ? section.output : `${section.output}/${page}`;
}

function pageUrl(slug) {
	return `/${slug}/`;
}

// A link written for GitHub, relative to the page's own place in emerald-lang,
// made to work on the site: another published page becomes a relative site
// link, and anything else in the repository (an example, a conformance case)
// a link to it on GitHub.
function rewriteLink(target, sourcePath, slug) {
	if (/^[a-z]+:/i.test(target) || target.startsWith('#')) return target;
	const hashAt = target.indexOf('#');
	const file = hashAt < 0 ? target : target.slice(0, hashAt);
	const anchor = hashAt < 0 ? '' : target.slice(hashAt);
	const resolved = path.posix.normalize(path.posix.join(path.posix.dirname(sourcePath), file));
	const directory = file.endsWith('/') || file === '';
	const candidate = directory ? `${resolved.replace(/\/$/, '')}/README.md` : resolved;
	const destination = published.get(candidate);
	if (destination) {
		const relative = path.posix.relative(pageUrl(slug), pageUrl(destination));
		return `${relative === '' ? '.' : relative}/${anchor}`;
	}
	const kind = directory ? 'tree' : 'blob';
	return `${repository}/${kind}/main/${resolved.replace(/\/$/, '')}${anchor}`;
}

function convert(markdown, sourcePath, slug, order) {
	const lines = markdown.split('\n');
	const headingAt = lines.findIndex((line) => line.startsWith('# '));
	if (headingAt < 0) throw new Error(`${sourcePath} has no "# " title`);
	const title = lines[headingAt].slice(2).trim();
	lines.splice(headingAt, 1);

	// Links are rewritten outside fenced code only.
	let fenced = false;
	const body = lines.map((line) => {
		if (/^\s*```/.test(line)) fenced = !fenced;
		if (fenced) return line;
		return line.replace(/\]\(([^)\s]+)\)/g, (_, target) => `](${rewriteLink(target, sourcePath, slug)})`);
	});

	const frontmatter = [
		'---',
		`title: ${JSON.stringify(title)}`,
		`sidebar:`,
		`  order: ${order}`,
		`editUrl: ${JSON.stringify(`${repository}/edit/main/${sourcePath}`)}`,
		'---',
		'',
	];
	return frontmatter.join('\n') + body.join('\n').replace(/^\n+/, '');
}

async function publish() {
	for (const section of sections) {
		await rm(path.join(contentRoot, section.output), { recursive: true, force: true });
	}
	let count = 0;
	for (const section of sections) {
		for (const [order, page] of section.pages.entries()) {
			const sourcePath = `${section.source}/${page}.md`;
			const slug = published.get(sourcePath);
			const markdown = await readFile(path.join(emeraldLang, sourcePath), 'utf8');
			const output = path.join(contentRoot, page === 'README' ? `${slug}/index.md` : `${slug}.md`);
			await mkdir(path.dirname(output), { recursive: true });
			await writeFile(output, convert(markdown, sourcePath, slug, order));
			count += 1;
		}
	}
	await mkdir(path.dirname(generatedGrammar), { recursive: true });
	const grammar = JSON.parse(await readFile(path.join(emeraldVscode, 'syntaxes/emerald.tmLanguage.json'), 'utf8'));
	await writeFile(generatedGrammar, JSON.stringify({ ...grammar, name: 'emerald' }, null, '\t'));
	console.log(`sync-docs: published ${count} pages from ${emeraldLang}`);
}

await plan();
await publish();
