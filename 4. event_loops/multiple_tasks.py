"""
In the intro ,we covered the process of getting the event loop, creating a coroutine
and a task from the coroutine and eventually putting the task on the event loop
and running the event loop.

but ofcourse asyncio is really only useful if we have multiple task to run.
lets use the example below
"""
print("Start of First Greet Iteration.")
print("________________________________")

import asyncio 


loop = asyncio.get_event_loop()


async def greet():
    print("Hello")
    loop.stop()


async def goodbye():
    print("goodbye")
    loop.stop()


loop.create_task(greet())
loop.create_task(goodbye())
loop.run_forever()

"""
Running the above code works, but we don't get to see the concurrent nature of the event loop
since both function would stop produce the same output if called one after the other in the normal 
python function utility.

Inorder to get a feel of the concurrent nature of the event loop, let make the task to do more than 
one thing each
"""
print("Start of Second Greet Iteration.")
print("________________________________")

async def greet_2(word):
    for i in range(5):
        print(word)
    loop.stop()


loop = asyncio.get_event_loop()

loop.create_task(greet_2('hello'))
loop.create_task(greet_2('goodbye'))
loop.run_forever()

"""
when you execute the code above, you will get the result shown below

hello
hello
hello
hello
hello
goodbye
goodbye
goodbye
goodbye
goodbye

which shows linearity and no level of concurrency, that is because we haven't introduce any concurrency
in the code, that is ,we haven't design that task such that it gives up control for other tasks to run.

To do that lets rewrite the task
"""
print("Start of Third Greet Iteration.")
print("________________________________")

async def greet_3(word):
    for i in range(5):
        await asyncio.sleep(0) # this place can be any action that means waiting for some external data
        print(word) # do something with the data in your task
    loop.stop()


loop = asyncio.get_event_loop()

loop.create_task(greet_3('hello'))
loop.create_task(greet_3('goodbye'))
loop.run_forever()


"""
When you use await in a coroutine (function defined with async def) and they can only be used
in such functions, you are telling python (the interpreter) that you wish to give up control for other 
tasks while waiting for data from some source which might take some time, in our case above
we are simulating the await with a sleep function which is equivalent to waiting due to inactivity for
external data.
"""

"""
it must be pointed out that not just any expression can be awaited, but only objects that are awaitable,
we would get to this in short while.
"""