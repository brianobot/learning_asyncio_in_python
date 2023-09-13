"""
In All Modern OS, there are a list of processes running on the computer system (performing some action).
Now since the processes are usually much more the available processors, the OS has to periodically
suspend execution of some processes for other to have their own fair share of time to execute, the 
OS knows how to suspend this process, and how to restart such that the process continues from where it 
stopped. this form is multitasking is called pre-emptive.

Now this idea is essential and applicable to the asyncio ecosystem, but unlike the operating system
which handles the switching, the event loop, which is an infinitely running while loop switches between
different events (functions) allowing each to execute and willingly give up control when sleeping and waiting
for some input, output.

Whenever python encounters the await key inside a task running on an event loop, python knows
that task is willing to give up control for other tasks to run, usually this wait because this task
has to perform IO based task which would cause time delay.

this further goes to showcase why there is an "io" in asyncio showing that it is best suited for io
related tasks, cause even in the fastest network there is bound to be some form of time taken.

it is important to reemphasize here that even though thread over similar benefits and architecture to some 
extent, it is more tricky to manage threads that it is to manage task in the asyncio ecosystem.

We can not use await inside normal python functions, since normal functions can pause their state and
expect to run until return before moving to the another task, and again normal functions are ran directly
and dont have to be put in an event loop to manage it execution but task in the asyncio do.

Modern python introduces 'async def' keyword to indicate task that can be put in an event loop and normal functions, 
these tasks can not be ran directly as this would lead to an error.

```
So, here's the story so far:
- In the world of asyncio, we don't run functions ourselves.
Rather, we define functions with "async def".
An async function can be turned into a task, and thus attached to the event loop.
You cannot run an async function on your own; it can only run in the event loop.
A task indicates that it's willing to give up the CPU in favor of another task with "await"
We use "await" to indicate that we're waiting for something that will take some time, typically I/O.
```
clipped from the email containing the tutorial i learnt from
"""