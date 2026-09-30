---
title: Numbers
sidebar:
  order: 4
description: Whole numbers and fractional ones, arithmetic and its order, and what happens at the edges.
---

Emerald has two kinds of number. An `Int` is a whole number, such as `42` or `-7`. A `Float` is a
number that can have a fractional part, such as `3.14` or `0.5`. A number with a decimal point is a
`Float`; one without is an `Int`.

```emerald
const players = 4       # an Int
const price = 2.50      # a Float
print(players, price)
```

```text title="Output"
4 2.5
```

Use an `Int` for things you count, and a `Float` for things you measure.

## Arithmetic

The usual operators work on both kinds:

```emerald
print(7 + 2)     # add
print(7 - 2)     # subtract
print(7 * 2)     # multiply
print(2 ** 10)   # raise to a power
```

```text title="Output"
9
5
14
1024
```

## Three kinds of division

Dividing whole numbers raises a question: what is 7 divided by 2? Emerald gives you a way to ask
for each answer.

- `/` always gives the exact answer, as a `Float`, even when both numbers are whole.
- `//` divides and rounds down to a whole number.
- `%` gives the remainder left over after `//`.

```emerald
print(7 / 2)
print(8 / 2)
print(7 // 2)
print(7 % 2)
```

```text title="Output"
3.5
4.0
3
1
```

`8 / 2` is `4.0`, not `4`: `/` always gives a `Float`, and a whole `Float` always keeps its `.0`
so you can tell it from an `Int`.

`%` is handier than it looks. `n % 2` is `0` exactly when `n` is even, and `minutes % 60` is what
is left after taking out the whole hours.

## Mixing the two kinds

When an `Int` meets a `Float`, the answer is a `Float`:

```emerald
print(2 + 0.5)
print(3 * 1.5)
```

```text title="Output"
2.5
4.5
```

Wherever a `Float` is expected, an `Int` is accepted and becomes one, so `var price: Float = 3`
holds `3.0`. The other way round needs a decision about the fraction, so Emerald makes you say
which you want:

```emerald
const x = 3.7
print(x.round())      # nearest whole number
print(x.floor())      # round down
print(x.ceil())       # round up
print(x.truncate())   # drop the fraction
```

```text title="Output"
4
3
4
3
```

The [Float](../../builtins/types/float/) page lists every way to round and convert.

## The order of operations

Emerald follows the order you learned in math: `**` first, then `*`, `/`, `//`, and `%`, then `+`
and `-`. Parentheses go first of all.

```emerald
print(2 + 3 * 4)
print((2 + 3) * 4)
print(10 - 4 - 3)
```

```text title="Output"
14
20
3
```

Operators of the same kind work left to right, so `10 - 4 - 3` is `(10 - 4) - 3`. The exception is
`**`, which works right to left, as it does in math: `2 ** 3 ** 2` is `2 ** 9`, which is `512`.

A minus sign written against a number is part of the number, so `-3.abs()` is `3`. With `**`, the
power still comes first: `-2 ** 2` is `-(2 ** 2)`, which is `-4`. When in doubt, add parentheses;
they cost nothing and make the meaning plain.

## Writing numbers

- A long number can use underscores to group its digits: `1_000_000` is one million.
- Very large or very small `Float`s can be written in scientific notation: `6.02e23` is 6.02 × 10²³.
- Numbers are written in decimal. Emerald doesn't have hexadecimal (`0xFF`), octal, or binary
  literals, and says so if you try one.

## At the edges

Dividing by zero has no answer, so it is an error rather than a strange result:

```emerald
print(5 // 0)
```

```text title="Output"
numbers.em:1:7: floor division by zero
  print(5 // 0)
        ^^^^^^
Check the divisor before dividing. Division by zero has no result for either numeric type.
```

An `Int` holds whole numbers up to about nine quintillion (9,223,372,036,854,775,807). An answer
too big to fit is an error, never a wrong number:

```emerald
print(9223372036854775807 + 1)
```

```text title="Output"
numbers.em:1:7: addition of 9223372036854775807 and 1 overflows Int
  print(9223372036854775807 + 1)
        ^^^^^^^^^^^^^^^^^^^^^^^
`Int` holds whole numbers from -9223372036854775808 through 9223372036854775807.
```

A `Float` is stored approximately, as in every programming language, so some simple-looking sums
come out slightly off:

```emerald
print(0.1 + 0.2)
```

```text title="Output"
0.30000000000000004
```

This isn't a bug in Emerald; it is how fractions are stored in a computer's binary arithmetic.
Round a `Float` when you show it, with `round_to` or `format`, and don't compare two calculated
`Float`s for exact equality. For money, count in cents with an `Int`.

## What you've learned

- An `Int` is a whole number; a `Float` can have a fraction. A decimal point makes a `Float`.
- `+`, `-`, `*`, and `**` do what you'd expect; `/` always gives a `Float`, `//` rounds down, and
  `%` gives the remainder.
- An `Int` and a `Float` together give a `Float`; turning a `Float` into an `Int` means choosing how
  to round.
- Operations follow math's order, and parentheses make it plain.
- Dividing by zero and overflowing an `Int` are errors; `Float` arithmetic is approximate.

The built-in [Int](../../builtins/types/int/) and [Float](../../builtins/types/float/) pages list
everything numbers can do. Next, [text](../text/): strings, and the many things they can do.
