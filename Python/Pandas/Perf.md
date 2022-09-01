# Performance

## get is faster
```python
import timeit

a1 = df.get('name').unique() #fastest
a2 = df.name.unique()        #ok
a3 = df['name'].unique()     #slow

t1 = timeit.Timer(lambda: df.get('name').unique())
print(t1.timit(10)
```

https://llllllllll.github.io/principles-of-performance/index.html

https://speakerdeck.com/pycon2018/jake-vanderplas-performance-python-seven-strategies-for-optimizing-your-numerical-code

https://speakerdeck.com/nnja/nina-zakharenko-the-basics-of-memory-management-in-python-north-bay-python-2018

https://software.intel.com/en-us/articles/large-matrix-operations-with-scipy-and-numpy-tips-and-best-practices

http://conference.scipy.org/proceedings/scipy2018/pdfs/anton_malakhov.pdf

http://conference.scipy.org/proceedings/scipy2017/pdfs/oleksandr_pavlyk.pdf
