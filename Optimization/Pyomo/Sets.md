# Sets
https://pascua.iit.comillas.edu/aramos/simio/transpa/s_GoodOptimizationModelingPracticesPyomo.pdf

## basic
```py
model.rng_set = RangeSet(1,10,2) # [1,3,5,7,9]
model.set_1 = Set(initialize=[i for i in range(6)])    # init with a list
model.set_2 = Set(initialize=('red', 'green', 'blue')) # init with a tuple
```

## Subsets

## Lag and lead operators: first/last, prev/next

## Circular indexes (prew/nextw)

## Union, intersection of sets
