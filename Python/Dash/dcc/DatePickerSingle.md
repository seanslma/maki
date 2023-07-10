# DatePickerSingle
https://dash.plotly.com/dash-core-components/datepickersingle

## example
```py
import dash
import dash_core_components as dcc
from datetime import datetime

app = dash.Dash(__name__)
app.layout = dcc.DatePickerSingle(
    id='my-single-date-picker',
    date=datetime(2023, 6, 10),             
    min_date_allowed=datetime(2023, 6, 5), 
    max_date_allowed=datetime(2023, 6, 15),
    display_format='YYYY-MM-DD',
    style={'marginRight': '7px'},
)

if __name__ == "__main__":
    app.run_server(debug=True)
```
