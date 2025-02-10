# Event

## PostgreSQL LISTEN/NOTIFY
Use to do something based on changes in db tables
- https://stackoverflow.com/questions/24285563/waiting-for-a-row-update-or-row-insertion-with-sqlalchemy
- https://tapoueh.org/blog/2018/07/postgresql-listen-notify

need to create triggers in postgresql
```py
from sqlalchemy.pool.base import PoolProxiedConnection
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
def main(conn: PoolProxiedConnection, channels: list[str]):
    with conn.cursor() as cur:
        for channel in channels:
            cur.execute(f'LISTEN {channel};')
    while True:
      await trio.lowlevel.wait_readable(conn)
      conn.poll()
      while conn.notifies:
          notify = conn.notifies.pop(0)
          print 'Got NOTIFY:', notify.pid, notify.channel, notify.payload

engine = sqlalchemy.Engine()
conn = engine.raw_connection()
conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

try:
    trio.run(main, conn, channels)
finally:
    conn.close()
    engine.dispose()
```

## event trigger
https://www.postgresql.org/docs/current/event-triggers.html

Python code use postgresql event triggers
```py
cnx = engine.raw_connection()
await trio.lowlevel.wait_readable(cnx)
cnx.poll()
while cnx.notifies:
    notify = cnx.notifies.pop(0)
    kwargs = json.loads(notify.payload)
```

This code uses Trio asynchronous I/O library and deals with PostgreSQL database notifications:

1. `await trio.lowlevel.wait_readable(cnx)`:
   - This line is using Trio's low-level API to wait until the `cnx` (presumably a network connection) becomes readable.
     In asynchronous programming, this line of code allows the program to efficiently wait for data to be available for reading without blocking the entire thread.

2. `cnx.poll()`:
   - This line is likely associated with a PostgreSQL connection (`cnx`).
     The `poll` method is commonly used in asynchronous PostgreSQL libraries to check for any events or notifications on the connection.

3. `while cnx.notifies:`:
   - This starts a `while` loop that iterates as long as there are notifications in the `cnx.notifies` list.
     Notifications in PostgreSQL are messages sent by the database server to connected clients to signal changes or events.

4. `notify = cnx.notifies.pop(0)`:
   - Inside the loop, this line pops (removes and returns) the first notification from the list of notifications (`cnx.notifies`). 

Overall, the code is waiting for the `cnx` connection to become readable, polling for any notifications on the connection, and then processing each notification in a loop. 
It suggests an asynchronous approach to handling PostgreSQL notifications, which is common in applications where you want to be notified of changes in the database in a non-blocking manner. 

## Triggers for Event Handling
PostgreSQL provides the ability to use triggers, which can be a core component of an event-driven architecture. Triggers allow you to respond automatically to database changes (like insert, update, or delete operations) and execute functions or actions in reaction to those changes.

Types of Triggers in PostgreSQL:
- BEFORE Triggers: Fire before the actual data modification is applied. They can be used to validate data or modify the data before it's committed.
- AFTER Triggers: Fire after the data modification is applied. These are often used for logging, auditing, or triggering additional actions (like updating other tables, calling external services, etc.).
- INSTEAD OF Triggers: Overwrites the default behavior of certain actions, allowing more complex logic for data manipulation.

### Logical Replication and Change Data Capture (CDC)
### NOTIFY/LISTEN (Asynchronous Event Notification)
### Polling and Periodic Task Scheduling
