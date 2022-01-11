# perf

## run time
```python
import timeit
t1 = timeit.Timer(lambda: df.column('name').unique())
print(t1.timit(10))
```

## ravel() vs flatten()
np.ravel() will avoid copy if possible and thus faster than flatten() 

## broadcasting rules
when broadcasting is possible, we do not need to use np.tile()
