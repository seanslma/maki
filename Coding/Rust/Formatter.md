# Formatter

## `rustfmt`
```
rustup component add rustfmt #install
cargo fmt             #format all files from root folder
cargo fmt --check     #check only
cargo fmt src/main.rs #format a file
cargo fmt src/util/   #format files in a folder
```

## rustfmt.toml
configuration
```toml
# Use a maximum line width of 100 characters (default is 100)
max_width = 100

# Use 4 spaces for indentation (default is 4)
indent_style = "Spaces"
tab_spaces = 4

# Put each struct field on a separate line if the struct has more than one field
struct_field_align_threshold = 1

# Always put trailing commas in multiline expressions
trailing_comma = "Always"

# Use single line where possible
use_small_heuristics = "Max"
```

## vscode integration
