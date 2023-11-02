# DashTable

https://dash.plotly.com/datatable

## example
```py
import dash
import dash_table

app = dash.Dash(__name__)

# Create a DataTable component
table = dash_table.DataTable(
    id='table',
    columns=[{'name': 'Name', 'id': 'name'}, {'name': 'Age', 'id': 'age'}, {'name': 'Occupation', 'id': 'occupation'}],
    data=[{'name': 'John Doe', 'age': 30, 'occupation': 'Software Engineer'}, {'name': 'Jane Doe', 'age': 25, 'occupation': 'Doctor'}, {'name': 'Peter Parker', 'age': 20, 'occupation': 'Student'}]
)

# Add the DataTable component to the app layout
app.layout = table

if __name__ == '__main__':
    app.run(debug=True)
```

## export to csv
https://stackoverflow.com/questions/61203436/export-plotly-dash-datatable-output-to-a-csv-by-clicking-download-link
