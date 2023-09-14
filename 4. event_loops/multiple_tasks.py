"""
In the intro ,we covered the process of getting the event loop, creating a coroutine
and a task from the coroutine and eventually putting the task on the event loop
and running the event loop.

but ofcourse asyncio is really only useful if we have multiple task to run.
lets use the example below
"""

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