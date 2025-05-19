# Install

## Windows
- Build Tools for Visual Studio 2022:
  - requires a valid Visual Studio license, unless building open-source dependencies for your project
  - https://visualstudio.microsoft.com/downloads
  - Desktop development with C++
- Rust: https://rustup.rs

## Linux
- `rustup`: `curl --proto '=https' --tlsv1.2 https://sh.rustup.rs -sSf | sh`
- `linker` (C compiler includes a linker): GCC or Clang. For Ubuntu, install `build-essential` package

## Update
```sh
rustc --version
rustup update         # update
rustup self uninstall # uninstall
```

## Install `rust-analyzer` extension in vs code
https://code.visualstudio.com/docs/languages/rust

## Install debugging support
- Windows `Microsoft C++` (ms-vscode.cpptools): https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools
- Linux/MacOS `CodeLLDB` (vadimcn.vscode-lldb): https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb
