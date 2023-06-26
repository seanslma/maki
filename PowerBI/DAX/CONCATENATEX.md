# CONCATENATEX

## join string
Shops table: Id, Shop, Country, Region
Products table: ProductType, ProductQuantity, ShopId

Create a Table to show the Total ProductQuantity by Country and Region, and all the product types.
```dax
ConcatenatedProductType = CALCULATE(
    CONCATENATEX(
        VALUES(Products[ProductType]),
        Products[ProductType], ", "
    ),
    FILTER(
        Products,
        RELATED(Shops[Id]) = Products[ShopId]
    )
)
```
