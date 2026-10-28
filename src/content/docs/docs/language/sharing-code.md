---
title: Sharing Code
sidebar:
  order: 31
description: Use a library someone else wrote by copying its folder into your project, and write one others can copy.
---

Sooner or later you'll want code someone else wrote, or you'll write something worth sharing.
Emerald has no package manager to download libraries for you. A library is a folder, and you
use one by copying it into your project. Because every folder in a project is a
[namespace](../projects-and-namespaces/), the library is ready as soon as it's there.

## Using a library

Say a classmate shares `geometry`, a folder of shapes and measurements. Copy that folder to the
top of your project, beside `main.em`:

```text title="Files"
my_game/
├── main.em
└── geometry/          ← copied in, unchanged
    ├── measure.em
    └── shapes/
        ├── shape.em
        ├── circle.em
        └── rectangle.em
```

`geometry/` is now the `Geometry` namespace, and `geometry/shapes/` is `Geometry.Shapes`:

```emerald title="main.em"
const room = Geometry.Shapes.Rectangle(5, 4)
print(Geometry.describe(room))
print(Geometry.total_area([room, Geometry.Shapes.Circle(1)]).round_to(2))
```

```text title="emerald run main.em"
rectangle: 20.0
23.14
```

There's nothing to install and nothing to configure. The version you have is the one you copied:
to update it, copy the new one over it. It's worth noting where a library came from, in a comment
or a README, so you know where to look for a newer one.

## Writing a library others can copy

A library is ordinary Emerald files in a folder. Three rules make it work when someone copies it
into their own project, and each one comes from namespace paths starting at the top of a project.

**It refers to itself by its own name.** Inside `geometry/`, a file writes
`Geometry.Shapes.Shape`, not `Shapes.Shape`:

```emerald title="geometry/measure.em"
func describe(shape: Geometry.Shapes.Shape): String {
    return "#{shape.name()}: #{shape.area().round_to(2)}"
}
```

Wherever the folder is copied, `Geometry.Shapes` still means the same thing. The short form
doesn't work, and Emerald says so while you're writing the library:

```text title="emerald run main.em"
geometry/measure.em:1:22: `Shapes.Shape` is not a type
  func describe(shape: Shapes.Shape): String {
                       ^^^^^^^^^^^^
Check the spelling or declare the struct in this project.
```

**It has no top-level code.** Only the project's own `main.em` runs statements, so a library holds
functions, types, and constants. A `main.em` inside the library would never run, and Emerald
says that too:

```text title="emerald run main.em"
geometry/main.em:1:1: this would never run
  print("demo")
  ^^^^^^^^^^^^^
Only the project's own `main.em` runs its top level, so `geometry/main.em` never does. A library keeps its demo in the project around it; move this there, or into a function declared in this file.
```

**It lives in a project of its own.** Put the library folder beside a `main.em` that shows it off.
That `main.em` is where you try the library while you write it, and anyone who wants to use the
library copies only the `geometry/` folder:

```text title="Files"
geometry-library/
├── main.em            ← the demo, run with `emerald run main.em`
├── README.md          ← what it does, and how to copy it
└── geometry/          ← the library itself
```

Two libraries with the same folder name can't both be copied into one project; rename one, and
change the name it uses for itself to match.

## Libraries that ship with Emerald

Everything in the [Built-ins](../../builtins/) and the standard library comes with Emerald itself,
already installed. Libraries that need more than Emerald code, such as graphics and sound, will
come that way too, rather than as folders to copy.

## What you've learned

- A library is a folder. Copy it beside your `main.em`, and its folder name is its namespace.
- The version you have is the one you copied; updating means copying again.
- A library calls itself by its own name, such as `Geometry.Shapes.Shape`.
- A library has no top-level code; its demo lives in a project around it.

Next, [annotations](../annotations/): the `@` words that tell Emerald something about a declaration.
