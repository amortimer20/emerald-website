---
title: Built-ins
description: The parts of Emerald that belong to the language itself.
---

Built-ins are the parts of Emerald that belong to the language itself: the types every
program is written with, a few functions available everywhere, the traits that decide how
values compare and display, and the errors a program raises. They need no import.

- **[Types](types/bool/):** `Bool`, `Int`, `Float`, `String`, `List`, `Dict`, `Set`, tuples,
  `Range`, and `Bytes`.
- **[Functions](functions/print/):** `print`, `write`, `input`, `random`, `exit`, and `assert`.
- **[Traits](traits/equatable/):** `Equatable`, `Hashable`, `Ordered`, and `Textual`, which a
  type adopts to choose how its values compare, sort, and display.
- **[Errors](errors/error/):** `Error`, and Emerald's own `RuntimeError` and `AssertionError`.

The [Standard Library](../library/) holds the tools that come with Emerald, such as files,
dates and times, and JSON.
