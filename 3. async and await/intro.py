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
"""