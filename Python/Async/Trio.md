# trio
Trio is a Python library designed for async concurrency, 
and it provides a simpler alternative to `asyncio` for managing concurrent tasks.
- https://trio.readthedocs.io/en/stable/
- a friendly Python library for async concurrency and I/O

## simple example: Running Two Async Tasks Simultaneously
Run two async tasks simultaneously using **Trio**. 
Each task will simulate some work with a `sleep` and print a message before and after the work.

```python
import trio

async def task_1():
    print("Task 1 starting")
    await trio.sleep(2)  # Simulate some work (sleep for 2 seconds)
    print("Task 1 done")

async def task_2():
    print("Task 2 starting")
    await trio.sleep(1)  # Simulate some work (sleep for 1 second)
    print("Task 2 done")

async def main():
    # Run both tasks concurrently
    async with trio.open_nursery() as nursery:
        nursery.start_soon(task_1)
        nursery.start_soon(task_2)

# Start the Trio event loop and run the main function
trio.run(main)
```

Explanation:
- **`task_1()` and `task_2()`**: These are asynchronous functions that simulate some work by using `trio.sleep()`. The first task sleeps for 2 seconds, while the second one sleeps for 1 second.
- **`main()`**: This is the main asynchronous function where we create a nursery (a concept in Trio for managing concurrent tasks). We use `nursery.start_soon()` to start the two tasks concurrently.
- **`trio.run(main)`**: This starts the Trio event loop and runs the `main` function.

## trio.lowlevel.wait_readable
In **Trio**, `trio.lowlevel.wait_readable` is a low-level function used for **waiting for a file descriptor** 
(or any object that behaves like a file descriptor) to become readable. 
It's part of the Trio's low-level API, which provides more control over concurrency but requires a deeper understanding of async programming.

This function is primarily used when you need to wait for data to become available for reading from a stream or file descriptor, 
and it integrates with the Trio event loop to ensure that your program doesn't block while waiting.

### How it Works
`trio.lowlevel.wait_readable` allows your program to wait until a specified **file descriptor** (like a socket or a pipe) is ready to be read. 
This is useful in scenarios where you're working with custom file descriptors or streams and want to avoid blocking your async code while 
waiting for data to be available.

The general signature is:
```python
trio.lowlevel.wait_readable(fd: int, timeout: Optional[float] = None)
```

- `fd`: The file descriptor that you want to monitor for readability. It could be any object that supports the `fileno()` method (e.g., a socket, pipe, or file).
- `timeout`: (Optional) The number of seconds to wait before the operation times out. If not provided, it will block indefinitely until the file descriptor becomes readable.

### Example Usage
we'll use `trio.lowlevel.wait_readable` to wait for data to be available on a socket:

```python
import trio
import socket

async def handle_client(client_socket):
    print("Waiting for data...")
    # Wait until the client socket is readable
    await trio.lowlevel.wait_readable(client_socket)
    data = client_socket.recv(1024)
    print(f"Received data: {data.decode()}")
    client_socket.close()

async def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(5)
    print("Server listening on port 12345...")

    while True:
        client_socket, client_address = await trio.to_thread.run_sync(server_socket.accept)
        print(f"Accepted connection from {client_address}")
        # Handle each client in a separate task
        trio.spawn(handle_client, client_socket)

async def main():
    await server()

trio.run(main)
```

Explanation:
- **Server Setup**: A server socket is created that listens on port `12345`. When a client connects, the server accepts the connection and hands it off to a new task for processing.
- **`handle_client`**: This is the function that handles the client connection. It first waits until the client socket is readable using `trio.lowlevel.wait_readable`.
- **Waiting for Readability**: `await trio.lowlevel.wait_readable(client_socket)` will block until there is data available on the `client_socket` to read.
- **Receiving Data**: Once the socket is readable, it reads the incoming data with `recv(1024)` and prints it.

### When to Use `wait_readable`:
- **Custom Streams**: If you are working with custom streams or file descriptors (like sockets, pipes, or file objects) and need more control over when they are ready to be read or written.
- **Low-Level Control**: When you need low-level control over file descriptors or sockets beyond the higher-level Trio abstractions like `trio.open_nursery()` or `trio.Stream`.
- **Non-blocking I/O**: To avoid blocking the event loop while waiting for external resources (like a socket) to be ready for reading.

### Considerations:
- **`wait_readable` is low-level**: For most high-level use cases, you'll be better off using Trio's `trio.open_nursery()` with async stream abstractions (like `trio.SocketStream`), which manage readability and writability for you.
- **Timeouts**: If you want to add a timeout, you can pass the `timeout` argument (in seconds), and it will raise a `TimeoutError` if the file descriptor isn't ready within that time.

In summary, `trio.lowlevel.wait_readable` is a powerful tool for handling readiness notifications of file descriptors or streams, but it is typically used when you need low-level control or need to interact with legacy code that uses raw file descriptors.
