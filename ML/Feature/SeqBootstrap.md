# Sequential Bootstrap

A sequential bootstrap is a variant of the bootstrap resampling method. It is used primarily in time series analysis or situations where data points are dependent (i.e., there's some temporal or sequential structure in the data).

How Does Sequential Bootstrap Work?
- Divide the data into blocks: The data is first divided into smaller, non-overlapping blocks or chunks (often called blocks of observations).
- Resample blocks: These blocks are then sampled with replacement to create new sequences of data, preserving the temporal structure.
- Reconstruct a new series: The blocks are stitched together to form a new time series, which can be used for further analysis or to estimate parameters (e.g., for model validation or hypothesis testing).

Types of Sequential Bootstrap
- Block Bootstrap (Fixed-Size Blocks)
- Moving Block Bootstrap (Overlapping Blocks)
- Circular Block Bootstrap

example
```py
import numpy as np

# Original time series data (example)
data = np.array([30, 32, 31, 29, 28, 30, 32, 33, 35, 34])

# Parameters for the block bootstrap
block_size = 3  # size of each block
n_bootstrap_samples = 5  # number of bootstrap samples

# Create a function to perform block bootstrap
def block_bootstrap(data, block_size, n_samples):
    n = len(data)
    n_blocks = n // block_size
    bootstrap_samples = []

    # Create blocks of size `block_size`
    blocks = [data[i:i + block_size] for i in range(0, n, block_size)]

    # Generate bootstrap samples by sampling blocks with replacement
    for _ in range(n_samples):
        sampled_blocks = np.random.choice(blocks, size=n_blocks, replace=True)
        bootstrap_sample = np.concatenate(sampled_blocks)
        bootstrap_samples.append(bootstrap_sample)

    return bootstrap_samples

# Perform block bootstrap
bootstrap_results = block_bootstrap(data, block_size, n_bootstrap_samples)

# Print the bootstrap samples
for i, sample in enumerate(bootstrap_results):
    print(f"Bootstrap Sample {i+1}: {sample}")
```
