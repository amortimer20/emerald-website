---
title: Projects and Namespaces
sidebar:
  order: 29
description: Grow a program beyond one file with a project folder, reach names in other folders through their namespace, and keep helpers private to a file.
---

Every program so far has been one file. That is enough for a long while, but a bigger program is
easier to find your way around when it is split up: one file for each part, folders for related parts.
In Emerald, a folder of files that work together is a *project*.

## A folder with main.em

A folder becomes a project when it holds a file named `main.em`. Every `.em` file in the folder, and in
the folders inside it, is then part of the program. There is nothing to import and no list of files to
keep: put a file in the folder, and its functions and types are available.

Here is a small project for planning a vegetable garden:

```text title="Files"
garden/
├── main.em
└── plants/
    ├── plant.em
    └── catalog.em
```

```emerald title="plants/plant.em"
struct Plant {
    const name: String
    const days_to_harvest: Int
}
```

```emerald title="plants/catalog.em"
const _catalog = [Plant("Tomato", 60), Plant("Radish", 25)]

func all(): List[Plant] {
    return _catalog
}

func quick(): List[Plant] {
    return all().filter({ plant => plant.days_to_harvest < 30 })
}
```

```emerald title="main.em"
for plant in Plants.all() {
    print("#{plant.name}: #{plant.days_to_harvest} days")
}
print(Plants.quick())
```

From inside the `garden` folder, run the project by running its main file:

```text title="emerald run main.em"
Tomato: 60 days
Radish: 25 days
[Plant(name: "Radish", days_to_harvest: 25)]
```

`main.em` is where the program starts. Only its statements run; the other files declare functions,
types, and constants for it to use. A statement anywhere else is an error, since it would never run.
Here, `print("loading the catalog")` was added to the end of `catalog.em`:

```text title="emerald run main.em"
plants/catalog.em:11:1: this would never run
  print("loading the catalog")
  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Only the entry file runs its top level. Move this into `main.em`, or into a function declared in this file.
```

## Folders are namespaces

Everything declared in the `plants` folder has its name inside a *namespace* called `Plants`: the
folder's name, capitalized the way a type is. That is why `main.em` writes `Plants.all()`. A folder
named `garden_tools` would be `GardenTools`. The file names add nothing: `all` is `Plants.all` whether
it lives in `catalog.em` or anywhere else in the folder, so moving it between files there changes
nothing.

Files in the same folder share a namespace, so they see each other's names directly. `catalog.em` uses
`Plant` from `plant.em` without writing `Plants.Plant`.

From another folder, the namespace is needed, and Emerald says so if it is left out:

```text title="emerald run main.em"
main.em:1:7: `quick` is not visible here
  print(quick())
        ^^^^^
It is declared in `Plants`. Write `Plants.quick`, or add `using Plants` at the top of this file.
```

## using

`using Plants` at the top of a file lets that file use the namespace's names directly:

```emerald title="main.em"
using Plants

print(quick())
print(Plant("Basil", 30))
```

```text title="emerald run main.em"
[Plant(name: "Radish", days_to_harvest: 25)]
Plant(name: "Basil", days_to_harvest: 30)
```

A `using` applies only to the file it is written in. If two namespaces you are using both have a name,
Emerald asks you to write which one you meant. `using` can also give a single name a shorter one, as
in `using Size = Pizza.Size` from [Nested Types](../nested-types/).

## Private to a file

A name starting with `_` is private to the file that declares it. `_catalog` above is used by the
functions beside it, but no other file can reach it, not even one in the same folder:

```text title="emerald run main.em"
main.em:1:7: `_catalog` is private to the file that declares it
  print(Plants._catalog)
        ^^^^^^^^^^^^^^^
A module-level name starting with `_` cannot be reached from another file. Remove the underscore to make it public.
```

This keeps the details of a file its own, so it can change them without breaking the rest of the
program. Other files use `all()` and `quick()`, which stay the same however the plants are stored.

## A folder without main.em

A folder with no `main.em` isn't a project, and each file in it is its own program. That suits a folder
of exercises: `emerald run exercise1.em` never sees `exercise2.em` beside it, even if both declare a
function with the same name.

The same happens if you run a file from inside a project directly, such as
`emerald run plants/catalog.em`: it runs on its own, without the rest of the project. Its names from
other files are then missing, and Emerald points to the project's main file instead.

## Your names and Emerald's

Emerald's own built-ins, such as `print`, `random`, and `File`, live in a namespace named `Emerald`
that every file can see without a `using`. A name your program declares always wins over a built-in
with the same name. Hiding one of the core built-ins gets a warning, and the built-in can still be
reached through `Emerald`:

```emerald
func random(): Int {
    return 4
}

print(random())
print(Emerald.random(1..6) <= 6)
```

```text title="emerald check"
projects.em:1:6: warning: `random` hides Emerald's built-in `random`
  func random(): Int {
       ^^^^^^
A name the program declares always wins, so `random` here means this one. Write `Emerald.random` to reach the built-in, or choose a different name.
```

Declaring a standard-library name, such as a `File` struct of your own, is silent, since you may well
mean your own. `Emerald.File` still reaches the built-in one.

## What you've learned

- A folder holding `main.em` is a project; every `.em` file inside it is part of the program.
- Only `main.em` runs statements; other files declare functions, types, and constants.
- A folder is a namespace named like a type, such as `Plants`; files in one folder share it.
- `Plants.all()` reaches a name in another folder; `using Plants` lets a file drop the prefix.
- A name starting with `_` is private to its file.
- Your names win over built-ins, which stay reachable as `Emerald.name`.

Next, [annotations](../annotations/): the `@` words that tell Emerald something about a declaration.
