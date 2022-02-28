# Post

## run post
```python
import requests
import json

url = 'https://task.test.com/api/my/url'

def do_post(data):
    resp = requests.post(url, json={'id': None, 'val': 12})
    #json to dic: dic = json.loads(resp.tex)
    print(resp.text)
```

## async post
```python
import aiohttp
import asyncio
import json

url = 'https://task.test.com/api/my/url'

async def do_posts():
    date_ranges = [
        ['2017-01-05', '2017-04-01'],
        ['2017-04-01', '2017-07-01'],
    ]
    async with aiohttp.ClientSession() as session:
        post_tasks = []
        async for date_range in aiter(date_ranges):
            post_tasks.append(do_post(session, url, date_range))
        # now execute them all at once
        await asyncio.gather(*post_tasks)

async def do_post(session, url, date_range):
    async with session.post(
        url,
        json={
            'id': None,
            'start_date': date_range[0],
            'end_date': date_range[1],
        }
    ) as response:
        data = await response.text()
        d = json.loads(data)
        print(f'-> Created post task: {d["task_id"]}')

async def aiter(lst):
    for val in lst:
        yield val

asyncio.run(po_posts())
```
