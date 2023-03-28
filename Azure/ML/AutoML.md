# Automated ML

## rerun failed experiment
```py
from azureml.core import Workspace, Experiment

# Load the workspace and experiment objects
workspace = Workspace.from_config()
experiment = Experiment(workspace, "experiment-name')

# Get the failed runs
failed_runs = experiment.get_runs(type='Failed')

# Re-run the experiment
for failed_run in failed_runs:
    new_run = failed_run.re_run()
```

## deploy using python
https://towardsdatascience.com/how-to-deploy-scikit-learn-models-to-azure-container-instances-a0a59d0d07a1

- Setup Training Environment from terminal
  ```
  conda create -n ml-10 python=3.10
  conda activate ml-10
  #install packahes
  azureml-core==1.39
  pandas==1.3.5
  scikit-learn==0.23.2
  mlflow==1.24.0
  cloudpickle==2.0.0
  psutil==5.9.0  
  ```
- get ml ws config
  ```
  # config.json
    {
        "subscription_id": "subscription-id",
        "resource_group": "resource-group-name",
        "workspace_name": "workspace-name"
    }
  ```
