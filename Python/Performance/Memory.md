# Memory

## BytesIO
https://pythonspeed.com/articles/bytesio-reduce-memory-usage/
- `read()` returns a bytes object. Allocates memory.
- `getbuffer()` returns a memoryview
- `getvalue()` returns the contents of the BytesIO as a bytes object. No copy.
