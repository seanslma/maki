# Jupyterlab

## install jupyterlab
```sh
pip install mlflow      #manage ml life cycle
mlflow ui               #start mlflow
pip install azureml-sdk #azure ml sdk
pip install jupyterlab  #install
jupyter lab             #start server
```

## fix issues
```sh
jupyter lab clean
jupyter lab update
jupyter lab build
```

## extension
```sh
jupyter labextension install @jupyterlab/codemirror
jupyter labextension update @krassowski/jupyterlab_go_to_definition
```

## jupyter install a kernel
```sh
conda install ipykernel
python -m ipykernel install --user --name <env-name> --display-name "<kernel-name>"
```
