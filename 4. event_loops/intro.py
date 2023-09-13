"""
Coming from the theory set up in the async and await lessons,
it is time to start doing some actual work
"""

import asyncio

loop  = asyncio.get_event_loop()

# it is that event to create or get an event loop
# whenever the get_event_loop function in the asyncio module is called
# it returns an event loop, to be more precise, it returns the event loop,
# since they can only be a single event loop in the system at a given time (its a singleton)

# so invoking get_event_loop mutiple times would always give the same event loop

# once gotten, the event loop can be started with the run_forever method
# loop.run_forever() # comment out to run the event loop

"""
now what we have done works, the event loop starts and actually runs until stop() is called

but there are 2 problems
- first, it get to run forever
- and then not task has been place in the loop, which is kind of the whole point of the loop
"""

# inorder to make use of the event loop we need to write a coroutine, 
# this is more like  regular function only that it is defined with the async key word infront
# the normal function def keyword.


async def greet():
    print("Hello World!")


# just like with generator functions, calling the coroutinr directly would produce a coroutine object

obj = greet()
print(f"Coroutine Objects: {obj}")


# in order to run the coroutine in the loop we need to create a task from the coroutine and run the loop

# loop = asyncio.get_event_loop()
# loop.create_task(greet())
# loop.run_forever()

"""
now this sort of works but then the program hangs, until killed with ctrl-c 
this is because after our coroutine (task) finished running the loop went on to 
well, run forever 🙂
"""

# to be able to stop the loop after the task completes, let call the stop method at the end of the task


async def greet():
    print("Hello")
    loop.stop()


loop.create_task(greet())
loop.run_forever()

# that seem pretty nice 