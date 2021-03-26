# VBA Notes

## Get array dimension

## Get Range
```vb
Function Rng(ws as Sheet, r0 as long, c0 as long, r1 as long, c1 as long)
  return ws.Range(Cells(r0,c0),Cells(r1,c1))
End Function
```

## Read CSV file
