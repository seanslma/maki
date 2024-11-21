# Package

## papermill
Papermill is a tool for parameterizing and executing Jupyter Notebooks.
```py
import papermill as pm

pm.execute_notebook(
   'path/to/input.ipynb',
   'path/to/output.ipynb',
   parameters=dict(alpha=0.6, ratio=0.1)
)
```
