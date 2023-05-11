# Parquet

## read `filters`
- The `filters` keyword is a row-group-wise action
- It does not do any filtering within `partitions`
- when using 'pyarrow', the filters will apply to the partition as well
