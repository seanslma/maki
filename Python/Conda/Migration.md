# Migration

How to migrate conda env.

## Export packages
```sh
conda activate myenv

# 1. Export conda packages
conda env export --from-history > conda_environment.yml

# 2. Export pip packages
# pip freeze > pip_requirements.txt
uv pip freeze > uvpip_requirements.txt
# in notepadd++ replace ` @ .*$` with empty

# 3. Get the packages only in conda
# If they can't be manged by uv, keep them in conda
```

## Import packages
```sh
# 1. Create env from conda package list
conda env create -f conda_environment.yml

# 1. Or create then install
conda create -n myenv python=3.14 uv
conda activate myenv

# 1b.Install conda packages (System Libraries only)
# non-Python system dependencies (like CUDA, Graphviz, or specific geospatial binaries)
conda env update -f conda_environment.yml

# 2. Install pip packages using uv
# pip install -r pip_requirements.txt
uv pip install -r uvpip_requirements.txt
```

conda_environment.yml
```yaml
name: new_env_name
channels:
  - conda-forge
dependencies:
  - python=3.14
  - uv
  - other conda packages
```

uvpip_requirements.txt
```
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
pandas
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
