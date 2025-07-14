# Trigger

## CI/CD pipeline
```yaml
trigger:
  - master
  - refs/tags/*
pr:
  - master
```

`trigger: - master - refs/tags/*`:
- The pipeline is triggered on:
  - Changes pushed directly to the master branch (e.g. commits, merges).
  - Any new Git tag (e.g. v1.0.0, release-2025) — this is useful for releases.

`pr: - master`:
- Triggered when a pull request
  - is created or updated with the master branch as the target
  - i.e. PRs that want to merge into master

### image `vmImageName: 'ubuntu-latest'`
- Not good for production same for python version.
- Best to use a pinned version: `vmImageName: 'ubuntu-22.04'`
