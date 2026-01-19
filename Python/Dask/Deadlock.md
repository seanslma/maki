# Deadlock

## threads
`dask.base.compute` is not thread-safe. So using `threads` can lead to deadlock.
