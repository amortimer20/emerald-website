---
title: Properties
sidebar:
  order: 21
description: Members that are read like fields but worked out each time, and writable ones that check or convert what they are given.
---

A *property* is read like a field, with no parentheses, but its value is worked out by code each time
it is read. It suits a value that follows from the fields, such as a full name from a first and last
name:

```emerald
struct Student {
    const first_name: String
    const last_name: String

    const full_name: String {
        return "#{self.first_name} #{self.last_name}"
    }
}

const student = Student("Ada", "Lovelace")
print(student.full_name)
```

```text title="Output"
Ada Lovelace
```

`const full_name: String { ... }` looks like a field with a block after it. The block runs whenever
`full_name` is read, and its `return` gives the value.

## Always up to date

Because a property is worked out on every read, it can never be out of date with the fields it comes
from:

```emerald
struct Rectangle {
    var width: Int
    var height: Int

    const area: Int {
        return self.width * self.height
    }
}

var room = Rectangle(3, 4)
print(room.area)
room.width = 10
print(room.area)
```

```text title="Output"
12
40
```

Storing the area in a field instead would mean remembering to update it every time the width or
height changed. A property can't be forgotten.

A `const` property is read-only. Assigning to it is an error that explains what to do instead:

```emerald
struct Rectangle {
    var width: Int
    var height: Int

    const area: Int {
        return self.width * self.height
    }
}

var room = Rectangle(3, 4)
room.area = 50
```

```text title="Output"
properties.em:11:6: `area` is a read-only property of Rectangle
  room.area = 50
       ^^^^
It is computed each time it is read. Change what it is computed from instead, or give it a `set` block as a `var` property.
```

## Properties you can assign to

A `var` property has two blocks: `get`, which works out its value when it is read, and `set`, which
runs when it is assigned, receiving the new value as `value`:

```emerald
struct Circle {
    var radius: Float

    var diameter: Float {
        get {
            return self.radius * 2
        }
        set {
            self.radius = value / 2
        }
    }
}

var wheel = Circle(1)
print(wheel.diameter)
wheel.diameter = 10
print(wheel.radius)
```

```text title="Output"
2.0
5.0
```

To the rest of the program, `diameter` looks like an ordinary field. Only the radius is stored, and
the property converts both ways.

A setter can also check what it is given. Paired with a [private](../classes/#keeping-fields-private)
field, it keeps a value within limits no matter what the rest of the program assigns:

```emerald
class Thermostat {
    var _target: Int = 20

    var target: Int {
        get {
            return self._target
        }
        set {
            self._target = value.clamp(10, 30)
        }
    }
}

const home = Thermostat()
home.target = 45
print(home.target)
home.target = 22
print(home.target)
```

```text title="Output"
30
22
```

## Property or method?

- A **property** answers a question about the value, cheaply and without changing anything: an area,
  a full name, whether a list is empty. It is read without parentheses.
- A **method** does something, takes parameters, or might take a while. It is called with parentheses.

Reading a property should never change the value it belongs to, and Emerald enforces that: a
property block that changes `self` is an error suggesting a method instead. And since a property is
read without parentheses, `room.area()` is an error that says so.

A struct prints its stored fields only, so `print(room)` shows `Rectangle(width: 10, height: 4)`,
without `area`.

## What you've learned

- `const name: Type { return ... }` declares a read-only property, worked out on every read.
- A property is always up to date with the fields it is computed from.
- `var name: Type { get { ... } set { ... } }` declares one that can be assigned; the setter gets
  `value`.
- A setter can convert or check what it is given.
- Properties answer questions without changing anything; methods do things.

Next, [inheritance](../inheritance/): classes built on other classes.
