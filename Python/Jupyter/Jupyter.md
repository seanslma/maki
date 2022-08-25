# Jupyter

## install
  python -m pip install jupyter
  
## start jupyter notebook
  python -m notebook \
  python -m notebook example.ipynb

## change cell width  
  from IPython.core.display import display, HTML \
  display(HTML("<style>.container { width:100% !important; }</style>"))  
  
## get the Docstring and method list pop-ups in Jupyter Notebook
Use Tab with your cursor directly after a defined variable to see the list of methods. For example, given: my_list = [1,2,3] you could then run that cell to define my_list as a variable, afterwards you could just type: my_list. (notice the dot) and then press **Tab** to see the **list of methods**. For the **doctrings** of functions, use **Shift+Tab** with your cursor right after the function.

## cell to markdown
  Esc + m
  
## markdown to cell
  Esc + y
  
## source control
use `jupytext` to synchronize `.py` and `.ipynb` files.
```
conda install jupytext                               #install
jupytext --set-formats ipynb,py <file>.ipynb         #create ipynb file
jupytext --set-formats ipynb,py <file>.ipynb --sync  #sync ipynb to .py file

jupytext --to notebook <file>.py  #from .py to .ipynb file
jupytext --to py <file>.ipynb     #from .ipynb to .py file
jupytext --to python --output <file>.py <file>.ipynb 
```
  
## enable extension
  pip install jupyter_nbextensions_configurator
  jupyter nbextensions_configurator enable --user #not work
  set cfigpath=C:\Users\sma\AppData\Roaming\Python\Python38\site-packages\jupyter_nbextensions_configurator\
  python %cfigpath%application.py enable --user #works
  pip install jupyter_contrib_nbextensions
  jupyter contrib nbextension install --user #not work
  set contrpath=C:\Users\sma\AppData\Roaming\Python\Python38\site-packages\jupyter_contrib_core\
  python %contrpath%application.py nbextension install --user #works
  
  http://localhost:8889/nbextensions
  
## lux
    jupyter nbextension install --py luxwidget
    jupyter nbextension enable --py luxwidget
  
