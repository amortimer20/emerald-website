---
title: Operators
sidebar:
  order: 7
description: Every operator in one place, grouped by what it does, and the order in which Emerald works them out.
---

The earlier pages introduced operators as they came up. This page gathers them in one place, so it
is also a page to come back to.

## Arithmetic

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `+` | add | `7 + 2` | `9` |
| `-` | subtract | `7 - 2` | `5` |
| `*` | multiply | `7 * 2` | `14` |
| `/` | divide, always giving a `Float` | `7 / 2` | `3.5` |
| `//` | divide and round down | `7 // 2` | `3` |
| `%` | the remainder after `//` | `7 % 2` | `1` |
| `**` | raise to a power | `2 ** 10` | `1024` |
| `-` (in front) | negate | `-(3 + 4)` | `-7` |

`+` also joins two strings. [Numbers](../numbers/) explains division, mixing `Int` and `Float`, and
what happens on overflow.

## Comparison

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `==` | equal | `3 == 3` | `true` |
| `!=` | not equal | `3 != 4` | `true` |
| `<` `<=` | less than, or equal | `3 < 5` | `true` |
| `>` `>=` | greater than, or equal | `5 >= 5` | `true` |

Comparisons can be chained: `0 <= score <= 100` asks whether `score` is in that range. See
[Booleans and Comparison](../booleans-and-comparison/).

## Logic

| Operator | Meaning | Example | Result |
| --- | --- | --- | --- |
| `and` | both are true | `true and false` | `false` |
| `or` | at least one is true | `true or false` | `true` |
| `not` | the opposite | `not true` | `false` |

`and` and `or` stop as soon as the answer is known.

## Assignment

Assignment is a statement of its own, never part of an expression, so it can't be confused with
`==` inside a condition.

| Operator | Meaning | Same as |
| --- | --- | --- |
| `=` | give a new value | |
| `+=` | add to | `x = x + y` |
| `-=` | subtract from | `x = x - y` |
| `*=` | multiply by | `x = x * y` |
| `/=` | divide by | `x = x / y` |
| `//=` | divide and round down | `x = x // y` |

```emerald
var seconds = 200
seconds //= 60
print(seconds)
```

```text title="Output"
3
```

## Other operators

These belong to ideas that later pages explain; they are listed here so the table is complete.

| Operator | Meaning | Explained in |
| --- | --- | --- |
| `a..b`, `a..<b` | a range from `a` through `b`, or up to but not including `b` | [Ranges and Slicing](../ranges-and-slicing/) |
| `x is Type` | whether a value is of a type | [Optionals](../optionals/), [Inheritance](../inheritance/) |
| `thing.name` | a member of a value, such as a method or property | [Text](../text/), [Structs](../structs/) |
| `thing?.name` | a member, if the value is there | [Optionals](../optionals/) |
| `f(x)` | call a function | [Functions](../functions/) |
| `list[i]` | an item by position | [Lists](../lists/) |
| `if c then a else b` | one of two values | [If and Else](../if-and-else/) |

## The order operators are worked out in

When an expression has several operators, the ones higher in this list go first. Operators on the
same line go from left to right, except `**`, which goes right to left.

1. `f(x)`, `list[i]`, `thing.name`, `thing?.name`
2. `**`
3. `-` in front of a value
4. `*`, `/`, `//`, `%`
5. `+`, `-`
6. `..`, `..<`
7. `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`
8. `not`
9. `and`
10. `or`
11. `if ... then ... else`

So `2 + 3 * 4` is `14`, since `*` comes before `+`, and `not a == b` means `not (a == b)`. `and` comes
before `or`, so `true or false and false` is `true or (false and false)`, which is `true`:

```emerald
print(2 + 3 * 4)
print(true or false and false)
print(1 + 1..2 + 2)
```

```text title="Output"
14
true
2..4
```

The last line is `(1 + 1)..(2 + 2)`, because arithmetic comes before a range.

Two cases often surprise people. `-2 ** 2` is `-4`, because `**` comes before the minus sign, as it
does in math; write `(-2) ** 2` for `4`. And `2 ** 3 ** 2` is `2 ** 9`, because `**` goes right to
left.

When an expression mixes several levels, parentheses make it clear to the reader, even when they
don't change the answer.

## What Emerald doesn't have

If you know another language, some familiar operators are missing on purpose:

- `&&`, `||`, and `!` are spelled `and`, `or`, and `not`.
- `++` and `--` don't exist; write `count += 1`.
- `%=` and `**=` don't exist; write `x = x % y` and `x = x ** y`.
- There is no `? :`; write `if c then a else b`.
- `in` isn't an operator; a list answers with `list.contains?(item)`.

## What you've learned

- Arithmetic, comparison, and logic operators, and the assignment shortcuts, are all in the tables
  above.
- Operators higher in the order are worked out first; parentheses override the order and make it
  plain.

Next, [if and else](../if-and-else/): making decisions.
