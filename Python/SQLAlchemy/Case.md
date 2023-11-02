# Case

## get min_date based on value of another col
The min_date should be date1 if terminated = 0 otherwise min_date = min(date1, date2). To implement this in the code, you can use the following code:

```py
import sqlalchemy as sa
from sqlalchemy import sql

# Create a SQLAlchemy engine
engine = sa.create_engine('mssql+pyodbc://username:password@servername/database')

# Get the metadata for the database
metadata = sa.MetaData()

# Get the table object for the table containing the date1, date2, and terminated columns
table = sa.Table('table_name', metadata, autoload=True, engine=engine)

# Create a CASE statement to determine the min_date based on the terminated value
min_date_case_statement = sql.case([
    (table.c.terminated == 0, table.c.date1),
    (table.c.terminated == 1, sql.func.min(table.c.date1, table.c.date2))
])

# Create a select statement to get all rows where the min_date is less than or equal to input_max
select_stmt = sa.select(table).where(min_date_case_statement <= input_max)

# Execute the select statement and get the results
results = engine.execute(select_stmt)

# Print the results
for row in results:
    print(row)
```

This code will print the results of the select statement to the console. You can modify the code to store the results in a variable or to use them in other ways.
```
