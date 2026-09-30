---
title: Structs
sidebar:
  order: 19
description: Make a type of your own that groups named values, build values of it, and give it methods.
---

A *struct* is a type you make yourself, grouping a few named values into one. A point has an x and a
y; a player has a name and a score. Declaring a struct describes its *fields*, and then you can make
as many values of it as you like:

```emerald
struct Point {
    var x: Int
    var y: Int
}

const p = Point(3, 4)
print(p)
print(p.x, p.y)
```

```text title="Output"
Point(x: 3, y: 4)
3 4
```

`struct Point` declares the type; its name is written in `PascalCase`, like the built-in types.
Each field is declared with `var` or `const` and a type. `Point(3, 4)` makes a value, giving the
fields their values in order, and `p.x` reads one back. Printing a struct shows every field.

## Making values

A struct comes with a function that makes its values, called its *constructor*. It takes one value
per field, in the order they are declared. Fields can have defaults, which a call can leave out, and
arguments can be named, as with any function:

```emerald
struct Player {
    const name: String
    var score: Int = 0
    var level: Int = 1
}

print(Player("Ada"))
print(Player("Grace", level: 5))
print(Player(name: "Hopper", score: 10))
```

```text title="Output"
Player(name: "Ada", score: 0, level: 1)
Player(name: "Grace", score: 0, level: 5)
Player(name: "Hopper", score: 10, level: 1)
```

A field that might have no value is an [optional](../optionals/), often with `nothing` as its
default: `const nickname: String? = nothing`.

## Changing fields

A struct value kept in a `var` can have its `var` fields changed:

```emerald
struct Point {
    var x: Int
    var y: Int
}

var p = Point(3, 4)
p.x = 10
print(p)
```

```text title="Output"
Point(x: 10, y: 4)
```

Both have to allow it: the value must be in a `var`, and the field must be `var`. A `const` field
never changes once the value is made, which suits things like a player's name:

```emerald
struct Player {
    const name: String
    var score: Int
}

var p = Player("Ada", 0)
p.name = "Bob"
```

```text title="Output"
structs.em:7:3: `name` is a `const` field of Player, so it cannot change
  p.name = "Bob"
    ^^^^
Declare it `var name: String` in Player if it needs to change.
```

## Structs are values

Like numbers and lists, a struct is a value: giving it to another name makes a copy, and changing one
leaves the other alone:

```emerald
struct Point {
    var x: Int
    var y: Int
}

var a = Point(1, 1)
var b = a
b.x = 99
print(a)
print(b)
```

```text title="Output"
Point(x: 1, y: 1)
Point(x: 99, y: 1)
```

For the same reason, two structs are equal when all their fields are equal:
`Point(1, 2) == Point(1, 2)` is `true`. When several parts of a program need to share and change one
thing, use a [class](../classes/) instead.

## Methods

A struct can have functions of its own, called *methods*, declared inside its braces. A method reaches
the value it was called on as `self`:

```emerald
struct Rectangle {
    const width: Int
    const height: Int

    func area(): Int {
        return self.width * self.height
    }

    func describe(): String {
        return "#{self.width} by #{self.height}"
    }
}

const room = Rectangle(3, 4)
print(room.area())
print(room.describe())
```

```text title="Output"
12
3 by 4
```

A field is always reached through `self.` inside a method; plain `width` is an error that suggests
`self.width`. That makes it obvious, reading a method, which names are fields and which are
parameters or local variables.

## Methods that change the value

A method can change the struct's fields. It can only be called on a value in a `var`, because it
changes that value:

```emerald
struct Counter {
    var count: Int = 0

    func increment() {
        self.count += 1
    }
}

var clicks = Counter()
clicks.increment()
clicks.increment()
print(clicks.count)
```

```text title="Output"
2
```

Emerald works out which methods change the value, so there is nothing to mark. Calling `increment` on a
`const` counter is an error saying the counter would have to be a `var`.

## A constructor of your own

When a value should be made from something other than its fields, a struct can declare its own
`constructor`, which replaces the generated one:

```emerald
struct Temperature {
    const celsius: Float

    constructor(fahrenheit: Float) {
        self.celsius = (fahrenheit - 32) * 5 / 9
    }
}

print(Temperature(212).celsius)
```

```text title="Output"
100.0
```

A constructor must give every field without a default its value.

## Structs in collections

Structs work anywhere other values do, which is where they pay off. A list of structs keeps related
values together, and block methods can use their fields:

```emerald
struct Score {
    const name: String
    const points: Int
}

const scores = [Score("Ada", 90), Score("Grace", 95)]
const best = scores.max_by { s => s.points }
print(best)
```

```text title="Output"
Score(name: "Grace", points: 95)
```

## What you've learned

- `struct Name { ... }` declares a type with named fields, each `var` or `const`.
- `Name(...)` makes a value, with values in field order; defaults and named arguments work as for
  functions.
- `value.field` reads a field; a `var` field of a value in a `var` can change.
- Structs are values: assigning copies them, and `==` compares every field.
- Methods, declared inside the braces, reach the value as `self`; one that changes it needs a `var`.
- A `constructor` can replace the generated one.

Next, [classes](../classes/): types whose values are shared rather than copied.
