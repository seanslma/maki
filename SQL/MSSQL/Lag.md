# Lag

shift row value to next row or previous row

## shift to next row
```sql
WITH cte_netsales AS (
  SELECT 
    year,
    month, 
    SUM(net_sales) net_sales
  FROM 
    sales.netsales_brands
  WHERE 
    year >= 2018
  GROUP BY 
    year, month
)
SELECT 
  year,
  month,
  net_sales,
  LAG(net_sales,1) OVER (
    ORDER BY year, month
  ) pre_mth_sales
FROM 
  cte_netsales;
```

## shift to next row with partition
```sql
WITH cte_sales AS (
  SELECT 
    year,
    month,
    brand,
    net_sales,
    LAG(net_sales,1) OVER (
      PARTITION BY brand
      ORDER BY year, month
    ) pre_sales
  FROM 
    sales.netsales_brands
  WHERE
    year >= 2018
)
SELECT
  year,
  month, 
  brand,
  net_sales, 
  pre_sales,
  FORMAT((net_sales - pre_sales)  / pre_sales, 'P') vs_pre_mth
FROM
  cte_sales;
```
