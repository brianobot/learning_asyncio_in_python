"""
Having been introduced to the concepts and syntax around the generator functions,
which when called returns a generator object which then can be ran and paused 
according to the distribution of yield statements in the function's body.

sometimes it is important and necceary to send some data back into the generator function
essentially allowing for bidirectional communication between the generator object and its
caller, the generator objects response by yield some value and also listen in on some input
from the caller by applying the yield key word is a different syntax
"""


# Fibonacci Series with Generators funtions in python
def fibonacci_series(n):
    first, second = 0, 1
    for i in range(n):
        yield first
        first, second = second, first + second
        

# generator to generate first 20 fib numbers
for fib in fibonacci_series(30):
    print(fib, end=" ")


def foo():
    x = 100
    print(f"Initial value of x = {x}")
    while True:
        x = yield x
        print(f"Value of X after receiviing = {x}")


"""
IF you are like me, you are probably getting the hang of all these intuitively
but can't seem to see how all these play together in the asyncio ecosystem in python.

Apparently this concepts are importance for foundational understanding, even though this generator
and coroutines functions are not explicitly used in the asyncio syntax, it is so because the asyncio
hides this implementation away, but there are still there and the idea of a loop running is still there,
and the sleeping of functions to be later awoke with their states and stack frames saved are still there.
"""