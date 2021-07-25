# zip etc

## zip
```python
letters = ['a', 'b', 'c']
numbers = [0, 1, 2]
for l, n in zip(letters, numbers):
    print(f'Letter: {l}')
    print(f'Number: {n}')
    
#unzip
pairs = [(1, 'a'), (2, 'b')]
numbers, letters = zip(*pairs)    
```

## sorting in parallel
```python
letters = ['b', 'a', 'd']
numbers = [2, 4, 3]
data1 = list(zip(letters, numbers))
data1.sort() #sort by letters

#or
data = sorted(zip(letters, numbers)) #sort by letters
```
## zip_logest
```python
from itertools import zip_longest

l1 = [1, 2, 3]
l2 = [1, 2]

lt = list(zip_longest(l1, l2, fillvalue=None))
print(lt)  #[(1, 1), (2, 2), (3, None)]
```
