import asyncio

# async await like in JS B-)
async def count(name, interval, end):
    """prints consequent numbers in interval"""
    time = 0
    while True:
        print(name, ' is ', "{:4.1f}".format(time))

        await asyncio.sleep(interval)
        time += interval
        if time >= end:
            break

async def init():
    fast_task = asyncio.ensure_future(count('counter 1', .3, 7))
    slow_task = asyncio.ensure_future(count('počítadlo', 1, 11))
    await fast_task
    await slow_task

loop = asyncio.get_event_loop() # create the asynchronous event loop
print('async code begins, ETA 11 seconds:\n')
loop.run_until_complete(init())
print('\nasync code ends')
loop.close()

# asyncio.run(init()) # since Python 3.7 this can be written instead of the three lines with loop
# but then I should use asyncio.create_task instead of asyncio.ensure_future

# asyncio is a library for IO - can also handle streams and such
