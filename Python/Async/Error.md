# Error

## RuntimeWarning: coroutine 'DefaultAzureCredential.get_token' was never awaited
The coroutine function has never been called correctly.
```py
import asyncio
async def my_coro():
    print('Hello there')
coro = my_coro() #will throw the warning: only creates a coroutine object not run the coroutine

#correct way to call the coroutine
asyncio.run(my_coro())
#or
await my_coro()
```
