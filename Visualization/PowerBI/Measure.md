# Measure

## show one of measure based on slicer
https://towardsdatascience.com/dynamic-filtering-in-power-bi-5a3e2d2c1856

- measure 1: measure1 = SUM('tbl'[amount])
- measure 2: measure2 = CALCULATE('tbl-measure'[measure1],DATESYTD(Dates[Date])), year to day
- create a slicer key-val table `tbl-keyval`: SelectedKey = MIN('tbl-keyval'[key])
- SelectedMeasure = SWITCH([SelectedKey], 1,'tbl-measure'[measure1], 2,'tbl-measure'[measure2])
