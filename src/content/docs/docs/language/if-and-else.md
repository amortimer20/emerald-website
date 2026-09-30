---
title: If and Else
sidebar:
  order: 8
description: Run code only when a condition holds, choose between several paths, and pick one of two values.
---

So far every program has run each line, top to bottom. `if` lets a program decide: it runs a block
of code only when a condition is `true`.

```emerald
const temperature = 25
if temperature > 20 {
    print("Warm")
}
print("done")
```

```text title="Output"
Warm
done
```

The condition, `temperature > 20`, comes after `if`, and the code to run goes between braces, `{`
and `}`. The code inside is indented by four spaces so a reader can see it belongs to the `if`.
Change the temperature to `15` and only `done` is printed.

The condition must be a `Bool`: a comparison, a `true` or `false` value, or a question such as
`name.empty?()`. [Booleans and Comparison](../booleans-and-comparison/) covers them.

## Else

`else` gives the code to run when the condition is `false`:

```emerald
const age = 11
if age >= 13 {
    print("You can join the club.")
}
else {
    print("Come back in a year or two!")
}
```

```text title="Output"
Come back in a year or two!
```

Exactly one of the two blocks runs, never both. `else` starts its own line, after the closing brace.

## Choosing among several paths

`else if` adds another condition to try when the ones before it were `false`:

```emerald
const temperature = 12
if temperature < 0 {
    print("Freezing")
}
else if temperature < 20 {
    print("Cool")
}
else {
    print("Warm")
}
```

```text title="Output"
Cool
```

The conditions are tried in order, and the first one that is `true` wins; the rest are skipped. So
`temperature < 20` only needs to mean "cool", because freezing temperatures were already taken care
of. The final `else` catches everything left over, and can be left off if nothing should happen
then.

When there are many cases for one value, [case](../case/) is often clearer.

## Blocks inside blocks

A block can hold any code, including another `if`:

```emerald
const age = 15
const member = true
if age >= 13 {
    if member {
        print("Welcome back!")
    }
}
```

```text title="Output"
Welcome back!
```

Often the two conditions can be joined instead, `if age >= 13 and member`, which is easier to read.

A name declared inside a block belongs to that block and disappears when it ends:

```emerald
if true {
    const message = "inside"
}
print(message)
```

```text title="Output"
decisions.em:4:7: [E1001] `message` is not defined
  print(message)
        ^^^^^^^
Check the spelling, or declare it before this line.
```

To use a value after the block, declare the name before it and assign it inside, as
[Variables and Constants](../variables-and-constants/#declaring-now-assigning-later) showed.

## One action, one line

When a condition guards a single action, the `if` can go after it, on one line:

```emerald
const score = 150
print("Bonus!") if score > 100
print("Tiny score") if score < 10
```

```text title="Output"
Bonus!
```

This form suits a short action and has no `else`. It works with a call, an assignment, `return`,
`break`, or `continue`, but not a declaration.

## Choosing a value

Sometimes the decision is between two values rather than two actions. `if ... then ... else` gives
one value or the other:

```emerald
const score = 12
const label = if score >= 10 then "winner" else "playing"
print(label)
```

```text title="Output"
winner
```

Both answers are needed, since the expression must have a value either way:

```emerald
const n = 3
const size = if n > 2 then "big"
```

```text title="Output"
decisions.em:2:33: an `if` used as a value needs an `else`
  const size = if n > 2 then "big"
                                  ^
Give a value for both outcomes: `if condition then value else other_value`.
```

And both answers must be the same kind of value: `if n > 2 then "big" else 7` is an error, because
`size` would be text or a number depending on `n`.

## Braces are required

A block always has braces, even when it holds a single line. `if n > 0 print("positive")` is an
error. This keeps every block looking the same, and there is no way to be misled about which lines
an `if` controls.

The opening brace can go at the end of the `if` line, as on this page, or on the line after it;
`emerald format` keeps a whole project to one style, which a project can choose in its
`emerald.toml`.

## What you've learned

- `if condition { ... }` runs a block only when the condition is `true`.
- `else` runs when it is `false`, and `else if` tries another condition; the first true one wins.
- A name declared in a block exists only inside it.
- `action if condition` guards one action on one line.
- `if condition then a else b` chooses between two values, and needs both.

Next, [case](../case/): choosing among many possibilities for one value.
