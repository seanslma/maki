#  Azure Repos

## git clone
Error
```
fatal: Cannot determine the organization name for this 'dev.azure.com' remote URL.
Ensure the `credential.useHttpPath` configuration value is set, or
set the organization name as the user in the remote URL '{org}@dev.azure.com'.
```

Solution: 
setting can be specific to Azure Repos
```sh
git config --global credential.https://dev.azure.com.useHttpPath true
```
