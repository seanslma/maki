# Redis

## check redis server availability
```py
import redis

def check_redis_availability():
    # Create a StrictRedis instance
    redis_client = redis.StrictRedis(host='localhost', port=6379, decode_responses=True)

    try:
        # Ping the Redis server
        response = redis_client.ping()
    except Exception as e:
        print(f'Error checking Redis availability: {e}')
    else:
        if response:
            print('Redis server is available.')
        else:
            print('Redis server did not respond to PING.')

# Check if Redis server is available
check_redis_availability()
```

## cache df
```py
import io
import time
import pyarrow as pa
import pyarrow.parquet as pq
import redis
r = redis.StrictRedis(host='my-redis', port=6379)

def paqdumps(df):
    buf = io.BytesIO() 
    d = pa.Table.from_pandas(df)    
    pq.write_table(d, buf, compression='zstd')      
    b = buf.getvalue()
    r.set('df', b)
    return b

def paqloads():
    b = r.get('df') 
    buf = pa.BufferReader(b)
    return pq.read_table(buf).to_pandas()  

t0 = time.time(); _ = paqdumps(df)  ; print(f'dump time: {time.time() - t0}')
t0 = time.time(); dx = paqloads()  ; print(f'load time: {time.time() - t0}')
```
