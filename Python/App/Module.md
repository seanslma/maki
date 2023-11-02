# Module

## win32com
install pywin32 for win32com:
```sh
python -m pip install pywin32
```

## Plotly and Cufflinks
cufflinks is the link between plotly and pandas.
```py
import pandas as pd
import cufflinks as cf
import plotly.offline
cf.go_offline()
cf.set_config_file(offline=False, world_readable=True)
```

## Geographical Plotting
```py
import plotly.plotly as py
import plotly.grath_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
init_notebook_mode(connected=True)

layout = dict(geo={'scope':'usa'})
choromap = go.Figure(data=[data], layout=layout)
iplot(choromap)
```
