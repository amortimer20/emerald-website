---
title: Generics
sidebar:
  order: 27
description: Write a type or a function once, and let each use say what kind of value it holds.
---

You have used generics since your first list. A `List[Int]` and a `List[String]` are the same kind of
collection holding different kinds of item, and the type in the brackets says which. Your own types and
functions can work the same way.

Suppose a game needs a board of letters, and a scoreboard of numbers, both laid out in a grid. Without
generics you would write the grid twice, once for `String` and once for `Int`, identical except for the
type. With generics you write it once:

```emerald
class Grid[Item] {
    const width: Int
    var _cells: List[Item] = []

    constructor(width: Int, height: Int, fill: Item) {
        self.width = width
        for _ in 0..<width * height {
            self._cells.append(fill)
        }
    }

    func get(x: Int, y: Int): Item {
        return self._cells[y * self.width + x]
    }

    func set(x: Int, y: Int, cell: Item) {
        self._cells[y * self.width + x] = cell
    }
}

const board = Grid(3, 3, ".")
board.set(1, 1, "X")
print(board.get(1, 1), board.get(0, 0))

const scores = Grid(2, 2, 0)
scores.set(0, 1, 7)
print(scores.get(0, 1) + 1)
```

```text title="Output"
X .
8
```

`[Item]` after the name is a *type parameter*: a name for whatever type each grid is given. Inside the
braces, `Item` is used like any other type. The board's `Item` is `String`, because it was filled with
`"."`, and the scoreboard's is `Int`. Any name will do; a word that says what the type is for, such as
`Item` or `Key`, reads better than a single letter.

## Where the type comes from

You never write the type where you build a value. Emerald works it out from the arguments, as it did
above, or from where the value goes:

```emerald
class Box[Item] {
    var value: Item

    constructor(value: Item) {
        self.value = value
    }
}

const heights: Box[Float] = Box(2)
print(heights.value)
```

```text title="Output"
2.0
```

`Box[Float]` is how the type is written, wherever a type goes. Because the box holds a `Float`, the `2`
becomes `2.0`, just as it would in a `List[Float]`. When nothing says what the type is, Emerald asks you
to write it:

```emerald
class Stack[Item] {
    var _items: List[Item] = []
}

const stack = Stack()
```

```text title="Output"
generics.em:5:15: Emerald cannot tell what `Item` is for this `Stack`
  const stack = Stack()
                ^^^^^
Nothing passed here says what `Item` is. Write the type where the value is kept, as in `const value: Stack[String] = Stack(...)`.
```

A `Box[Int]` is not a `Box[Float]`, and one cannot be used where the other is wanted.

## What a type parameter can do

`Item` could be any type at all, so inside `Grid` you can store it, pass it, return it, keep it in a
list, and print it, and nothing more:

```emerald
class Pair[Item] {
    const first: Item
    const second: Item

    func same?(): Bool {
        return self.first == self.second
    }
}
```

```text title="Output"
generics.em:6:16: `Item` values cannot be compared with `==`
          return self.first == self.second
                 ^^^^^^^^^^^^^^^^^^^^^^^^^
`Item` could be any type, and not every type can be compared with `==`. Write `Item with Equatable` where `Item` is declared to require that it can.
```

That is what lets `Pair` promise to work for every type. To ask for more, see [`with`](#asking-for-more-with)
below.

## Functions

A function can have type parameters too, written after its name. Each call works them out from what it
is given:

```emerald
func first_or[Item](items: List[Item], fallback: Item): Item {
    return if items.empty?() then fallback else items[0]
}

print(first_or([3, 4], 0))
print(first_or([], "none"))
```

```text title="Output"
3
none
```

In the second call, `[]` says nothing about its items, so `"none"` decides that `Item` is `String`.

A method can have type parameters of its own. Here `change` turns each item into something else, and
the block's result decides what:

```emerald
class Box[Item] {
    const value: Item

    func mapped[Result](change: func(Item): Result): Box[Result] {
        return Box(change(self.value))
    }
}

const name = Box("Ada")
print(name.mapped { text => text.count }.value)
```

```text title="Output"
3
```

## Asking for more: `with`

To compare, sort, or look up values of a type parameter, ask for a [trait](../traits/) that promises
it, with `with`:

```emerald
func largest[Item with Ordered](items: List[Item]): Item? {
    if items.empty?() {
        return nothing
    }
    var best = items[0]
    for item in items {
        best = item if item > best
    }
    return best
}

print(largest([3, 9, 4]))
print(largest(["pear", "fig"]))
```

```text title="Output"
9
pear
```

`Item with Ordered` lets `largest` use `>`, and it means every type given for `Item` must have an
order. `Int`, `Float`, and `String` do; so does any type of yours that takes on
[`Ordered`](../../builtins/traits/ordered/). A type that doesn't is caught at the call:

```emerald
func largest[Item with Ordered](items: List[Item]): Item? {
    return items.max()
}

struct Player {
    const name: String
}

print(largest([Player("Ada")]))
```

```text title="Output"
generics.em:9:7: `largest` needs `Item` values that can be put in order, and Player cannot
  print(largest([Player("Ada")]))
        ^^^^^^^
Add `with Ordered` to `Player` and give it what `Ordered` requires.
```

The others work the same way: `with Equatable` allows `==` and `contains?`, `with Hashable` lets the
values be dictionary keys and set members, and `with Textual` gives them `to_string()`. Your own traits
work too, and the body can call what they declare. A type parameter asks for one trait; to need two,
write a trait that builds on both, such as `trait Sortable with Ordered, Textual { }`, and ask for that.

## Enums

An enum can have type parameters too, so its values can hold them:

```emerald
enum Maybe[Item] {
    none
    some(value: Item)
}

func describe(found: Maybe[Int]): String {
    return case found {
        when Maybe.none then "nothing found"
        when Maybe.some(value) then "found #{value}"
    }
}

print(describe(Maybe.some(42)))
print(describe(Maybe.none))
```

```text title="Output"
found 42
nothing found
```

`Maybe.none` holds nothing at all, so it fits a `Maybe` of any type. (Emerald's own optionals,
`Int?`, already do this job; the example only shows the shape.)

## What Emerald leaves out

Some languages let a `Box[Int]` stand in for a `Box[Float]`, write types where a value is built, or ask
a value what its type parameter was while the program runs. Emerald does none of these. Each would make
generics bigger and harder to read than the problems they solve.

## What you've learned

- `class Grid[Item]` gives a type a type parameter; `Grid[String]` is a grid of strings.
- Emerald works out the types from the arguments or from where the value goes; you never write them
  where you build a value.
- A plain type parameter can be stored, passed, returned, and printed, and nothing more.
- Functions and methods can have type parameters too, worked out at each call.
- `with` asks for a trait, such as `Item with Ordered`, which lets the body use what the trait
  promises and checks every type given for it.
- Enums can have type parameters, and a value that holds nothing fits any of them.

Next, [errors](../errors/): what happens when something goes wrong while a program runs.
