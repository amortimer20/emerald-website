---
title: Case
sidebar:
  order: 9
description: Choose among many possibilities for one value, run the matching block, or produce a value for each.
---

When a decision depends on which of several values something has, a chain of `else if`s gets long
and repetitive. `case` names the value once and lists the possibilities:

```emerald
const day = "Saturday"
case day {
    when "Saturday", "Sunday" {
        print("Weekend!")
    }
    when "Friday" {
        print("Almost there")
    }
    else {
        print("A weekday")
    }
}
```

```text title="Output"
Weekend!
```

`case day` says what is being examined, called the *subject*. Each `when` lists one or more values,
separated by commas, and a block to run when the subject equals one of them. `else` runs when none
match.

## How it runs

- The subject is worked out once.
- The `when`s are tried from top to bottom, comparing with `==`.
- The first one that matches runs its block, and then the whole `case` is done. Only one block ever
  runs.
- If nothing matches, `else` runs. Without an `else`, nothing happens.

```emerald
const n = 9
case n {
    when 1 {
        print("one")
    }
}
print("end")
```

```text title="Output"
end
```

Since the first match wins, a `when` that repeats an earlier value could never run, and Emerald says
so:

```emerald
const n = 1
case n {
    when 1 {
        print("a")
    }
    when 1 {
        print("b")
    }
}
```

```text title="Output"
case.em:6:10: an earlier arm already matches this
      when 1 {
           ^
Arms are tried from the top and the first match runs, so this one never could. Remove it.
```

## Producing a value

A `case` can also give back a value, one for each possibility. Each `when` is followed by `then` and
the value, on one line:

```emerald
const place = 2
const label = case place {
    when 1 then "Gold"
    when 2 then "Silver"
    when 3 then "Bronze"
    else then "No medal"
}
print(label)
```

```text title="Output"
Silver
```

A `case` that produces a value must have one for every possible subject. With a number, the `when`s
can't list them all, so an `else` is required:

```emerald
const place = 2
const label = case place {
    when 1 then "Gold"
    when 2 then "Silver"
}
```

```text title="Output"
case.em:2:15: this `case` needs an `else`, since its arms cannot cover every value
  const label = case place {
                ^^^^
A `case` that produces a value needs one for every possible subject. Add `else then ...` after the last arm.
```

When the `when`s do cover everything, as `true` and `false` do for a `Bool`, the `else` can be left
off. [Enums](../enums/) are where this matters most: a `case` over an enum can list every one of its
values.

A `case` is either all blocks or all `then`s. Mixing the two in one `case` is an error that says so,
and so is producing a value that nothing uses.

## Conditions instead of a subject

Leave out the subject, and each `when` becomes a condition of its own. The first one that is `true`
runs:

```emerald
const temperature = 12
case {
    when temperature < 0 {
        print("Freezing")
    }
    when temperature < 20 {
        print("Cool")
    }
    else {
        print("Warm")
    }
}
```

```text title="Output"
Cool
```

This does the same as an `if`, `else if`, `else` chain. Use whichever reads better; a `case` lines the
conditions up where they are easy to scan.

## Case or if?

- Use `case` with a subject when you are asking *which value* something has.
- Use `if` when the conditions are about different things, or there are only one or two of them.

A `when` compares with `==`, so it matches exact values, not ranges: `when 1..10` is an error.
For "between" questions, use a subjectless `case` with comparisons, such as
`when 1 <= n <= 10`.

## What you've learned

- `case subject { when a, b { ... } else { ... } }` runs the first arm whose value matches.
- The first match wins, only one arm runs, and a repeated value is an error.
- `when ... then value` produces a value, and must cover every possibility, usually with
  `else then ...`.
- A `case` with no subject runs the first `when` whose condition is `true`.

Next, [loops](../loops/): doing something again and again.
