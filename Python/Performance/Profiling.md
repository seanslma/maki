# Profiling

## cProfile and snakeviz
SnakeViz has two visualization styles, 'icicle' and 'sunburst'.
```
1. pip install snakeviz
2. python -m cProfile -o temp.dat my.py
3. snakeviz temp.dat
```

## Linux
https://stackoverflow.com/questions/51982417/pandas-mask-where-methods-versus-numpy-np-where
```
perf record python np_where.py
perf report
```
