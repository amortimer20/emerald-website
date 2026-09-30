---
title: Ranges and Slicing
sidebar:
  order: 18
description: Ranges as values you can store and pass around, counting down and in steps, and taking part of a list or string.
---

[Loops](../loops/) used ranges to count. A range is also a value of its own, a `Range`, which can be
stored, printed, passed to a function, and asked questions:

```emerald
const hours = 0..<24
print(hours)
print(hours.count)
```

```text title="Output"
0..23
24
```

A range prints in its `..` form, which includes both ends: `0..<24` and `0..23` are the same numbers.

## The two kinds of range

- `a..b` counts from `a` up to `b`, including `b`.
- `a..<b` counts from `a` up to, but not including, `b`.

`..<` is the one to use with positions: a list with `count` items has positions `0..<count`. Ranges
count whole numbers only; `1.5..3` is an error.

## Counting down, and in steps

Ranges count upward. Counting down is written in words with `down_to`, which includes its target.
`step` counts by more than one, and `reverse` goes through the same numbers backwards:

```emerald
print((1..10).step(3).to_list())
print(10.down_to(1).step(3).to_list())
print((1..5).reverse().to_list())
```

```text title="Output"
[1, 4, 7, 10]
[10, 7, 4, 1]
[5, 4, 3, 2, 1]
```

`to_list()` turns a range into a list of its numbers, which is handy for seeing what a range will
count. A step says only how far to go, never which way: it must be at least 1, and the range or
`down_to` says the direction.

## Empty ranges are safe

A range whose start is past its end is empty. It counts nothing, and says why when printed:

```emerald
const n = 0
const r = 1..n
print(r)
print(r.empty?())
print(r.count)
```

```text title="Output"
1..0
true
0
```

This is what makes `for i in 1..n` safe when `n` is 0: the loop simply doesn't run. When both ends
are written as numbers, as in `5..1`, the range can only be a mistake, and Emerald points you to
`5.down_to(1)`.

## Passing ranges around

A range can be a parameter like any other value:

```emerald
func total(numbers: Range): Int {
    var sum = 0
    for n in numbers {
        sum += n
    }
    return sum
}

print(total(1..100))
```

```text title="Output"
5050
```

## Slicing lists and strings

A range inside square brackets takes part of a list or string, giving back a new one. Leave off the
start to begin at the beginning, and the end to go to the end:

```emerald
const numbers = [10, 20, 30, 40, 50]
print(numbers[1..3])
print(numbers[..<2])
print(numbers[3..])

const word = "Emerald"
print(word[..<3])
print(word[3..])
```

```text title="Output"
[20, 30, 40]
[10, 20]
[40, 50]
Eme
rald
```

The same rules apply to the ends as in counting: `1..3` includes position 3, and `..<2` stops before
position 2. The original list or string is never changed; the slice is a new one.

An end that goes past the last position is an error, since it names a position that doesn't exist:

```emerald
const numbers = [10, 20, 30]
print(numbers[1..5])
```

```text title="Output"
ranges.em:2:7: slice end 5 is outside this list, which has 3 elements
  print(numbers[1..5])
        ^^^^^^^^^^^^^
An inclusive end must name an existing position.
```

`numbers[1..]` is the safe way to say "from position 1 to the end", whatever the count is.

The [Range](../../builtins/types/range/) reference describes every member.

## What you've learned

- A range is a value: `0..<24` can be stored, printed, and passed to a function.
- `a..b` includes `b` and `a..<b` doesn't; ranges count whole numbers, upward.
- `down_to` counts down, `step` counts by more than one, and `reverse` goes backwards.
- A range that starts past its end is empty, which keeps loops over computed ranges safe.
- `list[a..b]` and `text[a..b]` take a slice; a missing start or end means the beginning or the end.

Next, [structs](../structs/): making types of your own.
