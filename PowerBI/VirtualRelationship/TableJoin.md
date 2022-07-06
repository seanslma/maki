# Table Join

## NATURALLEFTOUTERJOIN
can be used to join two tables without any relationships. The join will use the columns with the same name. T
he join result is a temporal table but the table must be used in a DAX context (measure).

### Calculate the sumproduct of columns from two tables
```
CalculatedTaxRate =
    VAR __avg_rate = Calculate(
        AVERAGE(TblTaxRate[Rate]),
        TREATAS(
            SUMMARIZE(TblProfit, TblProfit[Year], TblProfit[Company], TblProfit[Department]),
            TblTaxRate[Year],
            TblTaxRate[Company],
            TblTaxRate[Department]
        )
    )
    VAR __tmp = NATURALLEFTOUTERJOIN( 
        TblProfit, 
        TblTaxRate
    )    
    VAR __weighted_rate = DIVIDE( 
        CALCULATE(
            SUMX(__tmp,  TblProfit[Profit] * TblTaxRate[Rate]),
            TREATAS(
                SUMMARIZE(TblProfit, TblProfit[Year], TblProfit[Company], TblProfit[Department]),
                TblTaxRate[Year],
                TblTaxRate[Company],
                TblTaxRate[Department]
            )  
        ),
        SUM( TblProfit[Profit] )
    )
    VAR __is_row = HASONEFILTER(TblProfit[ProfitType])
RETURN
    if(__is_row, __avg_rate, __weighted_rate)
```
