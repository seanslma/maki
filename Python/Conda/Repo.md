# Repo
How create a conda repo: Use `Flask` to create a basic web app with api functions.

## web api
- post: upload a conda package
- post: move a conda package
- delete: delete a conda package

## config.json
setup conda channels

## setup internal channel
https://stackoverflow.com/questions/35359147/how-can-i-host-my-own-private-conda-repository
- Create the channel: `mkdir -p /tmp/my-conda-channel/linux-64`
- Build your conda package: `conda build my-package`
- Copy the built file to the channel: `cp /path-to-conda-bld/linux-64/my-package-1.0.0-py39_0.tar.bz2 /tmp/my-conda-channel/linux-64/`
- Index the channel: `conda index /tmp/my-conda-channel/linux-64/`
- Install the package from the channel: `conda install -c file://tmp/my-conda-channel/ my-package=1.0.0`
