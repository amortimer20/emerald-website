---
title: Traits
sidebar:
  order: 23
description: Describe an ability several types can share, have types promise to provide it, and write code that works with any of them.
---

A *trait* describes an ability: a set of methods (and sometimes fields) that a type promises to have.
Any struct or class can take on a trait, whatever it is related to, and code can then work with every
type that has that ability.

```emerald
trait Shape {
    func area(): Float

    func describe(): String {
        return "a shape with area #{self.area()}"
    }
}

struct Square with Shape {
    const side: Float

    @override
    func area(): Float {
        return self.side * self.side
    }
}

struct Circle with Shape {
    const radius: Float

    @override
    func area(): Float {
        return 3.14 * self.radius * self.radius
    }
}

const shapes: List[Shape] = [Square(2), Circle(1)]
for shape in shapes {
    print(shape.describe())
}
```

```text title="Output"
a shape with area 4.0
a shape with area 3.14
```

`trait Shape` says what every shape has: an `area` method, and a `describe` method. `area` has no body,
so it is a *requirement*: every type that takes on `Shape` must supply its own. `describe` has a body,
so it is a *default* that every shape gets for free.

`struct Square with Shape` says that squares are shapes, and `@override` marks the method that fulfils
the requirement. Then a `List[Shape]` can hold squares and circles together, and the loop treats them
all alike.

## A promise the checker holds you to

A type that takes on a trait must supply every requirement, and Emerald checks before the program
runs:

```emerald
trait Shape {
    func area(): Float
}

struct Square with Shape {
    const side: Float
}
```

```text title="Output"
traits.em:5:8: `Square` does not supply `area`, which the trait `Shape` requires
  struct Square with Shape {
         ^^^^^^
Add `@override func area(...)` with a body to `Square`.
```

Taking on a trait is always written out with `with`. A type that happens to have an `area` method, but
doesn't say `with Shape`, isn't a `Shape`. That keeps a promise from being made by accident.

## Traits as types

A trait can be used as a type, for a list as above, or for a parameter. A function that takes a trait
works with any type that has it:

```emerald
trait Named {
    const name: String
}

struct Pet with Named {
    const name: String
}

func greet(thing: Named) {
    print("Hello, #{thing.name}!")
}

greet(Pet("Rex"))
```

```text title="Output"
Hello, Rex!
```

Through a trait type, only what the trait describes can be used: inside `greet`, `thing.name` works, but
nothing else a `Pet` might have does. `is` asks whether a value has a trait, as it does for classes.

## Requiring fields

A trait can require a field as well as methods. `const name: String` in a trait means "has a `name` you
can read". A type fulfils it with an ordinary field, and a default method can use it:

```emerald
trait Named {
    const name: String

    func introduction(): String {
        return "I am #{self.name}."
    }
}

struct Robot with Named {
    const name: String
}

class Person with Named {
    const name: String
}

print(Robot("R2").introduction())
print(Person("Ada").introduction())
```

```text title="Output"
I am R2.
I am Ada.
```

A robot and a person have nothing else in common, yet both are `Named`. A trait stores nothing itself;
each type keeps its own fields.

## Several traits, one base class

A type can take on several traits, separated by commas, and a class can extend a base class too:
`class Duck extends Animal with Swimmer, Flyer`. A method a type writes itself always wins over a
trait's default. If two traits offer different defaults for the same method, Emerald asks you to write
that method yourself rather than guess which one you meant.

## Built-in traits

Emerald comes with a few traits of its own. Taking one on changes how Emerald treats your type. The
most common is `Textual`, which controls how a value prints:

```emerald
struct Money with Textual {
    const cents: Int

    @override
    func to_string(): String {
        return "$#{self.cents // 100}.#{(self.cents % 100).to_string().pad_start(2, "0")}"
    }
}

print(Money(399))
```

```text title="Output"
$3.99
```

Without `Textual`, it would print as `Money(cents: 399)`. The others are `Equatable` and `Hashable`, for
your own idea of equality, and `Ordered`, for sorting and `<`. The
[Built-ins traits](../../builtins/traits/equatable/) pages describe each.

## Trait or base class?

- Use a **base class** when types share an ancestry and fields: every dog and cat is an animal with a
  name. A class has at most one.
- Use a **trait** when unrelated types share an ability: robots and people can both be named, and
  squares, circles, and whole buildings can all have an area. A type can take on many.

## What you've learned

- `trait Name { ... }` describes methods and fields a type promises to have; a method without a body is
  a requirement, and one with a body is a default.
- `struct Type with Trait` takes it on; `@override` marks the methods that fulfil it.
- Emerald checks every requirement is supplied, and a trait is only taken on when written with `with`.
- A trait can be a type, for lists and parameters, exposing only what it describes.
- Built-in traits such as `Textual` change how Emerald treats your type.

Next, [enums](../enums/): types with a fixed set of named values.
