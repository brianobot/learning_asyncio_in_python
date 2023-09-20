"""
Recapping from the lesson of the last module.

Asyncio involve creating tasks to be executed on an event loop
and then running the event loop with the task place on it.


"""
import asyncio


async def greet(word):
    for count in range(5):
        await asyncio.sleep(0)
        print(word)


loop = asyncio.get_event_loop()


loop.create_task(greet("Hello"))
loop.create_task(greet("Goodbye"))

tasks = asyncio.all_tasks(loop=loop)
print(f"tasks: {tasks}")
group = asyncio.gather(*tasks)
print(f"Group: {group}")
loop.run_until_complete(group)

"""
This doesn't really show much aside introducing the ability to get a set of all the tasks
on an event loop and creating a group from that set.

We are shown another way to run the event loop, which runs until all the tasks in a group
have completed.
"""
import time
import requests

# Classic web scraper using the requests library

urls = [
    "https://brianobot.github.io/",
    "https://www.github.com/brianobot/",
    "https://www.linkedin.com/in/brian-obot-924b49216/",
]

sizes = {}

start_time = time.time()

for url in urls:
    content = requests.get(url).content
    sizes[url] = len(content), time.time() - start_time

total_time = time.time() - start_time
print("_"*40)
print(f"It Took {total_time} seconds")
print("_"*40)
print(f"{sizes = }")


"""
Let's redo this with the asyncio 
"""

async def measure_url_content(url):
    content = requests.get(url).content
    return content


loop = asyncio.get_event_loop()

start_time = time.time()
for one_url in urls:
    loop.create_task(measure_url_content(one_url))

tasks = asyncio.all_tasks(loop=loop)
group = asyncio.gather(*tasks)

loop.run_until_complete(group)

total_time = time.time() - start_time
print(f'It took {total_time} seconds')