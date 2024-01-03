# Event

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
