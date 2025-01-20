# Test

## test connection query
https://stackoverflow.com/questions/3668506/efficient-sql-test-query-or-validation-query-that-will-work-across-all-or-most
```sql
select 1           # mysql, sqlserver, postgresql, sqlite 
select 1 from dual # oracle
```

## using sqlalchemy
```py
from sqlalchemy import create_engine, text

conn_str = '***'
engine = create_engine(conn_str)
with engine.connect() as conn:
    rows = conn.execute(text('select 1')).fetchall()
    for row in rows:
        print(row)
```
