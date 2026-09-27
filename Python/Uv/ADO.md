# ADO

## setup artifacts feed credentials
private and pypi. This is for local interactive login.
```sh
uv tool install keyring --with artifacts-keyring

set UV_KEYRING_PROVIDER=subprocess
set UV_INDEX_ADO=https://pkgs.dev.azure.com/<ORG>/<PROJ>/_packaging/<FEED>/pypi/simple/
set UV_INDEX_ADO_USERNAME=VssSessionToken
set UV_INDEX_PYPI=https://pypi.org/simple/
set UV_INDEX_STRATEGY=first-index
```

## build package
```sh
uv build
```

## publish to feed
```sh
az login # az devops login
uv publish --publish-url "https://pkgs.dev.azure.com/<ORG>/<PROJ>/_packaging/<FEED>/pypi/upload/" --username VssSessionToken
```
