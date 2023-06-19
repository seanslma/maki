# Pipeline

## transactional pipeline
command in the pipeline will be executed once but will block other commands.
```
example
```py
def trans():
    pipe = r.pipeline(True)
    pipe.incr('trans:', 2)
    time.sleep(.1)
    pipe.incr('trans:', -1)
    ret = pipe.execute()
    print(ret[0])
for i in xrange(5):
    threading.Thread(target=trans).start()
    time.sleep(.5)
```

## non-transactional pipeline
still execute the commands in the pipeline without blocking other commands, for the benefit of increading performance.
```
pipe = r.pipeline(False)
pipe.xyz()
pipe.execute()
```
