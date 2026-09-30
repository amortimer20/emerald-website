---
title: Tests
sidebar:
  order: 28
description: Check that your code does what you meant with assert, write test functions with @test, and run them all with emerald test.
---

Running a program and reading what it prints tells you whether it works today. A *test* is a small
piece of code that does the checking for you, so you can check again after every change without
reading anything.

## assert

`assert` checks that something is true. If it is, nothing happens. If it isn't, the program stops and
shows what failed:

```emerald
const score = -2
assert score >= 0, "score must not be negative"
print("never printed")
```

```text title="Output"
tests.em:2:8: AssertionError: assertion failed: `score >= 0`
  assert score >= 0, "score must not be negative"
         ^^^^^^^^^^
score must not be negative
```

The message after the comma is optional, and is shown when the check fails. When the check is an `==`,
Emerald shows both sides, as you'll see below.

## Test functions

A test is a function marked `@test`. It takes no parameters, gives back nothing, and uses `assert` to
check a result:

```emerald
func clamp(value: Int, low: Int, high: Int): Int {
    return low if value < low
    return high if value > high
    return value
}

@test
func clamps_high_values() {
    assert clamp(15, 0, 10) == 10
}

@test
func clamps_low_values() {
    assert clamp(-3, 0, 10) == 0
}

@test
func keeps_values_in_range() {
    assert clamp(5, 0, 10) == 5
}

print("the program is running")
```

`emerald test tests.em` runs every test in the file, and reports:

```text title="emerald test"
3 tests passed.
```

The `print` at the end didn't run. `emerald test` uses the file's functions and types, but not the
statements that make up the program, so testing never starts the program itself. `emerald run` still
runs the program as usual, and skips the tests.

Name each test for what it checks. When one fails, its name is the first thing you read.

## When a test fails

Suppose the last test expected the wrong answer:

```emerald
func clamp(value: Int, low: Int, high: Int): Int {
    return low if value < low
    return high if value > high
    return value
}

@test
func clamps_high_values() {
    assert clamp(15, 0, 10) == 10
}

@test
func keeps_values_in_range() {
    assert clamp(5, 0, 10) == 6
}
```

```text title="emerald test"
tests.em:14:12: test `keeps_values_in_range` failed: AssertionError: assertion failed: `clamp(5, 0, 10) == 6`
      assert clamp(5, 0, 10) == 6
             ^^^^^^^^^^^^^^^^^^^^
Left was 5; right was 6.
in `keeps_values_in_range`, called at tests.em:13:6
2 tests, 1 failed.
```

The report names the test, shows the check, and gives both sides of the `==`. Whether the mistake is in
the code or in the test, you can see it at once. A failing test doesn't stop the others: every test
runs, and the last line counts them.

A test also fails if an error is raised inside it and not caught, such as an index outside a list.

## Testing that an error is raised

Sometimes the right result is an error. Call the code inside `try`, and put `assert false` after the
call, so the test fails if the call returns normally instead:

```emerald
class InvalidScore extends Error {
}

func check(score: Int) {
    raise InvalidScore("Score cannot be negative") if score < 0
}

@test
func rejects_negative_scores() {
    try {
        check(-5)
        assert false, "expected an InvalidScore error"
    }
    catch error: InvalidScore {
        assert error.message == "Score cannot be negative"
    }
}
```

```text title="emerald test"
1 test passed.
```

## Tests in a project

In a project of several files, `emerald test main.em` finds the tests in every file of the project, so
tests can live beside the code they check, or in files of their own.
[Projects and namespaces](../projects-and-namespaces/) explains how a project is put together.

## What you've learned

- `assert condition` stops with a report when the condition is false; `, "message"` explains why.
- A function marked `@test`, with no parameters and no result, is a test.
- `emerald test` runs every test, without running the program's own statements.
- A failing `==` shows both sides, and every test runs even when one fails.
- `try`, `assert false`, and `catch` together test that an error is raised.

Next, [projects and namespaces](../projects-and-namespaces/): growing a program beyond one file.
