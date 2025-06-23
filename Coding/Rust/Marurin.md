# Maturin

## create a project
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
