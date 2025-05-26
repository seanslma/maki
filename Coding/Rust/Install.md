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

Disable inlay hints:
```json
// Enables the inlay hints in the editor.
//  - on: Inlay hints are enabled
//  - onUnlessPressed: Inlay hints are showing by default and hide when holding Ctrl+Alt
//  - offUnlessPressed: Inlay hints are hidden by default and show when holding Ctrl+Alt
//  - off: Inlay hints are disabled
"editor.inlayHints.enabled": "on",
```

Turn off underline from mut variable name:
```json
"editor.semanticTokenColorCustomizations": {
    "enabled": true,
    "rules": {
        "*.mutable": {
            "underline": false,
        }
    }
}
```

## Install debugging support
- Windows `Microsoft C++` (ms-vscode.cpptools): https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools
- Linux/MacOS `CodeLLDB` (vadimcn.vscode-lldb): https://marketplace.visualstudio.com/items?itemName=vadimcn.vscode-lldb run in vscode (Ctrl + P): `ext install vadimcn.vscode-lldb`
