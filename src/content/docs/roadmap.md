---
title: Roadmap
description: What Emerald can do today, what is coming next, and the bigger things still being decided.
---

Emerald is in active `0.x` development. This page says where it is and where it is going. These are
plans, not promises: the order can change, and the bigger items are still being decided.

## Today

Emerald is an interpreter with the whole language: functions, optionals, collections, structs,
classes, traits, enums, typed errors, projects, tests, and a standard library with files, dates and
times, regular expressions, JSON, CSV, HTTP, and more. It comes with a formatter, a REPL, and a
language server. Releases are listed on
[GitHub](https://github.com/amortimer20/emerald-lang/releases).

## Next

- **The 0.7 release.** Console tables, panels, and prompts, a clearer error when input ends, and
  tasks and channels: a way to let work wait at the same time without threads, locks, `async`, or
  `await`. These are already written, and the reference documents them, but they are not in a
  release yet.
- **A better REPL.** The current one replays your whole session on every line, so a file write or a
  web request would happen again. The new one will keep the session alive, and show the result of
  every expression, as people expect.
- **Better editor support.** Completion and hover already work, but they are shallow for the
  built-in types. They will learn what a `List`, a `String`, or a `Task` can do.
- **A quality pass.** A deliberate round of using Emerald the way a new person would, fixing the
  rough edges and unhelpful messages found along the way.

## Later

- **A real compiler.** Emerald's static types are what make a fast language possible, and a native
  compiler is what Emerald 1.0 needs. How to build it, and on what, is still being decided, and will
  be settled by building prototypes.
- **Networking.** Sockets, and a web server to build on, using the same tasks that already let each
  connection run on its own.
- **A package manager.** A way to share Emerald code and use other people's, with versions.
- **Multicore.** Running tasks at the same time on several processor cores, once the compiler is
  chosen.

## What is not planned

Emerald leaves things out on purpose, so that what it has stays easy to learn and to read. It does not
plan to add `null`, operator spellings such as `&&` and `||` alongside `and` and `or`, or several
ways to write the same thing. Ideas to improve what is there are welcome on
[GitHub](https://github.com/amortimer20/emerald-lang/issues).
