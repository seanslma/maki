# Parquet

## parquet compression options `snappy` vs `zstd`
Switching to **Zstandard (`zstd`)** is a great move for 2026, especially if you are optimizing for cloud storage costs and performance. 
It has largely replaced GZIP as the "smart" compression choice.

Here is the breakdown of how it compares to **Snappy**.

### The Trade-off: Zstd vs. Snappy

| Feature | Snappy | Zstandard (Zstd) |
| --- | --- | --- |
| **Compression Ratio** | Moderate (Larger files) | **High (30–40% smaller than Snappy)** |
| **Write Speed** | **Extremely Fast** (Low CPU) | Slower (More CPU intensive) |
| **Read Speed** | Very Fast | **Near-Snappy speeds** |
| **Best For** | Real-time streaming / Hot data | **Long-term storage / Cost reduction** |

### How to implement it in code

To use `zstd` correctly in the `serialize` method, we should also consider the **compression level** (default is usually 3).

```python
# updated options
self.options = {
    'version': '2.6',
    'compression': 'zstd',
    'compression_level': 3, # Range is 1 (fastest) to 22 (smallest)
}

# serialize data
def serialize(self, data: pa.Table) -> pa.Buffer:
    buf = pa.BufferOutputStream()
    pq.write_table(
        table=data,
        where=buf,
        **self.options
    )
    return buf.getvalue()

```

### Pro Tip: The "Level 1" Sweet Spot

If we want the file size benefits of `zstd` but are worried about slowing down our pipeline, use `compression_level: 1`. 
It is significantly faster than the default while still producing much smaller files than Snappy.
