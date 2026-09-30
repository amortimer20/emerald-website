---
title: Dictionaries
sidebar:
  order: 15
description: Look values up by a key rather than a position, add and change entries, and go through them all.
---

A list finds items by position. A *dictionary* finds them by a *key* you choose, such as a name. Each
entry pairs a key with a value, written `key: value`:

```emerald
const ages = ["Ada": 36, "Grace": 85]
print(ages)
print(ages.count)
```

```text title="Output"
["Ada": 36, "Grace": 85]
2
```

Like a list, a dictionary holds one type of key and one type of value. `ages` is a
`Dict[String, Int]`: keys that are strings, values that are whole numbers.

## Looking up a value

Square brackets look a value up by its key:

```emerald
const ages = ["Ada": 36, "Grace": 85]
print(ages["Ada"])
print(ages["Bob"])
```

```text title="Output"
36
nothing
```

A key that isn't there gives `nothing`, so a lookup is [optional](../optionals/): its type is `Int?`.
That means you have to decide what a missing key means before using the value:

```emerald
const ages = ["Ada": 36]
print(ages["Ada"] + 1)
```

```text title="Output"
dictionaries.em:2:7: addition needs numbers, but this is Int? and Int
  print(ages["Ada"] + 1)
        ^^^^^^^^^^^^^^^
One of these may be absent. Give it a fallback with `.or(0)`, or check it against `nothing` first.
```

Often a fallback is exactly right:

```emerald
const ages = ["Ada": 36]
print(ages["Ada"].or(0) + 1)
print(ages["Bob"].or(0))
```

```text title="Output"
37
0
```

`contains_key?("Bob")` asks whether a key is there without looking up its value.

## Adding and changing entries

A dictionary declared with `var` can change. Assigning to a key adds the entry, or replaces its value
if the key is already there; `remove` takes one out:

```emerald
var ages = ["Ada": 36]
ages["Grace"] = 85     # add
ages["Ada"] = 37       # replace
print(ages)
ages.remove("Ada")
print(ages)
```

```text title="Output"
["Ada": 37, "Grace": 85]
["Grace": 85]
```

A key appears at most once, so assigning to an existing key never makes a second entry.

## An empty dictionary

An empty dictionary is written `[]`, with a type saying what it will hold. It prints as `[:]`, so
you can tell it from an empty list:

```emerald
var stock: Dict[String, Int] = []
print(stock)
stock["apples"] = 3
print(stock)
```

```text title="Output"
[:]
["apples": 3]
```

## Going through every entry

A `for` loop visits each entry, giving the key and the value names of their own:

```emerald
const ages = ["Ada": 36, "Grace": 85]
for (name, age) in ages {
    print("#{name} is #{age}")
}
```

```text title="Output"
Ada is 36
Grace is 85
```

Entries come out in the order they were added. `keys()` and `values()` give lists of just the keys
or just the values.

## A dictionary that counts

Dictionaries are the natural way to count things. Here each word is a key, and its value is how many
times it has appeared so far:

```emerald
const words = "the cat and the hat".split(" ")
var counts: Dict[String, Int] = []
for word in words {
    counts[word] = counts[word].or(0) + 1
}
print(counts)
```

```text title="Output"
["the": 2, "cat": 1, "and": 1, "hat": 1]
```

`counts[word].or(0)` is the count so far, or 0 the first time a word is seen.

## List or dictionary?

- Use a list when order matters and you think of items by position: a queue, a leaderboard, the
  lines of a file.
- Use a dictionary when you look things up by a name or other key: a phone book, stock levels,
  settings.

The [Dict](../../builtins/types/dict/) reference describes every method.

## What you've learned

- A dictionary, `["Ada": 36]`, maps keys to values, one type of each.
- `dict[key]` looks a value up and might be `nothing`; `.or(fallback)` handles a missing key.
- `dict[key] = value` adds or replaces an entry, and `remove(key)` takes one out.
- An empty dictionary is `[]` with a type, and prints as `[:]`.
- `for (key, value) in dict` visits the entries in the order they were added.

Next, [sets](../sets/): collections where each value appears once.
