# Pipeline

## transactional pipeline
command in the pipeline will be executed once but will block other commands.
```
pipe = r.pipeline(True)
pipe.xyz()
pipe.execute()
```

## non-transactional pipeline
still execute the commands in the pipeline without blocking other commands, for the benefit of increading performance.
```
pipe = r.pipeline(False)
pipe.xyz()
pipe.execute()
```
