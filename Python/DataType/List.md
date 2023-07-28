# List

## add two lists
```py
l = [1,2] + [3]
```

## duplicat items in list
```py
l = [1] * 3
```

## nested list
```py
#nested list
a = [[0] * 4 for i in range(3)]
```

## diff between two lists
```py
s1 = set(l1).difference(l2)
```

## remove empty items
```py
l2 = list(filter(None, l1))
```

## check all None
```py
l.count(None)==len(l)
all(v is None for v in l) #10x slower
```

## remove duplicate in list and keep order
```py
from collections import OrderedDict
lst = [1,2,4,2,5]
unique_list = list(OrderedDict.fromkeys(lst)) #python < 3.7
unique_list = list(dict.fromkeys(lst))        #python >= 3.7
```

## transpose list of tuples
```py
list_of_tuples = [(1,2), (3,4)]
list(zip(*list_of_tuples))
```
