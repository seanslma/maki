# Pandas

## example
```py
ax = df.plot(
  x='date',
  y=['forecast_revenue','actual_revenue'],
  title=f'Cal Year: 2022', figsize=(12,5),
)
_ = ax.set_ylabel("Revenued ($)")
```
