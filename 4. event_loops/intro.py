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