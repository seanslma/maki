# PySpark

## Job
Code with input and output to process data.

## Stage
Jobs are divided into stages.

## Task
One task per partition - each stage has some tasks.

## PySpark vs Dask
https://www.coiled.io/blog/moving-from-spark-to-dask

- spark for larger data, need to run on a cloud cluster
- dask for smaller data, faster and easier to integrate into python, can run locally
