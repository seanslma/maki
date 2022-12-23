# Example
```py
from celery import Task, registry, Celery

class Task01(celery.Task):
    _v = 0
    def add(self, x):
        self._v += x
        return self._v

cly = Celery(
    'tasks', 
    broker='redis://localhost:6379',
    backend='redis://localhost:6379',
)
@cly.task(base=Task01)
def task_01(x):
    val = task_01.add(x)
    return val
```       
