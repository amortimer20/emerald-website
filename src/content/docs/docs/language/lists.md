---
title: Lists
sidebar:
  order: 14
description: Keep many values in order, read and change them by position, and work with the whole list at once.
---

A list keeps several values in order. It is written as values between square brackets, separated by
commas:

```emerald
const fruits = ["apple", "banana", "cherry"]
print(fruits)
print(fruits.count)
```

```text title="Output"
["apple", "banana", "cherry"]
3
```

`count` says how many items a list has. Every item in a list has the same type: `fruits` is a
`List[String]`, a list of strings, and `[1, 2, 3]` is a `List[Int]`.

## Reading items

Each item has a position, called its *index*, counting from 0:

```emerald
const fruits = ["apple", "banana", "cherry"]
print(fruits[0])
print(fruits[2])
print(fruits.first, fruits.last)
```

```text title="Output"
apple
cherry
apple cherry
```

The last item is at `count - 1`, one less than the count, because counting starts at 0. `first` and
`last` are the ends; for an empty list they are `nothing`, so they are [optional](../optionals/).

Asking for a position the list doesn't have is an error that says which positions it has:

```emerald
const fruits = ["apple"]
print(fruits[3])
```

```text title="Output"
lists.em:2:7: index 3 is outside this list, which has 1 element
  print(fruits[3])
        ^^^^^^^^^
Valid indices are 0 through 0.
```

## Changing a list

A list declared with `var` can change: add items, replace them, or take them out.

```emerald
var scores = [10, 20]
scores.append(30)       # add to the end
scores.insert(0, 5)     # add at position 0
print(scores)
scores[1] = 99          # replace an item
print(scores)
const removed = scores.remove_at(0)
print(removed, scores)
```

```text title="Output"
[5, 10, 20, 30]
[5, 99, 20, 30]
5 [99, 20, 30]
```

`remove_at` takes out the item at a position and gives it back; `remove("Bob")` takes out an item by
its value. A `const` list can't change at all, as
[Variables and Constants](../variables-and-constants/) showed.

## An empty list

A list with nothing in it yet needs its type written, since there are no items to tell Emerald what
it will hold:

```emerald
var todo: List[String] = []
print(todo.empty?())
todo.append("Buy milk")
print(todo)
```

```text title="Output"
true
["Buy milk"]
```

Without the type, `var todo = []` is an error, and the message shows how to write one.

## New list, or change this list?

Some methods give back a changed *copy* and leave the list alone; others change the list itself. The
ones that change it end in `!`:

```emerald
var nums = [3, 1, 2]
print(nums.sort())   # a sorted copy
print(nums)          # unchanged
nums.sort!()         # sort this list
print(nums)
```

```text title="Output"
[1, 2, 3]
[3, 1, 2]
[1, 2, 3]
```

The same goes for `reverse` and `reverse!`, `shuffle` and `shuffle!`, and others. The `!` is a warning
sign: this changes what you call it on, so it only works on a `var`.

## Lists are values

Giving a list to another name makes a copy. Changing one doesn't change the other:

```emerald
var a = [1, 2, 3]
var b = a
b.append(4)
print(a)
print(b)
```

```text title="Output"
[1, 2, 3]
[1, 2, 3, 4]
```

A list behaves like a number here: after `var y = x`, changing `y` never changes `x`. That's also why
a function that receives a list can't change the caller's list, as [Functions](../functions/)
explained. (Emerald doesn't really copy every item each time; it shares the list until one of them
changes, so this is cheap.)

## Working with every item

A `for` loop visits each item, and the [block methods](../lambdas-and-blocks/) work on a whole list at
once:

```emerald
const prices = [4, 9, 2]
for price in prices {
    print("$#{price}")
}
print(prices.map { p => p * 2 })
print(prices.filter { p => p > 3 })
print(prices.sum(), prices.min(), prices.max())
```

```text title="Output"
$4
$9
$2
[8, 18, 4]
[4, 9]
15 2 9
```

When the loop needs positions too, `each_with_index` gives both:

```emerald
const fruits = ["apple", "banana"]
fruits.each_with_index { fruit, i => print("#{i}: #{fruit}") }
```

```text title="Output"
0: apple
1: banana
```

A few other questions lists answer: `contains?(item)` asks whether an item is there, `find { ... }`
gives the first item that matches, and `find_index { ... }` gives its position. The
[List](../../builtins/types/list/) reference describes every method.

## Part of a list, and lists of lists

A range of positions gives part of a list as a new list:

```emerald
const letters = ["a", "b", "c", "d"]
print(letters[1..<3])
print(letters[2..])
```

```text title="Output"
["b", "c"]
["c", "d"]
```

And a list can hold other lists, which suits a grid:

```emerald
const grid = [[1, 2], [3, 4]]
print(grid[1][0])
```

```text title="Output"
3
```

`grid[1]` is the second row, `[3, 4]`, and `[0]` is its first item.

## What you've learned

- A list, `[a, b, c]`, keeps items of one type in order; `count` says how many.
- `list[i]` reads an item by position, counting from 0; `first` and `last` might be `nothing`.
- A `var` list can grow and change with `append`, `insert`, `remove_at`, and `list[i] = value`.
- An empty list needs its type: `var todo: List[String] = []`.
- Methods ending in `!` change the list; the others give back a new one.
- Giving a list to another name copies it.

Next, [dictionaries](../dictionaries/): looking values up by a key.
