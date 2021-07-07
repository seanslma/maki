# datetime

date = DateSerial(year, month, day)

DateAdd("m", 12, FirstDate)

## str2dt
```vb
'string to datetime
dt = DateValue("2019-12-19") + TimeValue("12:47:34")
```

## dt2str
```vb
'date to string Format does not work
'wrong with rounding error: 30/06/2016 12:00:00 AM
Application.Text(DateSerial(2016,7,1) - 1e-7,"d/MM/yyyy h:mm:ss AM/PM")
'depend on local settings: 1-07-2016 12:00:00 AM
Format(DateSerial(2016,7,1) - 1e-7,"d/MM/yyyy h:mm:ss AM/PM")
```