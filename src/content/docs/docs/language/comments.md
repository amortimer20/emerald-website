---
title: Comments
sidebar:
  order: 2
description: Leave notes in a program for the people who read it, from a single line to a whole paragraph.
---

A comment is a note in a program that Emerald ignores. It is written for people: whoever reads the
program next, which is often you, a few weeks later. A good comment says *why* the code does
something, which the code itself can't always show.

## Line comments

`#` starts a comment that runs to the end of the line:

```emerald
# Greet the player before the game starts.
print("Welcome!")
print("Good luck!")   # This line runs second.
```

```text title="Output"
Welcome!
Good luck!
```

A comment can have a line to itself, or sit after the code on a line. Either way, everything from
the `#` onward is ignored.

A `#` inside a string is just a character, not a comment:

```emerald
print("Room #5")
```

```text title="Output"
Room #5
```

## Turning a line off

Putting `#` in front of a line of code stops it from running without deleting it. This is called
*commenting it out*, and it is a handy way to try a program without one of its lines:

```emerald
print("one")
# print("two")
print("three")
```

```text title="Output"
one
three
```

Remove the `#` to turn the line back on.

## Block comments

For a note longer than a line, `#[` starts a block comment and `]#` ends it. Everything between
them is ignored, however many lines it spans:

```emerald
#[
This program greets the player.
It was written for the first lesson.
]#
print("Hello")
```

```text title="Output"
Hello
```

Block comments can contain other block comments, so commenting out a stretch of code that already
has one inside works as you'd hope.

A block comment needs its `]#`. Without one, the rest of the file would be comment, so Emerald
points at where it started:

```emerald
#[ forgot to close
print("never")
```

```text title="Output"
comments.em:1:1: this block comment is never closed
  #[ forgot to close
  ^^
Close it with `]#`.
```

## Documentation comments

A comment that starts with `##` documents the declaration right below it, such as a function. It
says what the function is for, written for whoever will use it:

```emerald
## Greets someone by name.
func greet(who: String) {
    print("Hello, #{who}!")
}

greet("Ada")
```

```text title="Output"
Hello, Ada!
```

Functions come later, on the page about [functions](../functions/). For now, `##` is a `#` with a
job: it belongs to the declaration that follows it, so keep it directly above one. Documentation
text can use Markdown, such as `code` in backticks.

## Writing useful comments

- Say why, not what. `count += 1   # one more player` repeats the code; a comment saying *why* the
  count starts at 1 is worth keeping.
- Keep comments true. A comment that no longer matches its code is worse than none, so change the
  comment when you change the code.
- Prefer clear names to explaining comments. A variable called `seconds_left` needs no comment
  saying what it holds.

## What you've learned

- `#` starts a comment that runs to the end of the line; a `#` inside a string is only text.
- `#[` and `]#` surround a comment of any length, and can nest.
- `##` documents the declaration below it.
- Commenting out a line turns it off without deleting it.

Next, [variables and constants](../variables-and-constants/): giving values names.
