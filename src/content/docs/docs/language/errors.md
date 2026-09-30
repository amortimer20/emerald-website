---
title: Errors
sidebar:
  order: 27
description: What happens when something goes wrong while a program runs, how to handle it with try and catch, and how to raise errors of your own.
---

Emerald catches most mistakes before a program runs. Some problems can only appear while it runs,
though: a position that isn't in a list, a file that doesn't exist, a division by a number the user
typed as zero. When one happens, Emerald *raises an error*. If nothing handles it, the program stops
and says what went wrong:

```emerald
const scores = [90, 85]
print(scores[5])
print("never printed")
```

```text title="Output"
errors.em:2:7: index 5 is outside this list, which has 2 elements
  print(scores[5])
        ^^^^^^^^^
Valid indices are 0 through 1.
```

## Handling an error

`try` runs a block, and `catch` says what to do if an error is raised inside it. The program then
carries on after the `catch`, instead of stopping:

```emerald
const scores = [90, 85]
try {
    print(scores[5])
}
catch error: RuntimeError {
    print("Something went wrong: #{error.message}")
}
print("still running")
```

```text title="Output"
Something went wrong: index 5 is outside this list, which has 2 elements
still running
```

`catch error: RuntimeError` names the error `error`, and says which kind of error to catch.
`RuntimeError` is the kind Emerald raises for problems like this one, and `error.message` is its
explanation.

Before reaching for `try`, check whether there is a way that can't fail. For turning typed text into a
number, `to_int_maybe` with a check (see [Optionals](../optionals/)) is usually simpler than catching
the error `to_int` raises. `try` is for problems you can't check for in advance.

## Raising your own errors

A program can raise errors too. Declare a class that extends `Error`, and `raise` one with a message
when something is wrong:

```emerald
class InvalidScore extends Error {
}

func check(score: Int) {
    raise InvalidScore("Score cannot be negative") if score < 0
    print("Score #{score} is fine")
}

check(90)
try {
    check(-5)
}
catch error: InvalidScore {
    print(error.message)
}
```

```text title="Output"
Score 90 is fine
Score cannot be negative
```

When nobody catches it, the program stops, naming the error, where it was raised, and the call that led
there:

```emerald
class InvalidScore extends Error {
}

func check(score: Int) {
    raise InvalidScore("Score cannot be negative") if score < 0
}

check(-5)
```

```text title="Output"
errors.em:5:5: InvalidScore: Score cannot be negative
      raise InvalidScore("Score cannot be negative") if score < 0
      ^^^^^
Handle this error with `try` and `catch`, or correct the condition that raised it.
in `check`, called at errors.em:8:1
```

Giving each kind of problem its own error class lets the code that catches it tell them apart.

## Catching several kinds

A `try` can have several `catch` blocks, one per kind of error. The first one that matches runs:

```emerald
class NotFound extends Error {
}

class TooBig extends Error {
}

func load(n: Int) {
    raise NotFound("no such file") if n == 1
    raise TooBig("file too big") if n == 2
    print("loaded #{n}")
}

for n in 1..3 {
    try {
        load(n)
    }
    catch error: NotFound {
        print("missing: #{error.message}")
    }
    catch error: TooBig {
        print("too big: #{error.message}")
    }
}
```

```text title="Output"
missing: no such file
too big: file too big
loaded 3
```

`catch error` with no kind catches every error. Use it sparingly: catching everything can hide a
mistake you would rather see.

## Errors that carry information

An error class can have fields of its own, set in its constructor after `super(message)`:

```emerald
class LowBalance extends Error {
    const needed: Int

    constructor(needed: Int) {
        super("balance too low")
        self.needed = needed
    }
}

try {
    raise LowBalance(30)
}
catch error: LowBalance {
    print("#{error.message}: need #{error.needed} more")
}
```

```text title="Output"
balance too low: need 30 more
```

## Finally

A `finally` block runs whether the `try` block succeeded or not, which makes it the place to clean up,
such as closing a file:

```emerald
func risky() {
    raise RuntimeError("oops")
}

try {
    risky()
}
catch error: RuntimeError {
    print("caught: #{error.message}")
}
finally {
    print("cleanup always runs")
}
```

```text title="Output"
caught: oops
cleanup always runs
```

`finally` also runs when an error goes uncaught, before the program stops, and a `try` can have a
`finally` without any `catch`.

## Passing an error on

Inside a `catch`, `raise` on its own raises the same error again, for when you want to note that
something happened but still let the caller deal with it:

```emerald
try {
    try {
        raise RuntimeError("inner problem")
    }
    catch error {
        print("logging: #{error.message}")
        raise
    }
}
catch error {
    print("outer got: #{error.message}")
}
```

```text title="Output"
logging: inner problem
outer got: inner problem
```

The standard library's errors, such as `FileError` and `JsonError`, are listed on the
[Built-ins errors](../../builtins/errors/error/) pages and each library's page.

## What you've learned

- A problem while a program runs raises an error; unhandled, it stops the program with a message.
- `try { ... } catch error: Kind { ... }` handles errors of that kind, and the program carries on.
- Prefer a check that can't fail, such as `to_int_maybe`, over catching when you can.
- A class extending `Error` makes a kind of your own; `raise Kind("message")` raises one.
- Several `catch` blocks handle different kinds; `finally` always runs; a bare `raise` passes the
  error on.

Next, [tests](../tests/): checking that your code does what you meant.
