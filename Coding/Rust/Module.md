# Module

https://www.reddit.com/r/rust/comments/y3p5hx/how_can_i_have_multi_level_module_nesting/
```
src/
    main.rs
    foo.rs
    foo/
        bar.rs
        bar/
            baz.rs
```
- `main.rs` must contain a `mod foo;` line
- `foo.rs` or `foo/mod.rs` must contain a `mod bar;` line
- `foo/bar.rs` or `foo/bar/mod.rs` must contain a `mod baz;` line

When rust encounters `mod name;`, it goes and finds `name.rs` or `name/mod.rs` and uses its contents as the module at that site.sssssssssssssssssssssssssssssssssssssssssssss
