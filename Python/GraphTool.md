# Graph tool

## graphviz
conda install graphviz python-graphviz pydot
```
from graphviz import (
    Graph,
    Digraph,
)

f = Graph('test', format='png')
for k, v in data.item():
  f.node(k, v)
f.edges(['ab', 'ac', 'bd', 'ce', 'cf'])
f.reder('test', view=True)

f = Digraph(filename='c:/test.gv")

data = {
    'a': 'CEO',
    'b': 'Team-A', 'c': 'Team-B',
    'd': 'Staff-A', 'e': 'Staff-B', 'f': 'Staff-C', 
}
#nodes
for k, v in data.item():
    if k == 'a':
        f.node(k, v, shape='oval')        
    elif k in ['b', 'c']:
        f.node(k, v, shape'box')
    else:
        f.node(k, v, shape='plaintext')
#edges
f.edge('a', 'b')
f.edge('a', 'c')
f.edge('b', 'd')
f.edge('c', 'e')
f.edge('c', 'f')
    
f
```

## schemdraw
```
import schemdraw
from schemdraw.flow import *

with schemdraw.Drawing() as d:
    d += Start.lable('start')
    d += Data(w=3).lable('input')
    d += Process(w=5).lable('process')
    d += Decision(w=5).lable('decision')
    d += Arrow(w=5).right.lable('test')
```
