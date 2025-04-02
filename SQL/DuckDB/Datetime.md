# Datetime

## extract date from timestamp
```sql
cast(timeending - interval '30 minutes' as date) as date_updated
```

## extract year/month etc from date/timestamp
```sql
extract(part from date) # year, month, day, hour, minute, second
extract(year from timeending - interval '30 minutes') as year
```
