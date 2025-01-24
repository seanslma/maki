# Condarc

## config
The `channel_alias` specifies a base URL to prepend to all channel names that do not start with `http://` or `https://`. 
So, any channel name without an explicit URL will be prefixed with `https://conda.example.com/`.

Therefore, `example/uat` will be interpreted as `https://conda.example.com/example/uat`, effectively linking it to `https://conda.example.com/`.
```
auto_update_conda: false
update_dependencies: false
channel_alias: https://conda.example.com/
channel_priority: false
channels:
  - example/uat #!top
  - https://conda.anaconda.org/conda-forge #!top
  - https://repo.anaconda.com/pkgs/msys2
ssl_verify: False #/etc/ssl/certs/ca-certificates.crt
envs_dirs:
  - ~/conda-envs/
pinned_packages:
  - conda=4.9.2
  - mamba=0.33.3
```

## use `tar.bz2` instead of `.conda` format
in `.condarc` add:
```
conda-build:
  pkg_format: 'tar.bz2'
```
