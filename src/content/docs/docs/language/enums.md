---
title: Enums
sidebar:
  order: 24
description: Types with a fixed set of named values, and why case works so well with them.
---

Some values come from a short, fixed list: a direction is north, south, east, or west; a traffic light
is red, yellow, or green. An *enum* is a type made of exactly such a list of named values:

```emerald
enum Direction {
    north, south, east, west
}

const heading = Direction.north
print(heading)
print(heading == Direction.south)
```

```text title="Output"
Direction.north
false
```

`enum Direction` lists its values, separated by commas or on separate lines. A value is always written
with the enum's name, `Direction.north`, so it can't be confused with anything else, and it prints the
same way.

## Why not a string?

You could store `"north"` in a `String`, but nothing would stop a typo like `"nrth"` from slipping
through and quietly never matching. An enum value can only be one of its listed values, and a
misspelling is caught at once, with the real values listed:

```emerald
enum Light {
    red, yellow, green
}

print(Light.blue)
```

```text title="Output"
enums.em:5:7: `Light` has no value or type-level member named `blue`
  print(Light.blue)
        ^^^^^^^^^^
Check the spelling. The values of `Light` are `red`, `yellow`, `green`.
```

## Enums and case

Because an enum's values are all known, a [case](../case/) can list every one of them, and Emerald can
check that it does. A `case` that produces a value needs no `else` when it covers them all:

```emerald
enum Direction {
    north, south, east, west
}

func arrow(heading: Direction): String {
    return case heading {
        when Direction.north then "↑"
        when Direction.south then "↓"
        when Direction.east then "→"
        when Direction.west then "←"
    }
}

print(arrow(Direction.east))
```

```text title="Output"
→
```

Leave one out, and Emerald names the missing values:

```emerald
enum Direction {
    north, south, east, west
}

const heading = Direction.north
const word = case heading {
    when Direction.north then "up"
    when Direction.south then "down"
}
```

```text title="Output"
enums.em:6:14: this `case` gives no value for `Direction.east` or `Direction.west`
  const word = case heading {
               ^^^^
A `case` that produces a value needs one for every possible subject. Add an arm for each, or `else then ...` after the last arm.
```

A `case` of blocks that misses a value is allowed, but gets a warning:

```emerald
enum Light {
    red, yellow, green
}

const light = Light.red
case light {
    when Light.red {
        print("Stop")
    }
    when Light.green {
        print("Go")
    }
}
```

```text title="emerald check"
enums.em:6:1: warning: this `case` does not cover `Light.yellow`
  case light {
  ^^^^
Add an arm for each, or `else { }` to accept the gap deliberately.
```

This is the real payoff. If you later add `Light.flashing`, every `case` that doesn't handle it is
pointed out, instead of silently doing nothing.

## Enums with methods

An enum can have methods, declared after its values. Inside, `self` is the value the method was
called on:

```emerald
enum Light {
    red, yellow, green

    func next(): Light {
        return case self {
            when Light.red then Light.green
            when Light.green then Light.yellow
            when Light.yellow then Light.red
        }
    }
}

print(Light.red.next())
```

```text title="Output"
Light.green
```

An enum can't have stored fields; its values are just names. An enum can be the type of a field, which
is where it is often most useful:

```emerald
enum Suit {
    hearts, diamonds, clubs, spades
}

struct Card {
    const rank: Int
    const suit: Suit
}

print(Card(10, Suit.hearts))
```

```text title="Output"
Card(rank: 10, suit: Suit.hearts)
```

## What you've learned

- `enum Name { a, b, c }` declares a type with exactly those values, written `Name.a`.
- An enum catches misspellings that a string would let through.
- A `case` over an enum can cover every value; Emerald names any it misses.
- Enums can have methods, and can be the type of a field, but have no stored fields.

Next, [nested types](../nested-types/): types declared inside other types.
