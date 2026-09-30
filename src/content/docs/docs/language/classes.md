---
title: Classes
sidebar:
  order: 20
description: Types whose values are shared objects rather than copies, when to choose one over a struct, and keeping fields private.
---

A *class* is declared just like a struct, with fields, a constructor, and methods. The difference is
what happens when a value is given to another name. A struct is copied. A class value is an *object*,
and every name that holds it refers to the same object:

```emerald
class BankAccount {
    var balance: Int = 0

    func deposit(amount: Int) {
        self.balance += amount
    }
}

const mine = BankAccount()
const also_mine = mine
also_mine.deposit(50)
print(mine.balance)
print(mine)
```

```text title="Output"
50
BankAccount(balance: 50)
```

`also_mine` isn't a second account; it is another name for the same one, so a deposit through either
name shows up through both. Had `BankAccount` been a struct (kept in `var`s, since `deposit` changes
it), `also_mine` would have been a copy, and `mine.balance` would still be `0`.

## Sharing is the point

Sharing is what you want when several parts of a program deal with one thing. A function given an
object can change it, and the caller sees the change:

```emerald
class Player {
    var score: Int = 0
}

func reward(player: Player) {
    player.score += 10
}

const ada = Player()
reward(ada)
reward(ada)
print(ada.score)
```

```text title="Output"
20
```

Compare this with [Functions](../functions/): a list or struct passed to a function is the function's
own copy, which it can't change. An object is shared, so it can.

## `const` stops at the object

`const ada = Player()` means `ada` will always refer to the same player. It doesn't freeze the player:
the object's `var` fields can still change, as `ada.score` did above, and its methods can change it.
A `const` field is different: it never changes, whoever holds the object.

```emerald
class Player {
    const name: String
    var score: Int = 0
}

const p = Player("Ada")
p.name = "Bob"
```

```text title="Output"
classes.em:7:3: `name` is a `const` field of Player, so it cannot change
  p.name = "Bob"
    ^^^^
Declare it `var name: String` in Player if it needs to change.
```

## Same object, or same values?

Two structs are equal when their fields are equal. Two objects are equal only when they are the same
object:

```emerald
class Box {
    var n: Int = 0
}

const a = Box()
const b = Box()
const c = a
print(a == b)
print(a == c)
```

```text title="Output"
false
true
```

`a` and `b` are two separate boxes that happen to hold the same number; `c` is `a` itself.

## Keeping fields private

A name that starts with an underscore is *private*: only code inside the class's own braces can use it.
This lets a class protect its fields and offer methods instead, so the rest of the program can't put
it into a state that makes no sense:

```emerald
class BankAccount {
    var _balance: Int = 0

    func deposit(amount: Int) {
        self._balance += amount
    }

    func balance(): Int {
        return self._balance
    }
}

const account = BankAccount()
account.deposit(20)
print(account.balance())
account._balance = 1000000
```

```text title="Output"
classes.em:16:9: `_balance` is private to `BankAccount`
  account._balance = 1000000
          ^^^^^^^^
Only code written inside `BankAccount`'s braces can reach a name that starts with `_`.
```

Emerald checks this before the program runs. The same rule works for structs, and for methods too: a
helper method named with `_` is for the type's own use.

## Struct or class?

- Use a **struct** for a value: a point, a date, a score, a color. Two with the same fields are
  interchangeable, and copying one is natural.
- Use a **class** for a thing with an identity that several parts of the program share and change:
  a bank account, a player in a game, a game board.

When unsure, start with a struct. It is simpler to reason about, since nothing else can change it
behind your back.

## What you've learned

- A class is declared like a struct, but its values are shared objects, not copies.
- A function given an object can change it, and everyone holding it sees the change.
- `const` fixes which object a name refers to, not the object's `var` fields.
- Objects are equal only when they are the same object.
- A name starting with `_` is private to its type.
- Structs suit values; classes suit shared things with an identity.

Next, [properties](../properties/): fields worked out when they are read.
