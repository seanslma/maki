# perf

**StringBuilder** is actually a linked list of blocks, default with size from 16, 32, ....  To avoid the multiple blocks, we should set the capacity to the possibly largest value we need.
