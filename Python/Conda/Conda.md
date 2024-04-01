# Conda

Conda and Mamba Commands for Managing Virtual Environments\
https://www.imranabdullah.com/2021-08-21/Conda-and-Mamba-Commands-for-Managing-Virtual-Environments

## conda vs pip
https://pythonspeed.com/articles/conda-vs-pip/#:~:text=The%20fundamental%20difference%20between%20pip,even%20the%20Python%20interpreter%20itself).

- conda is more powerful
- conda has more freedom to choose some tools like BLAS based on mkl
- pip wheel can lead larger package size
- pip wheel not include executables and tools

## show all conda info
```
conda info --all
```

## update conda
```
conda update -n base conda
```

## create an env
```
conda create --name <env-name>
```

## init
Only need to run conda initialization when the CONDA_SHLVL variable is 0 - there are no activated envs.

## activate
Conda puts each environment on a stack as it is activated and deactivating merely pops one item off the stack.
The depth of the conda environment stack is stored in the environment variable CONDA_SHLVL. Running conda deactivate that many times should deactivate all environments.
```
for i in $(seq ${CONDA_SHLVL}); do
    conda deactivate
done
```

## activate anaconda/miniconda/conda-forge
```
conda create -n env-py38 python=3.8 anaconda
set PATH=C:\Anaconda\envs\py33\Scripts;C:\Anaconda\envs\py33;%PATH%
conda env list
conda activate env-py38
conda env remove -n ENV_NAME #if the folder still there, kill python and delete the folder
conda clean -afy #remove cache

#clone an existing env
conda create --name ENV_NAME_new --clone ENV_NAME_from
```

## create a notebook kernel
The second command is for registering the kernel for the environment. Do we need to run the second command?
```
conda install -c anaconda ipykernel
python -m ipykernel install --user --name=test-env
```

## install package
```
conda install -c conda-forge dash-bootstrap-components
```

## from github
```
conda activate my-env
conda install git pip
pip install git+git://github.com/plotly/Kaleido@master
```
