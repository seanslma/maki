# Date range

## split date range to intervals
df1 has columns `datetime` and `value` and df2 has `start_date`, `end_date` and `value2`.
The best way to add value2 to value based on the datetime
```py
import pandas as pd

# Create sample dataframes
df1 = pd.DataFrame({
    'datetime': ['2023-01-01 00:00:00', '2023-01-01 01:00:00', '2023-01-01 02:00:00'],
    'value': [10, 20, 30]
})

df2 = pd.DataFrame({
    'start_date': ['2023-01-01 00:00:00', '2023-01-01 01:00:00'],
    'end_date': ['2023-01-01 01:00:00', '2023-01-01 02:00:00'],
    'value2': [1, 2]
})

# Convert datetime columns to datetime type
df1['datetime'] = pd.to_datetime(df1['datetime'])
df2['start_date'] = pd.to_datetime(df2['start_date'])
df2['end_date'] = pd.to_datetime(df2['end_date'])

# Add a unique key to the df2 dataframe
df2['key'] = range(len(df2))

# Merge dataframes based on datetime range
merged_df = pd.merge(df1, df2, how='left', left_on=[(df1['datetime'] >= df2['start_date']) & (df1['datetime'] <= df2['end_date'])], right_on=['key'])

# Calculate new value column by adding value and value2
merged_df['new_value'] = merged_df['value'] + merged_df['value2'].fillna(0)

# Drop unnecessary columns
merged_df = merged_df.drop(['start_date', 'end_date', 'value2', 'key'], axis=1)

print(merged_df)
```

## split date range to intervals first?
In general, expanding the date range into timestamp intervals first and then doing a merge
- might be faster if you have a large dataset,
- since it reduces the number of comparisons that need to be made during the merge.
- However, this approach can also significantly increase the size of your dataframe and consume a lot of memory,
- so it might not be the best approach for all use cases

In contrast, the conditional join approach is
- more memory-efficient and
- can be faster if you have a relatively small dataset or
- if the number of overlapping date ranges is small.
- However, if the number of overlapping date ranges is large,
- then the conditional join approach might become slower compared to expanding the date range into timestamp intervals first.

In general, it's a good idea to test both approaches on your specific data and use case to determine which one is faster and more efficient for your needs.
