---
title: Roadmap
description: What Emerald can do today, what is coming next, and the bigger things still being decided.
---

Emerald is in active `0.x` development. This page says where it is and where it is going. These are
plans, not promises: the order can change, and the bigger items are still being decided.

## Today

Emerald is an interpreter with the whole language: functions, optionals, collections, structs,
classes, traits, enums whose values can carry data, generics, typed errors, projects, tests, tasks
and channels, and a standard library with files, dates and times, regular expressions, JSON, CSV,
HTTP, and more. Code is shared by [copying a library's folder](../docs/language/sharing-code/)
into a project, with no package manager. It comes with a
formatter, a REPL that keeps your session alive, and a language server that completes, explains, and
corrects what you write in Visual Studio Code. Releases are listed on
[GitHub](https://github.com/amortimer20/emerald-lang/releases).

## Next

- **A review of the whole interpreter.** Every crash, wrong answer, and untested rule found and
  fixed, so the interpreter is a contract the compiler can be checked against.
- **A real compiler.** Emerald's static types are what make a fast language possible, and a native
  compiler is what Emerald 1.0 needs. Emerald is written in Zig, and the compiler will be too. How
  it turns a program into something fast is still being decided, and will be settled by building
  prototypes.

## Later

- **Graphics, games, and sound.** Libraries for drawing, games, and audio that come with Emerald,
  written for beginners and built on a proven engine. How they look is still being designed.
- **Emerald 1.0.** The compiler and the complete standard library, together.

## After 1.0

- **A browser playground.** A page where you can try Emerald with nothing to install, so a class on
  school computers can start straight away.
- **Multicore.** Running tasks at the same time on several processor cores.
- **A debugger.** Stepping through an Emerald program one line at a time.

## What is not planned

Emerald leaves things out on purpose, so that what it has stays easy to learn and to read. It does not
plan to add a package manager, `null`, operator spellings such as `&&` and `||` alongside `and` and `or`, or several
ways to write the same thing. Ideas to improve what is there are welcome on
[GitHub](https://github.com/amortimer20/emerald-lang/issues).
