---
title: Loops
sidebar:
  order: 10
description: Repeat code while a condition holds, once for each item or number, and stop or skip ahead when you need to.
---

A loop runs the same block of code again and again. Emerald has two: `while` repeats as long as a
condition is `true`, and `for` repeats once for each item in a collection or number in a range.

## While

```emerald
var lives = 3
while lives > 0 {
    print("Lives left: #{lives}")
    lives -= 1
}
print("Game over")
```

```text title="Output"
Lives left: 3
Lives left: 2
Lives left: 1
Game over
```

Before each time through the block, the condition is checked. While it is `true`, the block runs;
once it is `false`, the program carries on after the loop. Something inside the block has to change
the condition eventually, as `lives -= 1` does here. Without that, the loop would run forever.

## For each item

`for` gives each item of a list a name, one at a time:

```emerald
const names = ["Ada", "Grace", "Hopper"]
for name in names {
    print("Hello, #{name}!")
}
```

```text title="Output"
Hello, Ada!
Hello, Grace!
Hello, Hopper!
```

`name` is a new name for each item, and it exists only inside the loop. Lists have a page of their
own, [Lists](../lists/). A `for` loop can go through a string's characters too: `for letter in
"café"` visits `c`, `a`, `f`, and `é`.

## For each number

A *range* gives the numbers to count through. `1..5` means 1 up to 5, including 5:

```emerald
for number in 1..5 {
    print(number)
}
```

```text title="Output"
1
2
3
4
5
```

`..<` stops *before* its end, which is what you want for positions that start at 0: `0..<3` is 0, 1,
and 2, and `0..<list.count` visits every position in a list.

When you only want to repeat something and don't need the number, name it `_`:

```emerald
for _ in 1..3 {
    print("Hip hip hooray!")
}
```

```text title="Output"
Hip hip hooray!
Hip hip hooray!
Hip hip hooray!
```

## Counting down and skipping

Ranges only count upward. To count down, say so with `down_to`:

```emerald
for n in 3.down_to(1) {
    print(n)
}
print("Liftoff!")
```

```text title="Output"
3
2
1
Liftoff!
```

`step` counts by more than one:

```emerald
for n in (0..10).step(3) {
    print(n)
}
```

```text title="Output"
0
3
6
9
```

Because ranges only count upward, a range that starts past its end simply counts nothing. That makes
a loop like `for i in 1..count` safe when `count` is 0: it doesn't run. When both ends are written as
numbers, though, an empty range can only be a mistake, and Emerald says what you probably meant:

```emerald
for n in 5..1 {
    print(n)
}
```

```text title="Output"
loops.em:1:10: this range is empty, because ranges count upward
  for n in 5..1 {
           ^^^^
Count down with `5.down_to(1)`, or up with `1..5`.
```

[Ranges and Slicing](../ranges-and-slicing/) covers ranges in full.

## Stopping early and skipping ahead

`break` leaves the loop at once. `continue` skips the rest of this time through and goes on to the
next. Both are often written with an `if` after them, on one line:

```emerald
for n in 1..10 {
    continue if n % 2 == 0    # skip even numbers
    break if n > 7            # stop after 7
    print(n)
}
```

```text title="Output"
1
3
5
7
```

`while true` makes a loop that only `break` can end. It suits a loop that should keep going until
something happens:

```emerald input="hi|quit"
while true {
    const answer = input("Say something (or quit): ")
    break if answer == "quit"
    print("You said #{answer}")
}
print("Bye!")
```

```text title="Terminal"
Say something (or quit): hi
You said hi
Say something (or quit): quit
Bye!
```

## A loop might not run at all

Emerald remembers that a loop's block might run zero times, for example over an empty list. So a
variable given its value only inside a loop may still be without one afterwards:

```emerald
var found: Bool
for n in 1..3 {
    found = true
}
print(found)
```

```text title="Output"
loops.em:5:7: `found` may not have been assigned
  print(found)
        ^^^^^
The loop that assigns `found` might not run at all. Give it a value before the loop.
```

Give it a starting value, `var found = false`, and the program works.

The name a `for` loop gives each item can't be changed, since it simply takes the next item each
time. Copy it into a `var` if you need one that changes.

## What you've learned

- `while condition { ... }` repeats while the condition is `true`; something must eventually make it
  `false`, or a `break` must end it.
- `for item in list { ... }` visits each item, and `for n in 1..5` each number; `..<` leaves out the
  end, and `_` is a name for a value you don't need.
- Ranges count upward; `down_to` counts down and `step` skips.
- `break` leaves a loop and `continue` moves on to the next time through.
- A loop's block might not run, so a variable assigned only inside it needs a starting value.

Next, [functions](../functions/): naming a piece of code so you can use it again.
