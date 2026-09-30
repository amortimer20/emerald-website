---
title: Tuples
sidebar:
  order: 17
description: Group a few values of different types together, unpack them into names, and return two answers from a function.
---

A *tuple* groups a few values together, and unlike a list, they can be of different types: a name and
an age, or a point's x and y. It is written as values in parentheses, separated by commas:

```emerald
const person = ("Ada", 36)
const point = (3, 4)
print(person, point)
```

```text title="Output"
("Ada", 36) (3, 4)
```

A tuple's type lists the type of each position: `person` is a `(String, Int)`. A tuple always has at
least two values, and its size never changes.

## Reading the values

Positions count from 0 and go after a dot:

```emerald
const person = ("Ada", 36)
print(person.0)
print(person.1)
```

```text title="Output"
Ada
36
```

A tuple's size is part of its type, so asking for a position it doesn't have is caught before the
program runs:

```emerald
const point = (3, 4)
print(point.2)
```

```text title="Output"
tuples.em:2:13: (Int, Int) has no position 2
  print(point.2)
              ^
Its positions are `0` through `1`.
```

## Unpacking into names

`person.0` doesn't say much. *Unpacking* gives each position a name of its own:

```emerald
const person = ("Ada", 36)
const (name, age) = person
print("#{name} is #{age}")
```

```text title="Output"
Ada is 36
```

Unpacking works in a `for` loop too, which suits a list of tuples:

```emerald
const scores = [("Ada", 90), ("Grace", 85)]
for (name, score) in scores {
    print("#{name}: #{score}")
}
```

```text title="Output"
Ada: 90
Grace: 85
```

That is also how a `for` loop over a [dictionary](../dictionaries/) names each key and value: every
entry is a tuple.

## Returning two answers

A function returns one value, but that value can be a tuple, which is the usual way to give back two
answers at once:

```emerald
func lowest_and_highest(numbers: List[Int]): (Int, Int) {
    return (numbers.min().or(0), numbers.max().or(0))
}

const (low, high) = lowest_and_highest([4, 9, 2])
print(low, high)
```

```text title="Output"
2 9
```

## Swapping two variables

Unpacking into names that already exist assigns them all at once, which makes swapping two variables a
single line:

```emerald
var a = 1
var b = 2
(a, b) = (b, a)
print(a, b)
```

```text title="Output"
2 1
```

## Tuples don't change

Once made, a tuple can't be changed in place. To change one value, build a new tuple:

```emerald
var point = (3, 4)
point.0 = 5
```

```text title="Output"
tuples.em:2:1: a tuple cannot be changed in place
  point.0 = 5
  ^^^^^^^
Build a new one, as in `pair = (1, pair.1)`.
```

## Tuple or struct?

A tuple is best for a small, short-lived group, such as the two answers from a function. When the
values deserve names and travel around a program, a [struct](../structs/) is clearer: `player.score`
says more than `player.1`.

## What you've learned

- A tuple, `("Ada", 36)`, groups a fixed number of values that can differ in type.
- `tuple.0`, `tuple.1`, and so on read its values; a missing position is caught early.
- `const (a, b) = tuple` unpacks it into names, in declarations and `for` loops alike.
- A function can return a tuple to give back several answers; `(a, b) = (b, a)` swaps.
- A tuple never changes; build a new one instead.

Next, [ranges and slicing](../ranges-and-slicing/): counting through numbers and taking part of a
list or string.
