# PyInvoke

https://docs.pyinvoke.org/en/stable
```
from invoke import task
@task
def build(c):
    print("Building!")
```
in shell run 
```
invoke build
```

https://github.com/pyinvoke/invoke

a Python library for managing shell-oriented subprocesses and organizing executable Python code into CLI-invokable tasks. 
```sh
invoke git.version
```
output
```
DEBUG: Executing `git describe --long --always --dirty`
0.14.0-0-g5dab79a
{"dirty": false, "tag": "0.14.0", "commit_number": 0, "hash": "5dab79a", "version": "0.14.0"}
```
