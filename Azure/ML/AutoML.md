# Automated ML

## models 
AutoML's forecasting regression models assume that all features provided by the user are `known into the future`, at least up to the forecast horizon.

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
  
## experiment
```py
import time
from azureml.core import Workspace, Experiment

automl_settings = {
    "name": f'auto_feature_engineering_{time.time()}',
    "task": "regression",
    "iterations": 10,
    "iteration_timeout_minutes": 10,    
    "max_cores_per_iteration": 1,
    "max_concurrent_iterations": 10,
    "primary_metric": 'r2_score',    
    "experiment_exit_score": 0.985,
    "debug_log": f'automl_errors{time.time()}.log',
    "verbosity": logging.ERROR,
}
# Local compute
automl_config = AutoMLConfig(
   preprocess=False,
   X=X_train,
   y=y_train,
   X_valid=X_valid,
   y_valid=y_valid,
   path=project_folder,
   **automl_settings,
)

# Training the model
experiment = Experiment(ws, experiment_name)
local_run = experiment.submit(automl_config, show_output=True)
```
