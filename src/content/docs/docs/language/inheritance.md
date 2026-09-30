---
title: Inheritance
sidebar:
  order: 22
description: Build a class on top of another, replace its methods with your own, and treat related objects alike.
---

A class can be built on top of another class, taking everything it has and adding more. The class it
builds on is its *base class*, and the new one is a *subclass*. A dog is an animal with a few extras:

```emerald
class Animal {
    const name: String

    func describe(): String {
        return "#{self.name} is an animal"
    }
}

class Dog extends Animal {
    constructor(name: String) {
        super(name)
    }

    func fetch() {
        print("#{self.name} fetches the ball")
    }
}

const rex = Dog("Rex")
print(rex.describe())
rex.fetch()
```

```text title="Output"
Rex is an animal
Rex fetches the ball
```

`class Dog extends Animal` makes `Dog` a subclass of `Animal`. A dog has everything an animal has,
the `name` field and the `describe` method, plus its own `fetch`. Only classes can extend others;
structs can't.

## Building a subclass

A subclass needs its own constructor when its base class takes arguments to build. The constructor's
first line, `super(...)`, builds the animal part, passing what `Animal` needs. Leave the constructor
out, and Emerald says what to add:

```emerald
class Animal {
    const name: String
}

class Dog extends Animal {
}
```

```text title="Output"
inheritance.em:5:7: `Dog` needs a constructor, because building `Animal` takes arguments
  class Dog extends Animal {
        ^^^
Add a constructor to `Dog` that starts with `super(...)`, passing what `Animal` needs.
```

A subclass can add fields of its own too, and set them in its constructor after `super(...)`.

## Replacing a method

A subclass can replace a method of its base class with its own version. `@override` on the line
before says that this is deliberate:

```emerald
class Animal {
    const name: String

    func speak(): String {
        return "..."
    }
}

class Dog extends Animal {
    constructor(name: String) {
        super(name)
    }

    @override
    func speak(): String {
        return "Woof"
    }
}

class Cat extends Animal {
    constructor(name: String) {
        super(name)
    }

    @override
    func speak(): String {
        return "Meow"
    }
}

const pets = [Dog("Rex"), Cat("Tom"), Animal("Generic")]
for pet in pets {
    print("#{pet.name}: #{pet.speak()}")
}
```

```text title="Output"
Rex: Woof
Tom: Meow
Generic: ...
```

This is the heart of inheritance. The loop treats every pet the same way, calling `pet.speak()`, and
each object answers with its own class's version. The list holds dogs, cats, and a plain animal, so
Emerald makes it a list of their shared base class, `List[Animal]`.

Without `@override`, a method with the same name as one in the base class is an error, so a method is
never replaced by accident. A replacing method takes the same parameters and gives back the same type
as the one it replaces.

## Using the base class's version

Inside a replacing method, `super.method()` runs the base class's version, which lets a subclass add to
it rather than start from scratch:

```emerald
class Animal {
    func describe(): String {
        return "an animal"
    }
}

class Dog extends Animal {
    @override
    func describe(): String {
        return super.describe() + ", and a good dog"
    }
}

print(Dog().describe())
```

```text title="Output"
an animal, and a good dog
```

## Asking what kind of object it is

A name of the base type can hold a subclass object, but through it you can only use what every
`Animal` has. `is` asks whether an object is of a particular class, and inside the `if`, Emerald treats
it as one:

```emerald
class Animal {
    const name: String
}

class Dog extends Animal {
    constructor(name: String) {
        super(name)
    }

    func fetch() {
        print("#{self.name} fetches")
    }
}

const pets: List[Animal] = [Dog("Rex"), Animal("Nemo")]
for pet in pets {
    if pet is Dog {
        pet.fetch()
    }
    else {
        print("#{pet.name} does not fetch")
    }
}
```

```text title="Output"
Rex fetches
Nemo does not fetch
```

Calling `pet.fetch()` without the `is` check is an error, and its message suggests exactly this.

## Classes meant only as a base

Sometimes a base class exists only to be extended: every shape has an area, but there is no such thing
as a plain shape. `@abstract` marks such a class, and a method it declares without a body, which every
subclass must then supply:

```emerald
@abstract
class Shape {
    @abstract
    func area(): Float
}

class Square extends Shape {
    const side: Float

    constructor(side: Float) {
        self.side = side
    }

    @override
    func area(): Float {
        return self.side * self.side
    }
}

print(Square(3).area())
```

```text title="Output"
9.0
```

An abstract class can't be made on its own: `Shape()` is an error that suggests making one of its
subclasses instead.

## When to use inheritance

Inheritance fits when one kind of thing really *is* a more specific version of another, and you want
to treat them alike: every shape has an area, every animal can speak. A class extends at most one base
class. When types share an ability rather than an ancestry, such as things that can be compared or
printed in a certain way, a [trait](../traits/) is usually the better tool.

## What you've learned

- `class Sub extends Base` builds a class on another, taking its fields and methods.
- A subclass whose base takes arguments needs a constructor starting with `super(...)`.
- `@override` replaces a base method, deliberately; each object runs its own class's version.
- `super.method()` runs the base class's version.
- `is` tests an object's class, and inside the test Emerald treats it as that class.
- `@abstract` marks a class that is only a base, and methods its subclasses must supply.

Next, [traits](../traits/): abilities that unrelated types can share.
