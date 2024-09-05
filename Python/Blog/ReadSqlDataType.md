# The Pandas Function `pd.read_sql` Returns An Empty DataFrame Without Correct Data Types
We provide a solution to the issue you might need

When querying data from databases such as MS SQL Server via the Driver `pyodbc`, we can conveniently get the data as a pandas DataFrame by using `pd.read_sql`. Generally, the driver provides information about the column names, data types, and other metadata associated with the result set. However, when the query result set is empty, the data type information is not available and pandas returns an `empty` DataFrame with all column types as `object`.

An empty DataFrame with wrong data types can cause issues in your Python code. If you do not check whether the returned DataFrame is empty or not your code will crash in many cases such as trying to extract the year from a datetime column and doing aggregations on float columns. Here we explain how to get the data type information in this situation when using `sqlalchemy` to create the query.

## Get the data types from the query statement
There are multiple approaches to get the data types but they are not always available in most situations.

### Option 1: `result.cursor.description`
The first approach is using the `.description` attribute of the database `cursor` object:
```python
import sqlalchemy

conn_string = f'mssql+pyodbc://{username}:{pwd}@{server_name}'
conn_string += f'/{database_name}?driver=ODBC+Driver+17+for+SQL+Server'
engine = sqlalchemy.create_engine(conn_string)
connection = engine.connect()

query = 'SELECT ID, Name, Price, StartDate FROM sales.Product;'
result = connection.execute(query)
print(result.cursor.description)
```

The output will be something like:
```
(
    ('ID', <class 'int'>, None, 10, 10, 0, False),
    ('Name', <class 'str'>, None, 50, 50, 0, False),
    ('Price', <class 'decimal.Decimal'>, None, 19, 19, 4, False),
    ('StartDate', <class 'datetime.datetime'>, None, 23, 23, 3, False),
)
```

### Option 2: `query.statement.selected_columns`
If the first approach does not work and you use `sqlalchemy` to create the query, you should still be able to get the data types.

Assume we defined the `sales.Product` Table as:
```py
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine, Column, DateTime, DECIMAL, Integer, Unicode

# Base classes and will hold the metadata about the tables
Base = declarative_base()

# A declarative class for Table `sales.Product` by inheriting from the Base class
class Product(Base):
    __tablename__ = 'Product'
    __table_args__ = {'schema': 'sales'}

    ID = Column(Integer, primary_key=True)
    Name = Name = Column(Unicode(50), nullable=False)
    Price = Column(DECIMAL(19, 4))
    StartDate = Column(DateTime)


# Create a SQLAlchemy engine
engine = create_engine(f'{database_connection_url}')

# Create tables in the database
Base.metadata.create_all(engine)
```

And we created the query in this way:
```py
from sqlalchemy import sql, types
from sqlalchemy.orm import Session

session = Session(bind=engine)
sp = Product
query = session.query(
    sp.ID.label('id'),
    sp.Name.label('name'),
    sp.Price.label('price'),
    sp.StartDate.label('start_date'),
)
```

Finally we can get the data types from the query:
```py
if isinstance(query, sqlalchemy.orm.query.Query):
    dtype = {
        c.name: c.type.__class__.__name__
        for c in query.statement.selected_columns
    }
```

The `dtype` is a dictionary with column names as keys and data types as values:
```
dtype = {
    'id': 'Integer',
    'Name': 'Unicode',
    'price': 'DECIMAL',
    'start_date': 'DateTime',
}
```

## Pass the data type information to `pd.read_sql`
There is a parameter `dtype` in `pandas.read_sql(..., dtype=None)` that can be used to pass the data types for the query results.

Note that in the previous section the extracted data types are the types defined in `sqlalchemy`. We need to convert them to the types that can be used in `pandas`. Here we provide a mapping for most of the data types:
```py
sa_to_pd_dtype = {
    'BigInteger': 'int64',
    'BIT': 'bool',
    'Boolean': 'bool',
    'Date': 'datetime64[ns]',
    'DateTime': 'datetime64[ns]',
    'DECIMAL': 'float',
    'Enum': 'category',
    'Float': 'float',
    'Integer': 'int64',
    'Interval': 'timedelta64',
    'LargeBinary': 'str',
    'Numeric': 'float',
    'SmallInteger': 'int16',
    'String': 'str',
    'Time': 'datetime64[ns]',
    'TIMESTAMP': 'datetime64[ns]',
    'Unicode': 'str',
}
```

And we set the data types when extracting the data using `pd.read_sql`:
```py
dtype = {
    col: sa_to_pd_dtype[typ]
    for col, typ in dtype.items()
    if typ in sa_to_pd_dtype
}
df = pd.read_sql(..., dtype=dtype)
```

## Why I got `NullType` for some data columns?
Assume the previous query has been changed to:
```py
query = session.query(
    sp.ID.label('id'),
    sp.Name.label('name'),
    sp.Price.label('price'),
    sql.func.dateadd(sql.text('day'), 1, sp.StartDate).label('actual_start_date'),
)
```
In this case, the data type for the column `actual_start_date` will be `NullType` instead of `DateTime`.

By digging into the `sqlalchemy` documents we find out that this is caused by the `sql.func.dateadd`.
Basically for functions that are not known, the type defaults to the `NullType`.
There are also other functions such as `sql.func.replace` and `sql.func.year` that might lead to the `NullType`.

To fix the issue, we need to pass the data type directly to the function:
```py
sql.func.dateadd(sql.text('day'), 1, sp.StartDate, type_=types.DateTime).label('actual_start_date')
```

## Reference

- [SQLAlchemy accessing column types from query results](https://stackoverflow.com/questions/64761911/sqlalchemy-accessing-column-types-from-query-results)
- [SQLAlchemy getting column data types of query results](https://stackoverflow.com/questions/2258072/sqlalchemy-getting-column-data-types-of-query-results)
- [SQL and Generic Functions](https://docs.sqlalchemy.org/en/gerrit/3941/core/functions.html)
