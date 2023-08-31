#  Prometheus
https://prometheus.io/docs/introduction/overview/

Prometheus is a monitoring system that is designed to be scalable, flexible, and easy to use.
It can collect metrics from all parts of the Kubernetes cluster, and it provides a unified view of the health of the system.
 
## how to run
download the binary file into a folder and setup the config using yaml. 
then run `prometheus --config.file=prometheus.yml`

## metrics
- counter: can only increase or reset i.e the value cannot reduce
- gauge: a number which can either go up or down
- histogram: for calculated values which are counted based on bucket values
- summary: an alternative to histogram - cheaper, but lose more data. calculated on app level hence aggregation of metrics from multiple instances of the same process is not possible. use histogram whenever possible.
