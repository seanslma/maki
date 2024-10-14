# Chart

## graphviz
Shapes: 
https://graphviz.org/doc/info/shapes.html

- Install `Graphviz`
- `conda install graphviz python-graphviz pydot`
```py
os.environ["PATH"] += os.pathsep + 'C:/Program Files/Graphviz/bin/'
from graphviz import (
    Graph,
    Digraph,
)

#Graph
f = Graph('test', format='png')
for k, v in data.items():
  f.node(k, v)
f.edges(['ab', 'ac', 'bd', 'ce', 'cf'])
f.render('test', view=True)

#Digraph
f = Digraph(filename='c:/test.gv', format='png')
data = {
    'a': 'CEO',
    'b': 'Team-A', 'c': 'Team-B',
    'd': 'Staff-A', 'e': 'Staff-B', 'f': 'Staff-C', 
}
#nodes
for k, v in data.items():
    if k == 'a':
        f.node(k, v, shape='oval')        
    elif k in ['b', 'c']:
        f.node(k, v, shape='box')
    else:
        f.node(k, v, shape='plaintext')
        
#labels
with g.subgraph(name='clusterA') as s:
    s.attr(rank='same')
    s.attr(rankdir='LR') #TB
    s.node('a', 'AA', shape='rnastab')
    s.node('b', 'BB', shape='signature')
#labels
with g.subgraph(name='clusterB') as s:
    s.attr(rank='same')
    s.node('c', 'CC', shape='trapezium')
    s.node('d', 'DD', shape='Mdiamond')  
#invisible edge    
g.edge('a', 'c', ltail='clusterA', lhead='clusterB', style='invis')
#not constrained
#a2 -- a0 [constraint=false];

#edges
f.edge('a', 'b')
f.edge('a', 'c')
f.edge('b', 'd')
f.edge('c', 'e')
f.edge('c', 'f', label='OK\nGo')

f.save()
f.render(view=0, cleanup=1)
f
```

## cloud inforstructure diagrams
```py
from diagrams import Diagram
from diagrams.aws.compute import EC2
from diagrams.aws.network import ELB
from diagrams.aws.database import RDS

with Diagram("Web Service", show=False):
    ELB("lb") >> EC2("web") >> RDS("userdb")
```

## schemdraw
https://stackoverflow.com/questions/71906464/how-to-add-annotations-anywhere-in-flowchart-schemdraw
```py
import schemdraw
from schemdraw.flow import *

with schemdraw.Drawing() as d:
    d += Start.lable('start')
    d += Data(w=3,h=2).lable('input')
    d += Process(w=5).lable('process')
    d += Decision(w=5).lable('decision')
    d += Arrow(w=5).right.lable('test')
```
