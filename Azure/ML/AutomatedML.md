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
