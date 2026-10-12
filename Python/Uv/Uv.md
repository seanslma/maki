# uv

`UV_INDEX_URL` has been depreciated, replace it by `UV_DEFAULT_INDEX`.

## install uv
```
curl -LsSf https://astral.sh/uv/install.sh | sh
uv --version
```

## create an env
```sh
mkdir -p ~/venvs
uv venv ~/venvs/p12 --python 3.12

echo 'source ~/venvs/p12/bin/activate' >> ~/.bashrc
echo "alias pp='uv pip'" >> ~/.bashrc
source ~/.bashrc
```

## install artifacts-keyring for interactive auth
```sh
uv tool install keyring --with artifacts-keyring
```

## config uv.toml
.config/uv/uv.toml
```toml
keyring-provider = "subprocess"

[[index]]
name = "ado"
url = "https://VssSessionToken@pkgs.dev.azure.com/<org>/<proj>/_packaging/my-pypi/pypi/simple/"

[[index]]
name = "pypi"
url = "https://pypi.org/simple/"
default = true
```

## build package
```sh
set UV_KEYRING_PROVIDER=subprocess

set UV_INDEX_ADO=https://pkgs.dev.azure.com/<org>/<proj>/_packaging/my-pypi/pypi/simple/
set UV_INDEX_ADO_USERNAME=VssSessionToken
set UV_INDEX_PYPI=https://pypi.org/simple/
set UV_INDEX_STRATEGY=first-index

az login # az devops login
uv build
```

## publish to feed
```sh
az login # az devops login

uv publish --publish-url "https://pkgs.dev.azure.com/<org>/<proj>/_packaging/my-pypi/pypi/upload/" --username VssSessionToken
```
