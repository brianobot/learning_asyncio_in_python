# learning_asyncio_in_python
Learning asyncio in Python

If you are like me, and i trust many other people that have found themselves in the strange mental place
of not really getting the full gists around the asyncio package or syntax in the python ecosystem, then maybe
this repository might help, or atleast stir more interest in your to dive more into the concept, 
i am documenting my learning here for reference and to help anyone that stumbles upon this repo. 

I Would point to useful materials that highlight the concepts needed for understanding this, i would try
not to duplicate ateraisl here, except neccesary...hope we are on the same page? .
<gives up control to a different section while waiting for the reader's response>


## Intro... 
Since i can't share the complete mail content here, below is a snippet of a mail from [Reuven M. Lerner](https://lerner.co.il/)
Subscribe to his mails [Here](https://sparklp.co/a03dbf14/) 
```
Let's start with some history and comparisons: Back in the olden days (even before I started to use computers),
a computer could only do one thing at a time. And indeed, if you had a home computer before the mid-1990s, then 
your computer could *still* probably only do one thing at a time.

If you were on a home computer at the time, it wasn't necessarily obvious what you would want to happen while 
you were working on your word processor, for example.  But if you had a mainframe (or even a minicomputer) at 
your disposal, it was clearly a waste of resources to have only one person using this enormous power at a given 
time.

Some very clever engineers figured out that you could do "time sharing" on a computer. What this meant was 
that every n fractions of a second, the currently running program (which is, after all, just a bunch of
instructions and data) would be copied into another part of memory, and another program would be copied 
into the running part.  n fractions of a second later, the currently running program would be switched out,
and a third program would be switched in.

In this way, you could have a bunch of people using the same computer at the same time.  Well, they weren't
*really* using it at the same time; the computer was actually only running one program at a time, servicing
one user. But the illusion was powerful enough that it worked pretty well.  By the time I started to use 
Unix systems in the late 1980s, this was standard stuff; even if you were only running text-based programs, 
you could have several of them executing at a given time, each doing its own thing.

The way that such systems worked was known as "pre-emptive multitasking."  Programs weren't asked if
they wanted to give up control and execution.  Rather, every so often the operating system would yank 
control away from them.  With pretty rare exception, though, this worked pretty well; programs didn't 
have to know that they were occasionally being put into the virtual equivalent of an induced coma and then 
revived n fractions of a second later.  Correctly run programs would just keep going, blissfully unaware 
that they had been suspended and restarted.

Then home users wanted to have some of this power. We started to see the Mac "System 7" and Windows 95, 
both of which offered some version of multitasking. But they didn't use pre-emptive multitasking.  Rather, 
they used something known as "cooperative multitasking."

In a cooperative multitasking environment, you still have separate processes, each running in its own 
piece of memory and with its own instructions.  And things are still swapped in and out of active memory.

The difference is that whereas in a pre-emptive multitasking environment, the operating system decides when 
each program's time slice is up, in a cooperative multitasking environment, the program itself says, 
"OK, I'm willing to give up the CPU for now."

```

This history and the introduction of these concepts here would serve to build the proper mindset towards mastering asyncio.
atleast that what i think, cause i am almost at the same level with you right now in terms of understanding what is going on here.
