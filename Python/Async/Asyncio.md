# Asyncio
https://docs.python.org/3/library/asyncio-eventloop.html

## call async function
```py
import asyncio
async def async_func():
    df = pd.read_parquet('data.parquet')
    return df
    
if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        df = loop.run_until_complete(async_func())
    finally:
        loop.close()
```

## async to sync
```py
def sync(coro):
    loop = asyncio.new_event_loop()
    future = asyncio.run_coroutine_threadsafe(coro, loop)
    return future.result()
```
