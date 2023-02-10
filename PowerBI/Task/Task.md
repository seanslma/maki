# Task

## Slicer latest date
Make sure slicer always has the default latest value, such as current year, quater, day etc.

## n-n relationship
Create a bridge table so replace the n-n relationship by n-1 and 1-n relationships.

## Total
Create measures to show employee salary and bonus with department and total summary (assume each department has the same bonus rate).

Functions to determine if the measure is in employee, department or all: HASONEVALUE, HASONEFILTER

Functions to get the summary of the bonus: SUMMERIZE, SUMX

Caveat: do not use variables in place of measure. Understand the differences between variables (temp value) and measures (function)
