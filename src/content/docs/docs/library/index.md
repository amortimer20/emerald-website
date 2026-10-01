---
title: Standard Library
description: The tools that come with Emerald, such as files, dates and times, and JSON.
---

The standard library is the set of tools that come with Emerald, for jobs most programs end up
needing: reading and writing files, working with dates, matching patterns in text, talking to
the web. Like the [built-ins](../builtins/), they need no import; every one is already there
when a program starts.

- **[Math, Program, and Random](program/math/):** [`Math`](program/math/) for constants,
  trigonometry, logarithms, and powers; [`Program`](program/program/) for the running program's
  own command-line arguments, and pausing it; and [`Random`](program/random/) for seeded random
  numbers.
- **[Files](files/file/):** `File` and `Directory` to read, write, and list; `Path` for working
  with file names; `FileHandle` and `FileWriter` for streaming; and `FileError`.
- **[Dates and Times](dates-and-times/date/):** `Date`, `Time`, `DateTime`, `Instant`,
  `Duration`, `TimeZone`, `Weekday`, `Stopwatch`, and `DateTimeError`.
- **[Regular Expressions](regex/regex/):** `Regex` and `Regex.Match`, to find, replace, and
  split text by pattern, and `RegexError`.
- **[Console](console/console/):** `Console` and `Console.Color`, for styled output, tables,
  and prompts.
- **[JSON](json/json/):** `Json`, `Json.Kind`, and `JsonError`, to read and write JSON text.
- **[HTTP](http/http/):** `Http` and `Http.Response`, to make web requests, and `HttpError`.

A name that a program declares itself always wins over one of these, so a program with its own
`File` still works. The library's version stays reachable as `Emerald.File`; see
[Projects and Namespaces](../language/projects-and-namespaces/).
