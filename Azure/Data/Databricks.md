# Databricks

Databricks is pretty much `managed Apache Spark`.

Azure Databricks provides data science, engineering, and analytical teams with a single platform for big data processing and machine learning.

Azure Databricks is optimized for three specific types of data workload and associated user personas:
- Data Science and Engineering
- Machine Learning
- SQL (premium tier only)

## Spark
Apache Spark clusters are groups of computers that are treated as a single computer and handle the execution of commands issued from notebooks.
- Work
- Jobs
- Stages
- Tasks

The Databricks appliance is deployed into Azure as a managed resource group within your subscription. This resource group contains
- the driver and worker VMs for your clusters, along with
- other required resources, including
  - a virtual network,
  - a security group, and
  - a storage account.

Internally, AKS is used to run the Azure Databricks control-plane and data-planes via containers.