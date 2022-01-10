# tips

## get list from Literal
```
import typing_extensions

MyType = typing_extensions.Literal['monkey', 'pig']
MyList = list(typing_extensions.get_args(MyType)) #['monkey', 'pig']
```
