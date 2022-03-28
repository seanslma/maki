# Conda

Conda and Mamba Commands for Managing Virtual Environments\
https://www.imranabdullah.com/2021-08-21/Conda-and-Mamba-Commands-for-Managing-Virtual-Environments

## activate anaconda/miniconda/conda-forge
```
conda create -n env-py38 python=3.8 anaconda
set PATH=C:\Anaconda\envs\py33\Scripts;C:\Anaconda\envs\py33;%PATH%
conda env list
conda activate env-py38
conda env remove -n ENV_NAME
conda clean -afy #remove cache

#clone an existing env
conda create --name ENV_NAME_new --clone ENV_NAME_from
```

## create a notebook kernel
```
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=test-env
```

## mamba
Compared to conda, mamba is faster but larger.

### clear cache
```
mamba clean --all
```

### error: SSL certificate not OK
in `.condarc`, we should delete this line
```
ssl_verify: C:\Users\usr\conda-envs\my.crt
```

## install package
```
conda install -c conda-forge dash-bootstrap-components
```

