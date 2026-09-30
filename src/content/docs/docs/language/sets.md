---
title: Sets
sidebar:
  order: 16
description: Collections in which each value appears once, for asking "have I seen this?" and combining groups.
---

A *set* is a collection in which each value appears at most once. It doesn't keep items by position
or by key; it only remembers whether a value is in it. Adding a value that is already there changes
nothing.

A set is written like a list, with a type that says it is a set:

```emerald
const colors: Set[String] = ["red", "green", "red"]
print(colors)
print(colors.count)
```

```text title="Output"
{"red", "green"}
2
```

The second `"red"` made no difference, so the set has two values. A set prints with braces, so you
can tell it from a list. Without the `Set[String]` type, the same brackets would make a list.

## Is it in the set?

The question a set answers best is whether something is in it:

```emerald
const colors: Set[String] = ["red", "green"]
print(colors.contains?("red"))
print(colors.contains?("blue"))
```

```text title="Output"
true
false
```

A list can answer this too, but it has to look through its items one by one. A set finds the answer
straight away, however many values it holds, which matters for large collections.

A set has no positions, so `colors[0]` is an error that suggests `contains?` instead.

## Adding and removing

A set declared with `var` can change. An empty one is `[]`, with its type:

```emerald
var seen: Set[String] = []
seen.add("Ada")
seen.add("Grace")
seen.add("Ada")
print(seen)
seen.remove("Ada")
print(seen)
```

```text title="Output"
{"Ada", "Grace"}
{"Grace"}
```

A classic use is remembering what has already happened, such as which guesses a player has already
made.

## Removing duplicates from a list

`to_set()` turns a list into a set, dropping repeats:

```emerald
const names = ["Ada", "Bob", "Ada"]
const unique = names.to_set()
print(unique)
print(unique.count)
```

```text title="Output"
{"Ada", "Bob"}
2
```

A list also has `unique()`, which drops repeats but keeps a list, in order.

## Combining sets

Sets can be combined the way groups are in math:

```emerald
const a: Set[Int] = [1, 2, 3]
const b: Set[Int] = [2, 3, 4]
print(a.union(b))          # in either
print(a.intersection(b))   # in both
print(a.difference(b))     # in a but not b
```

```text title="Output"
{1, 2, 3, 4}
{2, 3}
{1}
```

`subset?`, `superset?`, and `disjoint?` compare two sets. Two sets are equal with `==` when they hold
the same values, in any order.

## Going through a set

A `for` loop visits every value, in the order they were first added:

```emerald
const colors: Set[String] = ["red", "green"]
for color in colors {
    print(color)
}
```

```text title="Output"
red
green
```

The [Set](../../builtins/types/set/) reference describes every method.

## What you've learned

- A set holds each value at most once; write it with brackets and a `Set[...]` type.
- `contains?` asks whether a value is in it, quickly, however large it is.
- `add` and `remove` change a `var` set; adding a value that is there already does nothing.
- `to_set()` removes duplicates from a list.
- `union`, `intersection`, and `difference` combine sets.

Next, [tuples](../tuples/): a few values of different types grouped together.
