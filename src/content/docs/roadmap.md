---
title: Roadmap
description: What Emerald can do today, what is coming next, and the bigger things still being decided.
---

Emerald is in active `0.x` development. This page says where it is and where it is going. These are
plans, not promises: the order can change, and the bigger items are still being decided.

## Today

Emerald is an interpreter with the whole language: functions, optionals, collections, structs,
classes, traits, enums, typed errors, projects, tests, tasks and channels, and a standard library
with files, dates and times, regular expressions, JSON, CSV, HTTP, and more. It comes with a
formatter, a REPL that keeps your session alive, and a language server that completes, explains, and
corrects what you write in Visual Studio Code. Releases are listed on
[GitHub](https://github.com/amortimer20/emerald-lang/releases).

## Next

- **Networking.** Sockets, and a web server to build on, using the same tasks that already let each
  connection run on its own.
- **A package manager.** A way to share Emerald code and use other people's, with versions.
- **A browser playground.** A page where you can try Emerald with nothing to install, so a class on
  school computers can start straight away.

## Later

- **A real compiler.** Emerald's static types are what make a fast language possible, and a native
  compiler is what Emerald 1.0 needs. How to build it, and on what, is still being decided, and will
  be settled by building prototypes.
- **Multicore.** Running tasks at the same time on several processor cores, once the compiler is
  chosen.

## What is not planned

Emerald leaves things out on purpose, so that what it has stays easy to learn and to read. It does not
plan to add `null`, operator spellings such as `&&` and `||` alongside `and` and `or`, or several
ways to write the same thing. Ideas to improve what is there are welcome on
[GitHub](https://github.com/amortimer20/emerald-lang/issues).
