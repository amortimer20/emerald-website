---
title: Tasks and Channels
description: Let several pieces of work wait at once, and pass values between them.
sidebar:
  order: 0
  label: Overview
---

Much of what a program does is waiting: for a web server to answer, for a file, for a person to type, or
for a pause to end. If each wait must finish before the next begins, the waits add up. *Tasks* let
independent pieces of work wait at the same time, so a program that fetches four pages takes about as
long as the slowest one, not the sum of all four.

```emerald
const started = Instant.now()

const squares = Tasks.run { tasks =>
    var jobs: List[Task[Int]] = []
    for n in 1..4 {
        jobs.append(tasks.start { =>
            Program.sleep(Duration(milliseconds: 100))
            return n * n
        })
    }
    return jobs.map { job => job.result() }
}

print(squares)
print(Instant.now() - started < Duration(milliseconds: 300))
```

```text title="Output"
[1, 4, 9, 16]
true
```

Each of the four tasks waits for a tenth of a second, and together they take about a tenth of a second
rather than four tenths. Nothing in the program says `async` or `await`, and there are no threads or
locks to look after.

## How tasks work

- **`Tasks.run` makes a group.** Its block gets a [`TaskGroup`](taskgroup/), whose `start` begins a
  [`Task`](task/). `Tasks.run` doesn't return until every task started in the group has finished, so no
  task is left running after the code that started it has moved on.
- **A task gives a result.** `start` takes a block, and the block's value is the task's result, read
  with `result()`. If the task fails, `result()` raises its error.
- **One task runs at a time.** Tasks overlap their *waiting*, not their calculating. This is
  concurrency, not use of several processor cores: a task that is busy calculating holds up the others
  until it waits or calls [`Tasks.yield`](tasks/#yield).
- **Channels pass values between tasks.** A [`Channel`](channel/) is a queue that one task sends into
  and another receives from, waiting for each other as needed.

When a task or the group fails, the others are cancelled, their cleanup runs, and then the error
continues up, so a failure never leaves work half running. [Cancelling](task/#cancel) is also how a
program stops work it no longer needs.

## At a glance

| Page | What it covers |
| --- | --- |
| [`Tasks`](tasks/) | `Tasks.run` to make a group, and `Tasks.yield` to let others run |
| [`TaskGroup`](taskgroup/) | `start`, which begins a task, and the rules for task blocks |
| [`Task`](task/) | `result`, `wait`, `done?`, and `cancel` |
| [`Channel`](channel/) | Sending values between tasks |
| [`CancelledError`](cancellederror/) | What a cancelled task raises |
| [`DeadlockError`](deadlockerror/) | What is raised when every task is stuck waiting |

## Limits

Emerald's tasks don't use more than one processor core, there are no tasks that outlive their group, and
there is no way to wait on several channels at once. At most 64 tasks can be live at one time; a task
that has finished doesn't count, so a long run can start many more than 64 in total.
