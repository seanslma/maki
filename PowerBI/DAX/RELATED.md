# RELATED
https://learn.microsoft.com/en-us/dax/related-function-dax

RELATED(Tbl[Col]) must be in the head (from) side of the relatioship.

The RELATED function is used to retrieve values from a related table in a data model. 
It allows you to navigate from one table to another based on a defined relationship between them.

The RELATED function takes a column reference as an argument and returns the value of that column from the related table. 
It is typically used within calculated columns or measures to perform calculations or filter data based on related tables.

Here's an example to illustrate the usage of the RELATED function:
- Consider two tables: "Orders" and "Customers".
- The "Orders" table has a foreign key column "CustomerID" that relates to the "CustomerID" column in the "Customers" table.

Suppose you want to calculate the total sales made by each customer in the "Customers" table. 
You can create a calculated column in the "Customers" table using the RELATED function to retrieve the corresponding sales values from the "Orders" table:
```dax
TotalSales =
    CALCULATE (
        SUM ( Orders[Sales] ),
        RELATED ( Orders[CustomerID] )
    )
```
In this example, the RELATED function is used to retrieve the "CustomerID" from the "Orders" table related to each row in the "Customers" table. 
The CALCULATE function is then used to sum the "Sales" values from the "Orders" table for the related customer. 
The result is stored in the "TotalSales" calculated column in the "Customers" table.

The RELATED function is a powerful tool for performing calculations across related tables and leveraging the data model's defined relationships in Power BI.
