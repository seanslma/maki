# MLflow

Install the MLflow SDK `mlflow` package and the Azure Machine Learning `azureml-mlflow` plugin for MLflow:
```sh
pip install mlflow azureml-mlflow
```

## Models
### Log a file artifact
```py
filename = 'model.pkl'
with open(filename, 'wb') as f:
  pickle.dump(model, f)

mlflow.log_artifact(filename)
```

### Log a model
```py
mlflow.sklearn.log_model(sklearn_estimator, 'classifier')
```

## Track experiments and models
https://learn.microsoft.com/en-gb/azure/machine-learning/how-to-use-mlflow-cli-runs?view=azureml-api-2&WT.mc_id=devopslab-c9-cxa&tabs=jobs%2Ccli

### Config the experiment
```py
mlflow.set_experiment(experiment_name='hello-world')
```

### Config the run
```py
mlflow.start_run()
mlflow.log_params({
    'start_date': args.start_date,
})
...
mlflow.log_artifact(my_filepath, artifact_path='my_filepath')
mlflow.log_dict(my_report, 'my_report.json')
mlflow.log_metric('mape', mape)
mlflow.log_param('best_model_params', str(params['best']))
mlflow.end_run()

# or using context manager
with mlflow.start_run(run_name='hello-world') as run:
    ...
```

### Enable autologging for metrics, parameters, and files
```py
mlflow.autolog()
# training code
...
```

### View metrics and artifacts
- Jobs page, select the experiment name
- Experiment details page, select the Metrics tab
- Select logged metrics to render charts
- Save the chart for future use and share it with teammates by using a direct link

Query metrics, parameters, and artifacts programmatically
```py
run = mlflow.get_run('<run_id>')

metrics = run.data.metrics # last value of a given metric
params = run.data.params
tags = run.data.tags

# all values of a given metric
mlflow.get_metric_history()

# download artifacts
mlflow.artifacts.download_artifacts(run_id='<run_id>', artifact_path='helloworld.txt')
```
