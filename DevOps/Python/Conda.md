# Conda

## cache whl and conda packages
cache the packages so will not extract from remote

## cache conda env in CI 
https://stackoverflow.com/questions/69542082/dependency-caching-in-python-ci-pipeline-in-azure-devops

The installation of new package duiring a CI build will take a long time. We can cache the env and reuse it to reduce the build time.
