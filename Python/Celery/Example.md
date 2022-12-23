# Example
```py
from celery import Task, registry, Celery

class Task01(Task):
    _v: float
    def __init__(self):
        self._v = 0   
    def execute(self, x):
        self._v += x
        return self._v

app = Celery(
    'tasks', 
    broker='redis://localhost:6379',
    backend='redis://localhost:6379',
)
@app.task(base=Task01)
def task_01(x):
    val = task_01.execute(x)
    return val
```       
