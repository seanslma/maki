# Mamba

Compared to conda, mamba is faster but larger.

## show available versions 
```sh
mamba search -c conda-forge pyarrow
mamba show conda-forge/pyarrow
```

## update
Note: Installing the conda or mamba package in anywhere other than base will lead to surprising behavior.
```
mamba update -n base mamba
mamba install -n base 'mamba>=1.0'
```

## list env
```
mamba env list
```

## create env
```
mamba create --name dev python=3.11
# to activate dev by default, in the end of .bashrc add
mamba activate dev
# then
source ~/.bashrc
```

## install package
```
mamba install scipy black numpy pandas -y
mamba install sqlalchemy=1.* #install latest version of 1.x
```

## update package
```
mamba update pandas -y
```

## remove package
```
mamba remove pandas
```

## clear cache
```
mamba clean --all
```

## error: SSL certificate not OK
in `.condarc`, we should delete this line
```
ssl_verify: C:\Users\usr\conda-envs\my.crt
```
