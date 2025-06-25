# Maturin

## create a project
Create a folder and add layout files:
```sh
maturin new ./proj --bindings pyo3
cd proj
maturin develop
```

From an existing folder/project and add layout files:
```sh
mkdir my-proj && cd "$_"
pip install maturin
maturin init --bindings pyo3
maturin develop
```

## build options
https://www.maturin.rs/metadata.html#add-maturin-build-options

### dynamic version
To use the Rust crate version from `Cargo.toml` as the Python package version:
```
[project]
name = "my-project"
dynamic = ["version"]
```

## Mixed rust/python projects
https://github.com/PyO3/maturin
