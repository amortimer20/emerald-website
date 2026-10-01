---
title: Booleans and Comparison
sidebar:
  order: 6
description: True and false, the questions a program asks with comparisons, and combining answers with and, or, and not.
---

A program makes decisions by asking yes-or-no questions: is the score above 100? Is the list
empty? The answer to such a question is a `Bool`, which has exactly two values, `true` and
`false`.

```emerald
const is_raining = false
const game_over = true
print(is_raining, game_over)
```

```text title="Output"
false true
```

## Comparing values

A comparison asks a question about two values and gives a `Bool`:

| Operator | Question | Example | Answer |
| --- | --- | --- | --- |
| `==` | equal? | `3 == 3` | `true` |
| `!=` | not equal? | `3 != 3` | `false` |
| `<` | less than? | `3 < 5` | `true` |
| `<=` | less than or equal? | `5 <= 5` | `true` |
| `>` | greater than? | `3 > 5` | `false` |
| `>=` | greater than or equal? | `5 >= 3` | `true` |

```emerald
const score = 120
print(score > 100)
print(score == 50)
```

```text title="Output"
true
false
```

`==` has two equals signs: one `=` gives a variable a value, and two ask whether two values are the
same.

Numbers compare as you'd expect, and an `Int` and a `Float` compare with each other, so `1 == 1.0`
is `true`. Strings compare alphabetically with `<` and `>`, and exactly with `==`, so `"a" == "A"`
is `false`.

## Asking whether a value is in a range

To ask whether a value is between two others, write the comparisons in a row:

```emerald
const score = 75
print(0 <= score <= 100)
```

```text title="Output"
true
```

That reads the way you'd say it, "score is between 0 and 100", and means
`0 <= score and score <= 100`.

## Combining answers

Three words combine `Bool`s:

- `a and b` is `true` when both are `true`.
- `a or b` is `true` when at least one is `true`.
- `not a` is the opposite of `a`.

```emerald
const age = 15
const has_ticket = true
print(age >= 13 and has_ticket)
print(age < 13 or not has_ticket)
```

```text title="Output"
true
false
```

Emerald spells these as words. If you know a language that writes `&&`, `||`, and `!`, those aren't
a second spelling here; `!=` is still "not equal".

`and` and `or` stop as soon as they know the answer. In `false and anything`, the answer is already
`false`, so `anything` is never worked out:

```emerald
func check(): Bool {
    print("checking...")
    return true
}

print(false and check())
print(true or check())
```

```text title="Output"
false
true
```

`check` never runs, so `checking...` never prints. This matters when the right side would fail
without the left: `count > 0 and total / count > 10` never divides by zero, because a zero `count`
stops it first. (Functions are explained on the [functions](../functions/) page.)

## Only a Bool is true or false

Some languages treat `0`, an empty string, or an empty list as false. Emerald doesn't: a condition
has to be a real `Bool`, so the question is always written out.

```emerald
const count = 3
if count {
    print("some")
}
```

```text title="Output"
booleans.em:2:4: a condition must be a Bool, but this is Int
  if count {
     ^^^^^
Compare it to something, as in `count > 0`. Emerald has no truthy or falsey values.
```

Write `if count > 0` instead. Likewise, values of different types can't be compared, because the
answer would only ever be `false`:

```emerald
print(1 == "1")
```

```text title="Output"
booleans.em:1:7: Int and String cannot be compared
  print(1 == "1")
        ^^^^^^^^
`==` and `!=` compare two values of the same type, and Int and Float compare with each other.
```

Convert one first: `1 == "1".to_int()` is `true`.

## Questions that end in ?

A method whose name ends in `?` answers a yes-or-no question and gives a `Bool`:

```emerald
print("".empty?())
print("Emerald".starts_with?("Em"))
print(7.even?())
```

```text title="Output"
true
true
false
```

The `?` is part of the name, and it is how you can tell at a glance that the answer is `true` or
`false`.

## What you've learned

- A `Bool` is `true` or `false`, the answer to a yes-or-no question.
- `==`, `!=`, `<`, `<=`, `>`, and `>=` compare values; `0 <= x <= 100` asks for a range.
- `and`, `or`, and `not` combine answers, and `and` and `or` stop as soon as they know the answer.
- A condition must be a real `Bool`, and only values of the same type can be compared.
- A method ending in `?` answers a yes-or-no question.

Next, [operators](../operators/): every operator in one place, and the order they are worked
out in.
