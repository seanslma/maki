# DAX TREATAS

https://docs.microsoft.com/en-us/dax/treatas-function

`TREATAS(table expression, column[, other optional columns])`

Applies the result of a table expression as filters to columns from an unrelated table.

## detailed explanation
https://www.sqlbi.com/articles/understanding-data-lineage-in-dax/

## special case
https://community.powerbi.com/t5/Desktop/Unexpected-return-from-TREATAS-function/m-p/2068473#M771436

It gets the mapped column values in the expression and then get the `rows` with mapped column values (only the ones inboth). After that, it check other selected columns in the selected rows.

In this case, it first selects the rows with managers `John and Sam` in Sales, and then for each rows check the columns `Date` and `ID` - do the calculation if there is a match.  

## Use case (join two fact tables)
### Problem
```
Dim tables:
Dm1: Year
Dm2: Company

Fact tables:
Tb1: Year, Company, TaxRate
Tb2: Year, Company, Department, Profit

Dm1/2 linked to both Tb1/2 with 1-n relationships
But there are no direct relationships between Tb1/2.

View Table:
Tbv: Year, Company, Department, Profit, TaxRate, Tax
```

### Solution
The `TaxRate` and `Tax` must be calculated using measure. And we have to use `TREATAS` to link Tb1 to Tb2.
```
VAR __tax_rate = CALCULATE(
    AVERAGE(Tb1[TaxRate]),
    TREATAS(VALUES(Tb2[Year]), Tb1[Year]),
    TREATAS(VALUES(Tb2[Company]), Tb1[Company])
)
VAR __tax = __tax_rate * SUM(Tb2[Profit])
```

## treatas with multiple table columns
```
VAR __val = Calculate(
    AVERAGE(CertificateFees[CertificateFee]),
    TREATAS(
        SUMMARIZE(Transactions, Transactions[CertificateType], Transactions[TransactionType], Transactions[SaleId]),
        CertificateFees[CertificateType],
        CertificateFees[TransactionType],
        CertificateFees[SaleId]
    )
)
```
