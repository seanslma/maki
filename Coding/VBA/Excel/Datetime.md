# Datetime

## avoid comparing general string date with custom date
```
A1: "2023-01-01" format: General
A2: "2023-07-01" format: Custom "mmm-yy"
=A1>A2 will return True
```
Solution: Change "General" string date to "Date" format
