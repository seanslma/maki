# sort

```vb
Range("A1:E5").Sort Key1:=Range("A1"), Order1:=xlAscending, _
                    Key2:=Range("B1"), Order2:=xlAscending, _
                    Header:=xlGuess, OrderCustom:=1, MatchCase:=False, _
                    Orientation:=xlTopToBottom
                    
Header:=xlYes                   
```        