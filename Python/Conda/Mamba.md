# Mamba

Compared to conda, mamba is faster but larger.

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
mamba install scipy black numpy pandas
```

## update package
```
mamba update pandas
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
