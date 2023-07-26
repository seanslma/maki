# List

## remove duplicate in list and keep order
```py
from collections import OrderedDict
lst = [1,2,4,2,5]
unique_list = list(OrderedDict.fromkeys(lst)) #python < 3.7
unique_list = list(dict.fromkeys(lst))        #python >= 3.7
```
