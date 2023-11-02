# Profiling

In Python, the operation of verifying whether a specific example x belongs to S is efficient when S is declared as a set and is inefficient when S is declared as a list.

Using PyPy, Numba or similar tools to compile your Python code into fast, optimized machine code.

## cProfile
Use cProfile package in Python to find inefficiencies in your code.
```sh
python -m cProfile -s time my.py
```
But generally it's more convenient to run the code once and save the results to a file. Then do the analysis later.

## cProfile and pstats
```
python -m pstats my.profile
```

## cProfile and snakeviz
SnakeViz has two visualization styles, 'icicle' and 'sunburst'.
```
1. pip install snakeviz
2. python -m cProfile -o my.profile my.py
3. snakeviz my.profile
```

## Linux
https://stackoverflow.com/questions/51982417/pandas-mask-where-methods-versus-numpy-np-where
```
perf record python np_where.py
perf report
```
