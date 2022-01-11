# Profiling

## cProfile and snakeviz
Draws a pie chart with the problem function in the biggest piece.
```
1. pip install snakeviz
2. python -m cProfile -o temp.dat my.py
3. snakeviz temp.dat
```
