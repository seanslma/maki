# Mamba

Compared to conda, mamba is faster but larger.

## update package
```
mamb update pandas
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
