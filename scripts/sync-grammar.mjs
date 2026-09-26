// Copies emerald-vscode's TextMate grammar into the site, so ```emerald code
// blocks are highlighted exactly as the editor highlights them.
//
//   EMERALD_VSCODE  the emerald-vscode checkout (default: ../emerald-vscode)

import { mkdir, readFile, writeFile } from 'node:fs/promises';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const site = fileURLToPath(new URL('..', import.meta.url));
const emeraldVscode = path.resolve(site, process.env.EMERALD_VSCODE ?? '../emerald-vscode');
const output = path.join(site, 'src/generated/emerald.tmLanguage.json');

const grammar = JSON.parse(await readFile(path.join(emeraldVscode, 'syntaxes/emerald.tmLanguage.json'), 'utf8'));
await mkdir(path.dirname(output), { recursive: true });
await writeFile(output, JSON.stringify({ ...grammar, name: 'emerald' }, null, '\t'));
console.log(`sync-grammar: copied the Emerald grammar from ${emeraldVscode}`);
