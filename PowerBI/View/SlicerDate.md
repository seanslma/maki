# Date slicer

## include all dates in a date range slicer
Measure can affect slicers, but can only be used in visual level filter.

https://medium.com/microsoft-power-bi/automatically-adjust-power-bi-date-range-slicer-to-show-current-data-1b21e4cc6cc2
- create a measure: `is_max_date = IF(MAX(DimDate[Date]) <= TODAY(),1,0)`
- add the measure to the visual filter
