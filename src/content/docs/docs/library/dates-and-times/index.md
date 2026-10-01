---
title: Dates and Times
description: Which type to use for a day, a time on the clock, an exact moment, or a length of time.
sidebar:
  order: 0
  label: Overview
---

Emerald has a separate type for each thing a program can mean by "a time". They aren't
interchangeable, and that is deliberate: a birthday, a deadline, and a timeout are different kinds of
thing, and Emerald checks that one isn't used where another was meant.

| Type | Means | Prints as |
| --- | --- | --- |
| [`Date`](date/) | A day on the calendar: a birthday, a due date | `2026-09-25` |
| [`Time`](time/) | A time on the clock: an alarm, opening hours | `14:30:00` |
| [`DateTime`](datetime/) | A date and a time together, with no zone: what a calendar and wall clock show | `2026-09-25T14:30:00` |
| [`Instant`](instant/) | An exact moment, the same everywhere: a timestamp, a deadline | `2026-09-25T18:30:00Z` |
| [`Duration`](duration/) | An exact length of time: a timeout, a lap time | `1h 30m` |
| [`TimeZone`](timezone/) | Where the clocks are, which decides what time a moment shows | `Europe/Paris` |
| [`Stopwatch`](stopwatch/) | A way to measure how long something takes | |

[`Weekday`](weekday/) names the days of the week, and [`DateTimeError`](datetimeerror/) is what is
raised when a value can't be made. To pause a program for a length of time, see
[`Program.sleep`](../program/program/#sleep).

```emerald
const today = Date(2026, 9, 25)
var birthday = Date(2026, 3, 14)
if birthday < today {
    birthday = birthday.add(years: 1)
}
print("#{today.days_until(birthday)} days to go")
```

```text title="Output"
170 days to go
```

## Calendar steps and exact lengths

Two kinds of arithmetic look alike but behave differently, so they are written differently.

[`Duration`](duration/) and [`Instant`](instant/) are *exact*, so they have operators: an `Instant` plus
a `Duration` is always the same moment.

A step on the *calendar* depends on where it starts, since months differ in length. So `Date` and
`DateTime` have methods with named units, such as `date.add(months: 1)`, which from 31 January lands
on the last day of February. The unit is always named, because `add(5)` wouldn't say whether it meant
days or years; Emerald refuses it and lists the units.

A calendar day and 24 hours usually agree, but not on a day the clocks change. In New York, on the
day the clocks go forward, adding a calendar day keeps the time on the clock, while adding 24 exact
hours moves the clock on by one more hour:

```emerald
const new_york = TimeZone("America/New_York")
const noon = DateTime(2026, 3, 7, 12)

print(noon.add(days: 1))
print(noon.to_instant(new_york).after(Duration(days: 1)).to_date_time(new_york))
```

```text title="Output"
2026-03-08T12:00:00
2026-03-08T13:00:00
```

## Reading and writing text

Every value prints in the international standard form shown in the table, which reads the same in
every country and sorts correctly as text. Each type's `parse` reads that form back, and `parse_maybe`
gives `nothing` instead of raising an error. For another layout, put the parts into text yourself:

```emerald
const day = Date(2026, 9, 25)
print("#{day.weekday}, #{day.month_name} #{day.day}, #{day.year}")
```

```text title="Output"
Friday, September 25, 2026
```

## Time zones

A function that needs a zone takes an optional `zone`, and uses the computer's own, `TimeZone.local`,
when you give none. Named zones come from a copy of the international time zone database built into
Emerald, so a program gives the same answer on every computer.
