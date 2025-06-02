# Python

## python package `maturin`
`mamba install maturin`.
build and package python packages that contain rust code using pyo3

## rust package `pyo3`
a library with built-in types helps pass object from python to rust and the other way around.
```toml
[dependencies]
pyo3 = { version = "0.21.2", features = ["extension-module"] } # Use the latest stable pyo3 version
```

## create a lib project
```sh
cargo new --lib my_rust_module # new folder
cargo init --lib               # run inside existing folder
```

## build extension
Use `maturin` to build the Python extension module

`maturin develop`:
- compile Rust code and place the generated `.so` (Linux/macOS) or `.pyd` (Windows) file in a location where Python can find it
- also install a simple `*.pth` file that points to the build directory, making it easy to test during development

`maturin build --release`:
- Use `--release` for optimized builds
- Compile Rust code in `release` mode (optimized for performance)
- Package the compiled shared library and other python files into a .whl file
- The .whl file will be placed in a target/wheels directory

`maturin publish --release`:
- Run `maturin build --release`
- Upload the generated source distribution (.tar.gz) and wheel (.whl) files to PyPI
