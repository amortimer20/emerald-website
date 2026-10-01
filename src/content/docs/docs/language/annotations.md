---
title: Annotations
sidebar:
  order: 30
description: The four @ words that tell Emerald something about the declaration below them, and what each is for.
---

An *annotation* is a word starting with `@`, written on the line before a declaration. It doesn't run
anything; it tells Emerald something about that declaration, which Emerald then checks or acts on.
You've met all four already, on other pages. This page gathers them in one place.

```emerald
class Animal {
    func speak(): String {
        return "..."
    }
}

class Dog extends Animal {
    @override
    func speak(): String {
        return "Woof"
    }
}

print(Dog().speak())
```

```text title="Output"
Woof
```

## The four annotations

| Annotation | Goes on | Means |
| --- | --- | --- |
| `@override` | a method | This deliberately replaces a base class's method, or fulfils a trait's requirement. See [Inheritance](../inheritance/) and [Traits](../traits/). |
| `@abstract` | a class, or a method of one | The class is only a base and can't be made on its own; the method has no body, and every subclass must supply one. See [Inheritance](../inheritance/). |
| `@test` | a top-level function | This function is a test, run by `emerald test`. See [Tests](../tests/). |
| `@operator("+")` | a method | `+` on this type calls this method; `-`, `*`, and `/` work the same way. See [Operator Overloading](../operator-overloading/). |

That is the whole list. You can't declare annotations of your own, which keeps every `@` word one
you can look up here.

## Why they exist

Each annotation turns an intention into something Emerald can check. `@override` is the clearest
example. Replacing a base class's method without it is an error, so a method is never replaced by
accident, just by picking a name that happened to be taken:

```emerald
class Animal {
    func speak(): String {
        return "..."
    }
}

class Dog extends Animal {
    func speak(): String {
        return "Woof"
    }
}
```

```text title="Output"
annotations.em:8:10: `speak` is already a method of `Animal`
      func speak(): String {
           ^^^^^
Write `@override` on the line before it to replace `Animal`'s version, or give it a name of its own.
```

It works the other way around too: `@override` on something that replaces nothing is an error, so a
misspelled method name can't quietly become a new method.

## Mistakes Emerald catches

A misspelled annotation is caught, with a suggestion:

```emerald
class Animal {
    func speak(): String {
        return "..."
    }
}

class Dog extends Animal {
    @overide
    func speak(): String {
        return "Woof"
    }
}
```

```text title="Output"
annotations.em:8:5: `@overide` is not an annotation
      @overide
      ^^^^^^^^
Did you mean `@override`?
```

An annotation from another language is caught as well, and Emerald lists the ones it has:

```emerald
@deprecated
func old_greeting() {
    print("Hi")
}
```

```text title="Output"
annotations.em:1:1: `@deprecated` is not an annotation
  @deprecated
  ^^^^^^^^^^^
Emerald's annotations are `@override`, `@abstract`, `@test`, and `@operator("*")`.
```

An annotation in the wrong place, such as `@test` on a constant, says where it belongs:

```emerald
@test
const answer = 42
```

```text title="Output"
annotations.em:1:1: `@test` belongs on a function
  @test
  ^^^^^
Move `@test` to a top-level function with no parameters and no result.
```

## What you've learned

- An annotation is an `@` word on the line before a declaration, telling Emerald something about it.
- There are four: `@override`, `@abstract`, `@test`, and `@operator`.
- Each one states an intention that Emerald checks, such as that a method really replaces another.
- You can't define your own, and misspelled or misplaced ones are caught.

That is the end of the language reference. From here, the [Built-ins](../../builtins/) pages
describe every type and library Emerald comes with, one at a time.
