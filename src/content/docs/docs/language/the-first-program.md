---
title: The First Program
sidebar:
  order: 1
description: Write a program, run it, print text, ask a question, and read what Emerald says when something is wrong.
---

A program is a list of instructions that the computer carries out in order, from the top of the
file to the bottom. This page writes one, runs it, and then grows it a little at a time.

If you haven't yet, [install Emerald](/install/) first.

## Hello, world

Make a file named `hello.em` containing one line:

```emerald
print("Hello, world!")
```

Then open a terminal in the folder where you saved it, and run it:

```bash
emerald run hello.em
```

```text title="Output"
Hello, world!
```

That line is a complete program. `print` is a function built into Emerald: it shows whatever you
give it, then moves to a new line. The text between the double quotes is a string, Emerald's word
for a piece of text. The quotes mark where the string starts and ends; they are not printed.

Every Emerald file ends in `.em`, and `emerald run` runs one.

## One line after another

A program with several lines runs them in order:

```emerald
print("Ready...")
print("Set...")
print("Go!")
```

```text title="Output"
Ready...
Set...
Go!
```

`print` can show more than one value at once. Separate them with commas, and it puts a space
between each:

```emerald
print("The answer is", 42)
```

```text title="Output"
The answer is 42
```

`42` has no quotes because it isn't text, it is a number. With nothing between the parentheses,
`print()` prints an empty line.

## Asking a question

`input` shows a prompt, waits for someone to type an answer and press Enter, and gives back what
they typed:

```emerald
const name = input("What is your name? ")
print("Hello, #{name}!")
```

```text title="Terminal"
What is your name? Ada
Hello, Ada!
```

Here `Ada` is what the person typed. Two new things are at work:

- `const name = ...` gives the answer a name, so the next line can use it. The page on
  [variables and constants](../variables-and-constants/) explains names properly.
- `#{name}` inside a string puts a value into the text. Whatever is between `#{` and `}` is worked
  out, and the result takes its place. It can be any expression, not only a name:

```emerald
const apples = 3
print("You have #{apples * 2} apples.")
```

```text title="Output"
You have 6 apples.
```

The space at the end of `"What is your name? "` is deliberate: without it, the answer would be
typed right up against the question mark.

## When something is wrong

Everyone makes mistakes when writing programs, and a lot of programming is reading what the
computer says about them. Emerald checks the whole program before it runs any of it, and when
something is wrong it says what, where, and what to try. Suppose `print` is misspelled:

```emerald
pritn("Hello")
```

```text title="Output"
hello.em:1:1: [E1001] `pritn` is not defined
  pritn("Hello")
  ^^^^^
Check the spelling, or declare it before this line.
```

Read a message from the top:

- `hello.em:1:1` is where the problem is: the file, then the line, then the column (how many
  characters along the line).
- Then comes what is wrong, in plain words. `[E1001]` is the problem's code;
  `emerald explain E1001` shows a longer explanation with an example.
- The line itself is shown, with `^` marks under the part that is wrong.
- The last line suggests what to do about it.

Because Emerald checks first, nothing runs until every problem is fixed. A program never gets
halfway and then stops over a typo on its last line.

Two more mistakes nearly everyone meets early on. A string needs its closing quote:

```emerald
print("Hello)
```

```text title="Output"
hello.em:1:7: this string is never closed
  print("Hello)
        ^
Close it with `"` before the line ends.
```

And text and numbers can't be added together with `+`, because it isn't clear what adding them
would mean:

```emerald
print("Age: " + 12)
```

```text title="Output"
hello.em:1:7: `+` joins two Strings, but this is String and Int
  print("Age: " + 12)
        ^^^^^^^^^^^^
Convert the value with `to_string()`, or use interpolation, as in `"#{name}: #{score}"`.
```

The suggestion is the usual way to write it: `print("Age: #{12}")`.

## Checking without running

`emerald check` looks for problems without running the program:

```bash
emerald check hello.em
```

```text title="Output"
No problems found.
```

It is useful for a program that asks questions or takes a long time, when you only want to know
whether it is correct so far.

## What you've learned

- A program runs its lines in order, top to bottom, and `emerald run file.em` runs it.
- `print` shows values; a string is text between double quotes.
- `input` asks a question and gives back the answer.
- `#{...}` puts a value into a string.
- Emerald checks the whole program first, and its messages say what is wrong, where, and what to
  try.

Next, [comments](../comments/) let you leave notes in a program for the people who read it.
