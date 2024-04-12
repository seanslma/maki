# Session

https://docs.sqlalchemy.org/en/13/orm/session_basics.html#when-do-i-construct-a-session-when-do-i-commit-it-and-when-do-i-close-it

## create session
we can control when the session should be terminated and the number of sessions.
```py
import sqlalchemy as sa
from sqlalchemy.orm import sessionmaker
from fastapi import Depends

# create engine
url = sa.engine.url.URL.create(**cfg)
engine = sa.create_engine(url, **kwargs)
# note that default pool_recycle=-1 so by default max of 15 connections will be there indefinitely
# engine = sa.create_engine(host, max_overflow=0, pool_recycle=3600)

# create session
LocalSession = sessionmaker(bind=engine)
def get_session():
    session = LocalSession()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
        
@router.post('/get', response_model=Union[MyClass, None])
def get_task(session: Session = Depends(get_session)) -> Optional[MyClass]:
    return api.get_task(session)
```  

## separate session from method and class
```py
from contextlib import contextmanager

@contextmanager
def session_scope():
    session = Session()
    try:
        yield session
        session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()

def run_my_program():
    with session_scope() as session:
        my_func(session)
        my_class().query(session)
```

## terminate idle sessions
Can get errors like 
```
pyodbc.OperationalError: ('HYT00',
'[HYT00] [Microsoft][ODBC Driver 17 for SQL Server]Login timeout expired (0) (SQLDriverConnect)')

pyodbc.OperationalError: ('08S01',
'[08S01] [Microsoft][ODBC Driver 17 for SQL Server]TCP Provider: Error code 0x68 (104) (SQLEndTran)')
```
We must manage connection being terminated.

Setting a rule in your database connection string to terminate idle connections after 1 hour can have both **benefits and drawbacks**. 

**Benefits:**
- **Improved resource utilization:** Terminating idle connections frees up resources (memory, CPU) on the database server, potentially improving performance for active users.
- **Reduced costs:** In cloud environments where you pay per connection, reducing idle connections can lower costs.
- **Enhanced security:** Limiting connection lifetime can mitigate risks associated with long-lived, abandoned connections.

**Drawbacks:**
- **Increased connection churn:** Frequent connection creation and termination can put additional load on the database server, potentially impacting performance.
- **Potential application disruptions:** If applications don't handle connection drops gracefully, users might experience interruptions.
- **Configuration complexity:** Managing different idle connection timeouts for various scenarios can become cumbersome.

**When to set a 1-hour idle connection timeout:**
- **You have a high volume of short-lived database interactions.**
- **Resource utilization on the server is a concern.**
- **Cost optimization is a priority.**
- **Your applications can handle connection drops effectively.**

**When to avoid setting a 1-hour timeout:**
- **You have long-running database operations or transactions.**
- **Application performance is critical, and connection disruptions cannot be tolerated.**
- **Managing connection timeouts and handling drops adds unnecessary complexity.**

**Alternatives to consider:**
- **Connection pooling:** This optimizes connection management by reusing existing connections instead of creating new ones each time.
- **Longer idle timeouts:** Consider setting a timeout that aligns with your typical application usage patterns to balance resource utilization and user experience.
- **Dynamic timeouts:** Implement connection timeouts based on specific contexts (e.g., user type, query type) for more granular control.

## `query` parameter in `sa.engine.url.URL.create`
The `query` parameter in `sa.engine.url.URL.create` is a `dictionary` used to specify 
connection options specific to the database dialect and underlying driver (DBAPI) being used. 
It allows you to pass additional configuration beyond the core connection details like username, password, host, etc.

**Important points to remember:**
- Not all database dialects or drivers support the `query` parameter
- The specific options you can use within the `query` dictionary depend entirely on the chosen dialect and driver
- PostgreSQ does not support `query`, but has the `connect_args`

Here are some resources to help you further:
- SQLAlchemy Engine Configuration: [https://docs.sqlalchemy.org/20/core/engines.html](https://docs.sqlalchemy.org/20/core/engines.html)
- Discussion on `query` parameter keys for PostgreSQL: [https://stackoverflow.com/questions/61555363/how-to-connect-to-postgresql-using-sqlalchemy](https://stackoverflow.com/questions/61555363/how-to-connect-to-postgresql-using-sqlalchemy)
