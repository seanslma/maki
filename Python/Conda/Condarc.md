# Condarc

```
auto_update_conda: false
update_dependencies: false
channel_alias: https://conda.example.com/
channel_priority: false
channels:
  - example/uat #!top
  - https://conda.anaconda.org/conda-forge #!top
  - https://repo.anaconda.com/pkgs/msys2
ssl_verify: True
envs_dirs:
  - ~/conda-envs/
pinned_packages:
  - conda=4.9.2
  - mamba=0.33.3
```
