# Setup

## track component build time
use `report_timing=True` in `create()` method to track the time it takes to build each component of the model.

## tips
https://groups.google.com/g/pyomo-forum/c/YTPByhZzboA
- try to avoid innecessary loops
- try to get all your "if" comparisons out of the loops
- try to use pythonic way to iterate, instead of raw "for"s
