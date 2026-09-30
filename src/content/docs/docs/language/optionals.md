---
title: Optionals
sidebar:
  order: 13
description: Values that might be missing, how Emerald makes you handle them, and the simple ways to do it.
---

Sometimes a value might not be there. Turning `"42"` into a number works, but turning `"hello"` into
one can't. Rather than crashing or making up a number, Emerald gives back a special value, `nothing`,
which means "no value":

```emerald
print("42".to_int_maybe())
print("hello".to_int_maybe())
```

```text title="Output"
42
nothing
```

`to_int_maybe` gives back an *optional*: either an `Int`, or `nothing`. Its type is written `Int?`,
read "maybe an Int". The `?` means the value might be missing.

## You have to handle the missing case

An `Int?` isn't an `Int`, so it can't be used like one until you've dealt with the chance that it
is `nothing`:

```emerald
const age = "42".to_int_maybe()
print(age + 1)
```

```text title="Output"
optionals.em:2:7: addition needs numbers, but this is Int? and Int
  print(age + 1)
        ^^^^^^^
One of these may be absent. Give it a fallback with `.or(0)`, or check it against `nothing` first.
```

This is the point of optionals: a missing value can't slip through unnoticed and cause a crash
later. Emerald catches it before the program runs, and the message suggests the two ways to handle
it.

## Check it

Compare the value with `nothing`. Inside the branch where it can't be `nothing`, Emerald knows it is
an `Int`, and lets you use it as one:

```emerald
const answer = input("How old are you? ")
const age = answer.to_int_maybe()
if age == nothing {
    print("Please type a number.")
}
else {
    print("Next year you will be #{age + 1}.")
}
```

```text title="Terminal"
How old are you? 12
Next year you will be 13.
```

In a function, a guard at the top often reads best: return early when the value is missing, and the
rest of the function can treat it as present:

```emerald
func half(text: String): Int {
    const n = text.to_int_maybe()
    return 0 if n == nothing
    return n // 2
}

print(half("10"))
print(half("ten"))
```

```text title="Output"
5
0
```

## Or give a fallback

`.or(value)` gives back the value if it is there, and the fallback if it is `nothing`. The result is
never missing, so it is a plain `Int`:

```emerald
const age = "abc".to_int_maybe().or(0)
print(age)
```

```text title="Output"
0
```

Use `.or` when there is a sensible default, and a check when a missing value needs different
handling.

## Declaring an optional

Write `?` after a type to let a name hold `nothing`:

```emerald
var nickname: String? = nothing
print(nickname)
nickname = "Addy"
print(nickname)
```

```text title="Output"
nothing
Addy
```

Without the `?`, a name can never be `nothing`, and Emerald refuses to put `nothing` in it. So when
you see a type without `?`, you know the value is always there.

## Functions that might have no answer

A function whose answer might be missing says so in its return type, and returns `nothing` when it
has no answer:

```emerald
func find_score(name: String): Int? {
    return 90 if name == "Ada"
    return nothing
}

print(find_score("Ada"))
print(find_score("Bob"))
```

```text title="Output"
90
nothing
```

Every path must still return something, `nothing` included; a function never gives back `nothing`
just by reaching its end.

Many built-in methods work this way: `list.first` is `nothing` for an empty list, and `input_maybe`
gives `nothing` when there is no more input. Their names and types tell you so.

## When the check stops counting

Emerald remembers a check only while the value can't have changed. Give a checked `var` a new value
and the check no longer counts:

```emerald
var n = "4".to_int_maybe()
if n != nothing {
    n = nothing
    print(n + 1)
}
```

```text title="Output"
optionals.em:4:11: addition needs numbers, but this is Int? and Int
      print(n + 1)
            ^^^^^
One of these may be absent. Give it a fallback with `.or(0)`, or check it against `nothing` first.
```

A `const` can't change, so a check on a `const` always counts, which is one more reason to prefer
`const`.

## Reaching into something that might be missing

When a struct or class value might be missing, `?.` reaches one of its fields only if the value is
there, and gives `nothing` otherwise: `player?.name`. It comes up once you have your own types, on
the [structs](../structs/) and [classes](../classes/) pages.

## What Emerald doesn't have

If you know another language: there is no `null`; `nothing` is Emerald's word, and only a type with
`?` can hold it. There is no `??` operator; write `.or(fallback)`. And a type can't be optional twice:
`Int??` is an error, since one `?` already says the value might be missing.

## What you've learned

- `Int?` means "an `Int`, or `nothing`"; `nothing` means no value.
- An optional can't be used as a plain value until the missing case is handled.
- Check it against `nothing` (or return early), and Emerald treats it as present afterwards.
- `.or(fallback)` gives a plain value with a default.
- `?` after a type lets a name hold `nothing`; without it, the value is always there.
- A function whose answer might be missing returns an optional type.

Next, [lists](../lists/): keeping many values in order.
