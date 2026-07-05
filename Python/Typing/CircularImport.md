# Circular Import

## Avoid type hints import
- Use `annotations` and `TYPE_CHECKING`
- `MyClient` is only used for type hints, so don't import it at runtime
- This will also avoid circular import dependencies

## Example 1
```py
# my_api.py
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .my_client import MyClient

class MyAPI:
    def __init__(self, client: MyClient):
        self._client = client

# my_client.py
from ._my_api import MyAPI

class MyClient(object):
    def __init__(self):
        self.api = MyAPI(client=self)
```

## Example 2
```py
# person.py
class Person:
    def __init__(self, name: str):
        self.name = name

# parent.py
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .child import Child

class Parent(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.children: list[Child] = []

# child.py
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .parent import Parent

class Child(Person):
    def __init__(self, name: str):
        super().__init__(name)
        self.parents: list[Parent] = []
```
