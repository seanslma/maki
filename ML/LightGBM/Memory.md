# Memory

## LightGBM memory factors
- https://github.com/microsoft/LightGBM/issues/562
- https://lightgbm.readthedocs.io/en/latest/FAQ.html

Adjusting these parameters can reduce memory usage:
- `histogram_pool_size`: 1024? histogram cache ~ `20bytes * num_leaves * num_features * num_bins`
- `num_leaves`: 255? When `num_leaves` decreases, the RAM required decreases exponentially
- `max_bin`:

Solution to lower RAM usage in LightGBM:
- set `histogram_pool_size` parameter to the MB you want to use
- approximately RAM used = histogram_pool_size + dataset size
- lower `num_leaves`, lower `max_depth`, or lower `max_bin`

## lightgbm reduce memory
- https://lightgbm.readthedocs.io/en/latest/Parameters-Tuning.html
- https://github.com/microsoft/LightGBM/issues/6319

lightgbm training-time memory usage:
- raw data
- dataset
- model
- other

Avoid the memory usage for the `raw data`:
- construct a Dataset directly from a file (either a CSV/TSV/LibSVM file or a LightGBM Dataset binary file).

Reduce the memory usage of the `dataset`:
- use smaller `max_bin` [default = 255] or high `min_data_in_bin`
- remove irrelevant features before construction
- In Python, construct a dataset and perform training in the same process to avoid storing a copy of the raw data by passing `free_raw_data=True`

Reduce the size of the `model`:
- use `early stopping`
- set `max_depth` [default = -1] (good values of this will depend on num_leaves).
- reduce `num_leaves`. default = 31
- reduce `n_estimators` (`num_boost_round`).
- increase `min_gain_to_split`. default = 0.0
- increase `min_data_in_leaf`. default = 20
