# Spark

Apache Spark is a framework for distributed computing.
- store intermediate data and results in memory
- provide an API to write applications
- is fully compatible with the Hadoop ecosystem

## driver
- communicate with cluster manager
- request resources (CPU, memory, etc.) from cluster manager for Spark's executors (JVMs)
- transform all Spark operations into DAG computations
- schedule and distribute computations as tasks across the Spark executors
- communicate directly with executors after resource allocation

## cluster manager
Cluster manager manages and allocates resources for cluster nodes.
- built-in standalone cluster manager
- Apache Hadoop YARN
- Apache Mesos
- Kubernetes

## executor
An executor runs on each worker node in the cluster. The executors communicate with the driver program.
