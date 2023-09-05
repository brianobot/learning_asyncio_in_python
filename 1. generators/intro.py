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


