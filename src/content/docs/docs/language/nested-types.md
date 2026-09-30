---
title: Nested Types
sidebar:
  order: 25
description: Declare a type inside another when it belongs to it, reach it by its full name, and give it a shorter one.
---

Sometimes a type only makes sense as part of another. A pizza's size means nothing on its own; it is a
pizza's size. A struct, class, or enum can declare types inside its braces, and they belong to it:

```emerald
struct Pizza {
    enum Size {
        small, medium, large
    }

    const size: Pizza.Size
    const toppings: List[String]

    func price(): Int {
        return case self.size {
            when Pizza.Size.small then 8
            when Pizza.Size.medium then 10
            when Pizza.Size.large then 12
        }
    }
}

const order = Pizza(Pizza.Size.large, ["cheese"])
print(order.price())
print(order)
```

```text title="Output"
12
Pizza(size: Pizza.Size.large, toppings: ["cheese"])
```

`Size` is declared inside `Pizza`, and its full name is `Pizza.Size`. Grouping it this way keeps
related names together, and leaves the plain name `Size` free for something else, such as a
`Shirt.Size`.

## Always the full name

A nested type is always written with the type around it, even inside that type's own code, as in
`price` above. So `Pizza.Size` means the same thing everywhere you read it. Writing just `Size`, inside
or outside `Pizza`, is an error.

You've already met one nested type: `Console.Color`, the enum of colors in the standard library, is an
enum nested inside `Console`.

## A shorter name

When a long name comes up often, `using` gives it a shorter one for the rest of the file:

```emerald
struct Pizza {
    enum Size {
        small, large
    }
}

using Size = Pizza.Size
print(Size.large)
```

```text title="Output"
Pizza.Size.large
```

The short name is only an alias: the value is still a `Pizza.Size`, and prints that way.

## What can nest

- A struct, class, or enum can declare nested structs, classes, enums, and traits, to any depth.
- A nested type is private to its outer type when its name starts with `_`, just like a field.
- A nested type doesn't belong to any particular value of the outer type; it is simply a type whose
  name lives inside another.

## What you've learned

- A type declared inside another's braces belongs to it, and is named `Outer.Inner`.
- The full name is used everywhere, including inside the outer type.
- `using Short = Outer.Inner` gives a shorter name for the rest of the file.

Next, [errors](../errors/): what happens when something goes wrong while a program runs, and how to
handle it.
