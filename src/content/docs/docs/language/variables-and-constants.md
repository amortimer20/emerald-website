---
title: Variables and Constants
sidebar:
  order: 3
description: Give a value a name, change it later or promise it never changes, and let Emerald keep track of its type.
---

A program remembers values by giving them names. A name that can be given a new value later is a
*variable*, declared with `var`. A name that keeps its first value for good is a *constant*,
declared with `const`.

```emerald
var score = 0
const limit = 100
```

Both lines declare a name and give it a value with `=`. After this, `score` and `limit` can be used
wherever their values could.

## Variables change

A variable's value can be replaced with `=`:

```emerald
var score = 0
print(score)
score = 10
print(score)
```

```text title="Output"
0
10
```

Changing a variable by some amount is so common that it has a shorter way to write it. `+=` adds to
it, `-=` subtracts, `*=` multiplies, and `/=` divides:

```emerald
var score = 10
score += 5    # now 15
score -= 3    # now 12
score *= 2    # now 24
print(score)
```

```text title="Output"
24
```

`score += 5` means exactly `score = score + 5`.

## Constants don't

A constant keeps the value it was declared with. Trying to change one is an error, caught before
the program runs:

```emerald
const limit = 100
limit = 200
```

```text title="Output"
variables.em:2:1: [E3001] `limit` cannot be reassigned
  limit = 200
  ^^^^^
It was declared with `const`. Use `var` if the value needs to change.
```

Use `const` whenever a value won't need to change, which is most of the time. It tells a reader
they can stop wondering whether the value changes somewhere further down, and Emerald holds the
program to that promise.

A constant list or other collection can't change either, not even by adding to it:

```emerald
const scores = [1, 2]
scores.append(3)
```

```text title="Output"
variables.em:2:1: [E3001] `scores` is a `const`, so its contents cannot change
  scores.append(3)
  ^^^^^^
Declare `scores` with `var` if it needs to change.
```

## Every name has a type

Every value in Emerald has a *type*, the kind of value it is: `Int` for a whole number, `Float` for a
number with a fractional part, `String` for text, `Bool` for true or false, and many more. A
variable takes its type from its first value and keeps it, so it can't later hold a different kind
of value:

```emerald
var count = 3
count = "three"
```

```text title="Output"
variables.em:2:9: this is String, but `count` holds Int
  count = "three"
          ^^^^^^^
Assign a value of the declared type, or convert it first.
```

Emerald works out the type from the value, so you rarely write it. When you want to say it
yourself, write it after the name with a colon:

```emerald
var price: Float = 3
print(price)
```

```text title="Output"
3.0
```

Here the type makes `3` a `Float`, which is why it prints as `3.0`. The page on
[numbers](../numbers/) explains the difference.

## Declaring now, assigning later

A variable can be declared with only a type and given its value later, as long as it gets one before
it is used:

```emerald
var greeting: String
const hour = 9

if hour < 12 {
    greeting = "Good morning"
}
else {
    greeting = "Good afternoon"
}
print(greeting)
```

```text title="Output"
Good morning
```

Emerald checks every path through the program, so it notices when one of them leaves the variable
without a value. Take away the `else`, and the afternoon has no greeting:

```emerald
var greeting: String
const hour = 9

if hour < 12 {
    greeting = "Good morning"
}
print(greeting)
```

```text title="Output"
variables.em:7:7: `greeting` may not have been assigned
  print(greeting)
        ^^^^^^^^
Assign `greeting` on every branch before reading it.
```

A declaration needs either a value or a type; `var x` on its own is an error, since there is no way
to tell what it will hold. (`if` and `else` have a page of their own:
[if and else](../if-and-else/).)

## One name, one declaration

Once a name is declared, declaring it again is an error, even inside a block:

```emerald
var score = 1
var score = 2
```

```text title="Output"
variables.em:2:5: `score` is already declared
  var score = 2
      ^^^^^
Each name can have one declaration in a scope. Choose a different name, or remove the duplicate.
```

To give an existing variable a new value, leave off the `var`: `score = 2`. And a name must be
declared before it is used, so `total = 5` with no `var total` first says `` `total` is not defined
``.

## Naming

- Names are written in `snake_case`: lowercase words joined by underscores, such as
  `high_score` or `seconds_left`. Type names, which come later, are written in `PascalCase`, such
  as `String`.
- A name can contain letters, digits, and underscores, but can't start with a digit.
- Names are case-sensitive: `score` and `Score` are different names.
- Choose names that say what the value means. `seconds_left` is clearer than `s` or `time2`.

## What you've learned

- `var` declares a variable, which can be given a new value with `=`, `+=`, and the rest.
- `const` declares a constant, which never changes; prefer it whenever you can.
- Every value has a type, and a name keeps the type of its first value. Write the type after a colon
  when you want to state it.
- A variable can be declared first and assigned later, if every path gives it a value before it is
  read.
- A name is declared once, before it is used, in `snake_case`.

Next, [numbers](../numbers/): whole numbers, fractional ones, and arithmetic.
