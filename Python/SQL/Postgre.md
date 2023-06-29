# Postgre

## example
```py
import pandas as pd
from contextlib import contextmanager

@contextmanager
def db_session():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def exe(query):
    with db_session() as session:
        session.execute(query)
        
def qry(query):
    with db_session() as session:
        result = session.execute(query)
        data = result.fetchall()
        cols = result.keys()
        df = pd.DataFrame(data, columns=cols)
    return df
    
# list schemas (namespaces) in current database
df = qry('''select nspname as schema_name from pg_namespace;''')

# list tables in "staging" schema
df = qry('''select table_name from information_schema.tables where table_schema = 'staging';''')

# select top 5 rows from "staging.sales" table
df = qry('''select * from staging.sales order by insert_timestamp desc limit 5;''')

# select sale records from "staging.sales" table based on sale_id
df = qry('''select * from staging.sales where sale_id = 123456;''')

# delete sale record
exe('''delete from staging.sales where sale_id = 123456;''')
```
