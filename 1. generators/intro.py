"""
Please ensure to read the README before starting off with this intro.

it has laid the conceptual foundation upon which this and later lessons would build upon
Brian Obot.


Like mentioned in the intro, the threading and multiprocessing are two ways to try
and do more things are once in a computer system, even though threading isn't exactly 
doing the things in parallel, it does give this feeling. and the reason python threads doesn't
run in parallet in mostly due to a thing called the GIL (Global Interpreter Lock), and not forgetting that
threads are sort of tricky and hard to work with.


In Asyncio, the systemm doesn't decide when a process should give up control for other process to be executed
but it is the process that willing gives up control while attending to some time delaying IO operations
like writing to a file or reading from a network. and it would resume where it left when controls finally comes round 
to it again.


"""


"""
GENERATORS.

Unlike normal functions that when called are ran from top to bottom and optional return a value,
the generator function return their value through a yield statement everything it is called by a next function
directly or indirectly through a for loop.

Example below
"""

def normal_function():
    # does some action in the function body
    # nothing interesting to see here, lets move on to return a value
    return 12


result = normal_function() # the function is called and the result value is assigned to a variable
print(f"\nthe return value of the {normal_function.__name__} is {result}")


def generator_function():
    # function body 
    yield 1
    yield 2
    yield 3

# in order to get the values from the generator functions, lets use a for loop
for item in generator_function():
    print(item)

"""
Now to the function presented above, it's a typical function declaration and calling process,
for most common functions the function starts and returns almost immediately ... and the other part
of the program is ran ..but some functions have to do some waiting for some external resources, like download
some data from the web, or read data from a file, or write data into a file.
"""
