# Issue

## polars integer calculation not upcasted
Polars does not automatically upcast integer types during arithmetic
```py
from datetime import datetime, timedelta
df = (
    pl.DataFrame({
        'ts': pl.datetime_range(
            start=datetime(2025,7,1,2,0,0),
            end=datetime(2025,7,1,2,20,0),
            interval='5m',
            eager=True,
         )
    })
    .with_columns(
        hour=pl.col('ts').dt.hour(),
        minute=pl.col('ts').dt.minute(),
        minutes=pl.col('ts').dt.hour() * 60 + pl.col('ts').dt.minute(),
    )
)
print(df)
# shape: (5, 4)
# ┌─────────────────────┬──────┬────────┬─────────┐
# │ ts                  ┆ hour ┆ minute ┆ minutes │
# │ ---                 ┆ ---  ┆ ---    ┆ ---     │
# │ datetime[μs]        ┆ i8   ┆ i8     ┆ i8      │
# ╞═════════════════════╪══════╪════════╪═════════╡
# │ 2025-07-01 02:00:00 ┆ 2    ┆ 0      ┆ 120     │
# │ 2025-07-01 02:05:00 ┆ 2    ┆ 5      ┆ 125     │
# │ 2025-07-01 02:10:00 ┆ 2    ┆ 10     ┆ -126    │
# │ 2025-07-01 02:15:00 ┆ 2    ┆ 15     ┆ -121    │
# │ 2025-07-01 02:20:00 ┆ 2    ┆ 20     ┆ -116    │
# └─────────────────────┴──────┴────────┴─────────┘
```
