# Extension

## enable extension
http://localhost:8889/nbextensions
```
pip install jupyter_nbextensions_configurator
jupyter nbextensions_configurator enable --user #not work

set cfigpath=C:\Users\sma\AppData\Roaming\Python\Python38\site-packages\jupyter_nbextensions_configurator\
python %cfigpath%application.py enable --user #works

pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user #not work

set contrpath=C:\Users\sma\AppData\Roaming\Python\Python38\site-packages\jupyter_contrib_core\
python %contrpath%application.py nbextension install --user #works
```

## extensions
- Add a Table of Content (Table of Content 2)
