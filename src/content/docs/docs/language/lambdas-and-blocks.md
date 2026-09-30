---
title: Lambdas and Blocks
sidebar:
  order: 12
description: Functions without names, written where they are needed and handed to other functions, and how they remember the variables around them.
---

A *lambda* is a function without a name, written right where it is needed. It is written between
braces: what it receives, an arrow `=>`, and what it gives back.

```emerald
const numbers = [1, 2, 3, 4]
print(numbers.map { n => n * 10 })
```

```text title="Output"
[10, 20, 30, 40]
```

`{ n => n * 10 }` is a lambda: given a number `n`, it gives back `n * 10`. `map` calls it once for
every item of the list and collects the answers into a new list. When a lambda is the last thing a
call takes, it can follow the call's parentheses, or replace them when there are none, as here. A
lambda written this way is often called a *block*.

## Handing work to a method

Many methods take a block that says what to do with each item. Three you'll use constantly:

```emerald
const numbers = [1, 2, 3, 4]
print(numbers.map { n => n * 10 })          # change each item
print(numbers.filter { n => n % 2 == 0 })   # keep some items
numbers.each { n => print(n) }              # do something with each
```

```text title="Output"
[10, 20, 30, 40]
[2, 4]
1
2
3
4
```

`map` and `filter` give back a new list and leave the original alone. `each` just runs the block for
every item. Numbers have block methods too:

```emerald
3.times { i => print("Round #{i + 1}") }
```

```text title="Output"
Round 1
Round 2
Round 3
```

[Lists](../lists/) and the [List](../../builtins/types/list/) reference list many more.

## Blocks with several lines

A block can hold several lines. When it gives back a value, it uses `return`, as a function does:

```emerald
const numbers = [3, 8, 1]
const labels = numbers.map { n =>
    if n > 5 {
        return "big"
    }
    return "small"
}
print(labels)
```

```text title="Output"
["small", "big", "small"]
```

`return` inside a block leaves only the block, giving back its answer for this item; it doesn't
leave the function around it. Likewise, `break` and `continue` can't reach out of a block to stop a
loop around it.

A block that takes nothing still has its arrow: `{ => print("hi") }`. One that takes two values
names both: `{ a, b => a + b }`. And `_` names a value the block doesn't need: `{ _ => ... }`.

## Lambdas are values

A lambda can be stored in a name and called like a function. On its own, with no method to say
what it receives, it has to give its parameter a type:

```emerald
const double = { value: Int => value * 2 }
print(double(21))
```

```text title="Output"
42
```

```emerald
const double = { value => value * 2 }
```

```text title="Output"
lambdas.em:1:18: `value` needs a type
  const double = { value => value * 2 }
                   ^^^^^
A lambda written on its own says what it receives, as in `{ value: Int => value * 2 }`.
```

In `numbers.map { n => ... }`, `n` needs no type because the list says what it holds.

## Writing functions that take a block

A function type is written like a declaration without names: `func()` takes nothing and gives
nothing back, `func(Int): Int` takes an `Int` and gives one back. A parameter with a function type
receives a lambda:

```emerald
func twice(action: func()) {
    action()
    action()
}

twice { => print("Hip hip!") }
```

```text title="Output"
Hip hip!
Hip hip!
```

When the function takes other arguments too, the block still goes last, after the parentheses:

```emerald
func apply(n: Int, change: func(Int): Int): Int {
    return change(n)
}

print(apply(5) { x => x * x })
```

```text title="Output"
25
```

## Blocks remember what's around them

A block can use the variables around it, and even change them:

```emerald
var total = 0
[1, 2, 3].each { n => total += n }
print(total)
```

```text title="Output"
6
```

The block doesn't get a copy of `total`; it uses the variable itself. A lambda keeps the variables it
uses even after the function that made it has finished, which lets it remember things between
calls:

```emerald
func make_counter(): func(): Int {
    var count = 0
    return { =>
        count += 1
        return count
    }
}

const next = make_counter()
print(next(), next(), next())
```

```text title="Output"
1 2 3
```

Each call to `next` adds one to the same `count`, which lives on inside the lambda. A lambda that
keeps variables like this is called a *closure*.

## A block in a condition

When a call with a block appears in an `if`, `while`, or `for` line, put parentheses around the
call, so its braces aren't mistaken for the start of the `if`'s own block:

```emerald
const items = [1, 5]
if (items.any? { n => n > 3 }) {
    print("found one")
}
```

```text title="Output"
found one
```

## What you've learned

- A lambda, `{ value => answer }`, is a function without a name; `{ => ... }` takes nothing.
- A block after a call is passed to it: `map`, `filter`, `each`, and `times` all take one.
- A block with several lines uses `return`, which leaves only the block.
- A lambda can be stored and called; on its own, its parameters need types.
- A function type such as `func(Int): Int` lets your own functions take blocks, which go last.
- A block uses the variables around it, not copies, and keeps them after its function ends.

Next, [optionals](../optionals/): values that might be missing.
