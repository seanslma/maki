# Airflow

## A complete Apache Airflow tutorial: building data pipelines with Python
https://theaisummer.com/apache-airflow-tutorial/

## Airflow vs. Prefect vs. Argo
- https://huyenchip.com/2021/09/13/data-science-infrastructure.html
- https://neptune.ai/blog/argo-vs-airflow-vs-prefect-differences
- https://medium.com/arthur-engineering/picking-a-kubernetes-orchestrator-airflow-argo-and-prefect-83539ecc69b

**airflow**
- data workflows are defined using Python instead of YAML
- package the entire workflow into one container
- DAGs are not parameterized - you can't pass parameters into your workflows
- DAGs are static - it can't automatically create new steps at runtime as needed

**prefect**
-  workflows are defined in Python, parameterized and dynamic
-  can run each step in a container, but has container problem

**argo worflow**
- every step in an workflow is run in its own container
- workflows are defined in YAML
  - allow you to define each step and its requirements in the same file
  - workflow definitions can become messy and hard to debug
- can only run on Kubernetes clusters
