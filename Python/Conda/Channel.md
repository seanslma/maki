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
```sh
conda search -c <channel_name>
```
