---
title: Operator Overloading
sidebar:
  order: 26
description: Let your own types use +, -, *, and /, and compare them with < and ==, by connecting operators to ordinary methods.
---

Numbers can be added with `+`. Your own types can be too, when adding them means something, such as two
vectors or two amounts of money. `@operator("+")` connects `+` to a method:

```emerald
struct Vector2 {
    const x: Float
    const y: Float

    @operator("+")
    func add(other: Vector2): Vector2 {
        return Vector2(self.x + other.x, self.y + other.y)
    }
}

const a = Vector2(1, 2)
const b = Vector2(3, 4)
print(a + b)
print(a.add(b))
```

```text title="Output"
Vector2(x: 4.0, y: 6.0)
Vector2(x: 4.0, y: 6.0)
```

`a + b` simply calls `a.add(b)`: the operator is another way to write the method call. So an operator
never hides what it does. You can always find the method it runs, and call it by name too.

Without the annotation, `+` on two vectors is an error that suggests adding one.

## Which operators

`@operator` works for the four arithmetic operators: `+`, `-`, `*`, and `/`. When a method takes and
gives back the type's own values, as `add` does, its name is fixed: `add` for `+`, `subtract` for `-`,
`multiply` for `*`, and `divide` for `/`. That keeps every `+` discoverable by the same name. Emerald
says so if another name is used.

## Mixing types

The other side of the operator can be a different type. Multiplying money by a whole number gives more
money:

```emerald
struct Money {
    const cents: Int

    @operator("*")
    func times(quantity: Int): Money {
        return Money(self.cents * quantity)
    }
}

print(Money(125) * 3)
```

```text title="Output"
Money(cents: 375)
```

Here the method can have any clear name, since it isn't `Money` times `Money`. The value on the left
decides which method runs, so `Money(125) * 3` works, but `3 * Money(125)` would need `Int` to know about
money, and it doesn't.

## Compound assignment comes free

Once `+` is connected, `+=` works too:

```emerald
struct Vector2 {
    const x: Float
    const y: Float

    @operator("+")
    func add(other: Vector2): Vector2 {
        return Vector2(self.x + other.x, self.y + other.y)
    }
}

var position = Vector2(0, 0)
position += Vector2(1, 1)
position += Vector2(1, 1)
print(position)
```

```text title="Output"
Vector2(x: 2.0, y: 2.0)
```

## Comparing: `<` and `==`

Comparison works through the built-in traits rather than `@operator`. Adopting `Ordered` and writing one
`compare` method gives your type `<`, `<=`, `>`, and `>=`, and lets lists of it be sorted. `compare`
returns a negative number when `self` comes first, zero when the two are equal, and a positive number
when `self` comes after:

```emerald
struct Version with Ordered {
    const major: Int
    const minor: Int

    @override
    func compare(other: Version): Int {
        return self.major - other.major if self.major != other.major
        return self.minor - other.minor
    }
}

print(Version(1, 2) < Version(1, 10))
print([Version(2, 0), Version(1, 5)].sort())
```

```text title="Output"
true
[Version(major: 1, minor: 5), Version(major: 2, minor: 0)]
```

A struct already compares with `==` field by field. To choose your own meaning, adopt `Equatable` and
write `equals`; add `Hashable` too if values of the type will be dictionary keys or set members. The
[Ordered](../../builtins/traits/ordered/) and [Equatable](../../builtins/traits/equatable/) pages describe
them.

## When to overload

Give a type an operator only when its meaning is obvious to anyone reading the code: adding vectors,
multiplying money. If you have to explain what `+` means for your type, a named method, such as
`merge` or `combine`, is clearer.

## What you've learned

- `@operator("+")` on a method lets `a + b` call it; `+`, `-`, `*`, and `/` can be connected.
- A same-type operation must be named `add`, `subtract`, `multiply`, or `divide`.
- The other side can be a different type, such as `Money * Int`; the left side decides.
- `+=` and friends work once the operator does.
- `Ordered` gives `<` and sorting through `compare`; `Equatable` gives your own `==`.

Next, [errors](../errors/): what happens when something goes wrong while a program runs.
