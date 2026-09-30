---
title: Functions
sidebar:
  order: 11
description: Name a piece of code so you can run it again, give it values to work with, and get an answer back.
---

A function is a piece of code with a name. Once declared, it can be run, or *called*, by writing its
name, as many times as you like. Functions let you write something once and use it everywhere, and
give a name to what a few lines of code do.

```emerald
func greet() {
    print("Hello!")
}

greet()
greet()
```

```text title="Output"
Hello!
Hello!
```

`func` declares a function, followed by its name, parentheses, and its code in braces. Declaring it
doesn't run it; `greet()` does. You have been calling functions since the first page: `print` and
`input` are functions that come with Emerald.

## Giving a function values

A function can take *parameters*: names for the values it needs, each with its type:

```emerald
func greet(name: String) {
    print("Hello, #{name}!")
}

greet("Ada")
greet("Grace")
```

```text title="Output"
Hello, Ada!
Hello, Grace!
```

The values in the call, `"Ada"` and then `"Grace"`, are the *arguments*. Each call gives `name` the
argument it was passed. A function can take several parameters, separated by commas.

Emerald checks every call against the function's parameters before the program runs, so a call
with the wrong kind of value, or the wrong number of them, is caught:

```emerald
func greet(name: String) {
    print("Hello, #{name}!")
}

greet(42)
```

```text title="Output"
functions.em:5:7: this is Int, but parameter `name` of `greet` needs String
  greet(42)
        ^^
Pass a value of the expected type, or convert it first.
```

## Getting an answer back

A function can work something out and *return* it. The type of the answer goes after the
parentheses, following a colon, and `return` gives the answer back:

```emerald
func area(width: Int, height: Int): Int {
    return width * height
}

print(area(3, 4))
const room = area(5, 2)
print(room)
```

```text title="Output"
12
10
```

A call to `area` is a value like any other: it can be printed, stored, or used in a calculation.
`return` also ends the function at once, so anything after it doesn't run.

Every way through a function that promises an answer has to give one. Here, a number that isn't
positive falls out of the bottom with nothing to return:

```emerald
func sign(n: Int): String {
    if n > 0 {
        return "positive"
    }
}
```

```text title="Output"
functions.em:1:6: not every path in `sign` returns a value
  func sign(n: Int): String {
       ^^^^
Add a `return` on every path, or restructure so every branch returns.
```

Emerald can usually work out the answer's type itself, so `: Int` can be left off `area`. Writing it
is a good habit anyway: it tells a reader what to expect without reading the code.

## Returning early

A function can return from several places. The one-line `return ... if` form suits a function that
settles simple cases first:

```emerald
func describe(age: Int): String {
    return "a baby" if age < 1
    return "a child" if age < 13
    return "a teenager" if age < 20
    return "an adult"
}

print(describe(0))
print(describe(15))
print(describe(40))
```

```text title="Output"
a baby
a teenager
an adult
```

## Default values and named arguments

A parameter can have a default value, used when the call leaves it out. Parameters with defaults
come after the ones without:

```emerald
func greet(name: String, punctuation: String = "!") {
    print("Hello, #{name}#{punctuation}")
}

greet("Ada")
greet("Grace", "?")
greet("Hopper", punctuation: "!!!")
```

```text title="Output"
Hello, Ada!
Hello, Grace?
Hello, Hopper!!!
```

The last call *names* its argument, `punctuation: "!!!"`. Naming arguments makes a call easier to
read, especially when several are numbers: `area(width: 3, height: 4)` says which is which. Named
arguments can come in any order, but they go after any unnamed ones.

Each name declares one function. There can't be two functions called `show`, one for numbers and one
for text; give them different names, or use a default value.

## Where functions can go

A function can be called before the line it is declared on, so a program can put its main code at
the top and its helper functions below:

```emerald
greet()

func greet() {
    print("Hi from below")
}
```

```text title="Output"
Hi from below
```

## Parameters can't be changed

A parameter is a constant inside the function; it holds the value it was given:

```emerald
func bump(n: Int) {
    n += 1
}
```

```text title="Output"
functions.em:2:5: `n` cannot be reassigned
      n += 1
      ^
Parameters are read-only. Assign it to a local variable first if you need a version that can change.
```

A list passed to a function is the function's own copy, so a change to it would vanish when the
function ends. Emerald refuses the change rather than let it silently disappear:

```emerald
func add_guest(guests: List[String], guest: String) {
    guests.append(guest)
}
```

```text title="Output"
functions.em:2:5: `guests` is a parameter, so a change to it would be lost when the function returns
      guests.append(guest)
      ^^^^^^
Copy it into a `var`, change the copy, and return it, as in `var changed = guests`.
```

The fix is to return the changed list, and have the caller keep it:

```emerald
func add_guest(guests: List[String], guest: String): List[String] {
    var updated = guests
    updated.append(guest)
    return updated
}

var party = ["Ada"]
party = add_guest(party, "Grace")
print(party)
```

```text title="Output"
["Ada", "Grace"]
```

The page on [classes](../classes/) introduces objects that are shared rather than copied, for when
several parts of a program need to change the same thing.

## A function that calls itself

A function may call itself. This is called *recursion*, and suits problems that contain smaller
copies of themselves:

```emerald
func factorial(n: Int): Int {
    return 1 if n <= 1
    return n * factorial(n - 1)
}

print(factorial(5))
```

```text title="Output"
120
```

A recursive function that returns a value must state its return type, since Emerald can't work it
out from a call to itself. Each call must get closer to a case that stops, here `n <= 1`; without
one, the calls would go on until Emerald stops them with an error.

## What you've learned

- `func name(parameters) { ... }` declares a function, and `name(arguments)` calls it.
- Parameters have types, and Emerald checks every call.
- `: Type` after the parentheses and `return` give back an answer; every path must return one.
- Parameters can have defaults, and arguments can be named.
- A function can be called before its declaration.
- Parameters can't be changed; return a changed copy instead.
- A function can call itself, if it states its return type and always reaches a stopping case.

Next, [lambdas and blocks](../lambdas-and-blocks/): functions without names, passed to other
functions.
