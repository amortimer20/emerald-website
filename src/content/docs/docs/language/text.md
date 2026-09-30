---
title: Text
sidebar:
  order: 5
description: Strings of text, putting values into them, the characters they hold, and the everyday things you do with them.
---

A piece of text is a `String`. You have already written some: anything between double quotes is a
string.

```emerald
const greeting = "Hello"
const name = "Ada"
print(greeting, name)
```

```text title="Output"
Hello Ada
```

## Putting values into text

`#{...}` inside a string puts a value into the text, as [The First Program](../the-first-program/)
showed. Whatever is between `#{` and `}` is worked out first, so it can be any expression:

```emerald
const apples = 3
print("I have #{apples} apples, or #{apples * 2} halves.")
```

```text title="Output"
I have 3 apples, or 6 halves.
```

Strings can also be joined with `+`, but only to other strings. Interpolation is usually easier to
read, and it works with any value:

```emerald
const first = "Ada"
const last = "Lovelace"
print(first + " " + last)
print("#{first} #{last}")
```

```text title="Output"
Ada Lovelace
Ada Lovelace
```

## Special characters

Some characters can't be typed straight into a string. A backslash starts an *escape*, a short code
for one:

```emerald
print("She said \"hi\"")
print("one\ttwo")
print("first line\nsecond line")
print("a backslash: \\")
print("not interpolated: \#{name}")
```

```text title="Output"
She said "hi"
one	two
first line
second line
a backslash: \
not interpolated: #{name}
```

`\"` is a double quote, `\t` a tab, `\n` a new line, `\\` a backslash, and `\#` a `#` that doesn't
start an interpolation. `\u{e9}` writes a character by its Unicode number, which is handy for one
that is hard to type or invisible, such as a combining accent.

## Longer text

Text that spans several lines goes between triple double quotes:

```emerald
const poem = """
    Roses are red,
      violets are blue.
    """
print(poem)
```

```text title="Output"
Roses are red,
  violets are blue.
```

The text starts on the line after the opening `"""`, and the closing `"""` goes on a line of its
own. The indentation before the closing quotes is removed from every line, so the string can be
indented to match your code while any extra indentation, like the second line's, is kept.
Interpolation and escapes work here too.

## Text taken exactly as written

A string in single quotes is *raw*: backslashes and `#{` are just characters. That suits text full of
backslashes, such as a Windows path:

```emerald
print('C:\new\folder')
print('no #{name} here')
```

```text title="Output"
C:\new\folder
no #{name} here
```

In double quotes, `\n` in that path would have become a new line.

## Characters

A string is a sequence of characters, and `count` says how many:

```emerald
const word = "café"
print(word.count)
print(word[0], word[3])
```

```text title="Output"
4
c é
```

`word[0]` is the first character; counting starts at 0, so the last one is `word[count - 1]`.
Emerald counts characters the way a reader sees them, so `é` is one character, and so is an emoji
built from several parts, such as a family 👨‍👩‍👧.

A range of positions gives part of a string. `..<` stops before its end, and `..` includes it:

```emerald
const word = "Emerald"
print(word[0..<3])
print(word[3..])
```

```text title="Output"
Eme
rald
```

Asking for a position the string doesn't have is an error that says which positions it does have:

```emerald
print("cat"[5])
```

```text title="Output"
text.em:1:7: index 5 is outside this String, which has 3 characters
  print("cat"[5])
        ^^^^^^^^
Valid indices are 0 through 2.
```

## Strings don't change

Once made, a string can't be changed in place. Methods that seem to change one, like `upper`, give
back a new string and leave the original as it was:

```emerald
var word = "cat"
word[0] = "b"
```

```text title="Output"
text.em:2:1: a String cannot be changed in place
  word[0] = "b"
  ^^^^^^^
Strings are immutable. Build a new one instead, for example with `replace` or interpolation.
```

A `var` can still be given a whole new string: `word = "bat"`.

## Everyday things to do with text

```emerald
const line = "  Hello, World  "
print(line.trim())                 # remove spaces from both ends
print(line.trim().upper())         # capitals
print(line.contains?("World"))     # does it appear?
print("a,b,c".split(","))          # break into a list
print("cat".replace("c", "b"))     # swap one piece for another
print("ha".repeat(3))              # repeat
```

```text title="Output"
Hello, World
HELLO, WORLD
true
["a", "b", "c"]
bat
hahaha
```

Methods can be chained, one after another, reading left to right: `line.trim().upper()` trims,
then capitalizes. A method whose name ends in `?`, like `contains?`, answers a yes-or-no question.
The [String](../../builtins/types/string/) page lists every method.

## Comparing and converting

`==` compares two strings exactly, capitals included, and `<` compares them alphabetically:

```emerald
print("Ada" == "Ada", "a" == "A", "apple" < "banana")
```

```text title="Output"
true false true
```

To turn a number into text, interpolate it or call `to_string()`; to turn text into a number, call
`to_int()` or `to_float()`:

```emerald
print(42.to_string() + "!")
print("42".to_int() + 1)
```

```text title="Output"
42!
43
```

## What you've learned

- A string is text in double quotes; `#{...}` puts a value into it, and `+` joins strings.
- Escapes such as `\n` and `\"` write special characters; triple quotes hold several lines; single
  quotes take text exactly as written.
- `count`, `[i]`, and ranges read the characters, counted as a reader sees them, from 0.
- Strings never change; their methods give back new strings.
- `==` and `<` compare text; `to_string`, `to_int`, and `to_float` convert.

Next, [booleans and comparison](../booleans-and-comparison/): true, false, and questions a program
can ask.
