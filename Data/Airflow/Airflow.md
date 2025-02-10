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

## Prefect vs Temporal
https://linen.prefect.io/t/22927872/ulva73b9p-how-does-prefect-compare-to-temporal

**Orchestration vs. Workflow Platform:**
- Prefect focuses primarily on data workflow orchestration. It's designed to run and monitor data pipelines, with a strong emphasis on ease of use and deployment, especially for complex DAGs (Direct Acyclic Graphs).
- Temporal is a more general-purpose workflow as a code platform. It's designed for a wide variety of use cases, not just data workflows, and provides robust features for state management, retries, and long-running processes.

**State Management:**
- Prefect: Uses state management abstractions that allow for easy retries and failure handling within data workflows.
- Temporal: Provides a more robust system for state management across complex workflows, supporting long-running activities and reliable execution across failures.

**Ecosystem and Integrations:**
- Prefect has built-in integrations with popular data engineering tools and platforms, such as Dask, DBT, and various cloud services.
- Temporal has broader integrations suitable for various applications, extending beyond data engineering.

**Ease of Use:**
- Prefect is often praised for its user-friendly API, making it easier to define and orchestrate complex workflows using Python.
- Temporal requires more investment in learning its model, but it offers strong guarantees and flexibility once mastered.
