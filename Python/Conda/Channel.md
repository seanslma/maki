# Channel
https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-channels.html

## list channels
```sh
conda config --show channels
```

## delete a channel
```sh
conda config --remove channels https://anaconda.org
```

##  list packages available in channel
https://stackoverflow.com/questions/43222407/how-to-list-package-versions-available-with-conda
```sh
conda search -c conda-forge jupyterlab # will also search in the channels listed in .condarc
conda search -c conda-forge "jupyterlab>=3.5"
conda search -c conda-forge --override-channels jupyterlab # search the provided channel only
conda search -c conda-forge --override-channels --json "jupyterlab>=3.6"
```
