# numpy
```python
x = np.arange(5)
```

## tile/repeat
```python
a = np.array([1, 2])
np.tile(a,2) #duplicate the array n times
np.repeat(a,2) #duplicate each element n times
```

## join array
```python
#join a sequence of arrays along an existing axis
a = np.array([[5, 6]])
b = np.array([[1, 2], [3, 4]])
np.concatenate((a, b), axis=0)
np.concatenate((a, b), axis=None)
```
## reshape
```python
import numpy as np
d = np.array([[1,2,3],[4,5,6],[7,8,9]])

# row by row
d.reshape(-1, order='c')
#array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# col by col
d.reshape(-1, order='f')
#array([1, 4, 7, 2, 5, 8, 3, 6, 9])

#when no intention to change the new array
# it will be faster to use 
d.ravel(order='c')
d.ravel(order='f')
```

## sort
```python
people = np.array(people)
ages = np.array(ages)
ind = ages.argsort()
sortedPeople = people[ind]
```
## max value and index
```python
#get all max values
ind = np.where(a == a.max())
#get only first max value
ind = np.unravel_index(a.argmax(), a.shape)
```

## top n min val
```python
#1d arr
ind = np.argpartition(d1, n-1)[:n]

#ind in order
min_val = arr[ind]
min_val_order = np.argsort(min_val)
ordered_ind = ind[min_val_order]

#2d arr
flat_ind = np.argpartition(d2.ravel(), n-1)[:n]
row_ind, col_ind = np.unravel_index(flat_ind, d2.shape)

#ind in order
min_val = arr[row_ind, col_ind]
min_val_order = np.argsort(min_val)
row_ind, col_ind = row_ind[min_val_order], col_ind[min_val_order]
```

## apply function
```python
def my_func(a):
    return (a[0] + a[-1]) * 0.5
b = np.array([[1,2,3], [4,5,6], [7,8,9]])
np.apply_along_axis(my_func, 0, b) #col by col
#out array([4., 5., 6.])
np.apply_along_axis(my_func, 1, b) #row by row
#out array([2.,  5.,  8.])
```

## elems in a not in b
```python
#numpy
a = np.array([1,2,3,4,5,6,7])
b = np.array([2,4,6,8])
msk = np.in1d(a, b)
a[~msk]
np.setdiff1d(a, b)

#pandas
msk = (pd.Index(pd.unique(b)).get_indexer(a) >= 0)
a[~msk]
```
