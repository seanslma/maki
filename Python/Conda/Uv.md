# uv

Use `conda` to manage conda only packages and `uv` for pip packages.

## Install conda packages
```sh
conda env create -f conda_environment.yaml
```
conda_environment.yaml
```yaml
name: p12
channels:
  - https://conda.anaconda.org/conda-forge
  - https://repo.anaconda.com/pkgs/msys2
  - conda-forge
dependencies:
  - python=3.12
  - uv
  - python-graphviz
  - sqlite
  - turbodbc  
  - cx_oracle
  - m2-coreutils  # ls command
  - terraform
  - terragrunt
  - kubernetes-client 
  - kubelogin 
  - kubectl-krew
prefix: c:/users/usr/conda-envs/p12
```

## Install pip packages under conda env
```sh
uv pip install -r uv_pip_requirements.txt
```

uv_pip_requirements.txt
```txt
adlfs
aiocache
aiohttp
arrow
azure-identity
azure-keyvault-secrets
azure-storage-blob
bayesian-optimization
beautifulsoup4
bokeh
catboost
cherrypy
click
dash
dash-bootstrap-components
dash-extensions
dash-leaflet
dask
dask-jobqueue
deltalake
distributed
duckdb
exchangelib
factory-boy
fastapi
flask
fsspec
furl
geojson
holidays
httpx
hypercorn
ipykernel
jinja2
joblib
jupyterhub
jupyterlab
jupyterlab-pygments
jupyterlab-server
jupytext
kaleido
lightgbm
lxml
matplotlib
memory-profiler
mergedeep
mkdocs
mkdocs-material
mkdocs-material-extensions
mkdocstrings
mkdocstrings-python
numba
numpy
openai
optuna
oracledb
orjson
pandas<3.0
plotly
polars
prophet
pyarrow
pydantic
pydantic-settings
pyodbc
pyomo
pyspark
pytest
python-calamine
pytz
redis
requests
ruff
scikit-learn
scipy
seaborn
seqlog
setuptools
sqlalchemy
sqlalchemy-utils
statsmodels
tenacity
tensorflow
turbodbc
uvicorn
xarray
xgboost
xlsxwriter
zstandard
```

## uv publish to ado artifacts
https://docs.astral.sh/uv/guides/integration/azure/

pyproject.toml
```toml
[[tool.uv.index]]
name = "<my_feed>"
url = "https://pkgs.dev.azure.com/<ORGANIZATION>/<PROJECT>/_packaging/<FEED>/pypi/simple/"
```

setup:
- https://blog.nathanv.me/posts/azure-artifacts-uv/
- https://www.linkedin.com/pulse/part-3-microsoft-fabric-azure-devops-ci-projects-harsha-guggilla-bb2nc

