# Package

## tlmgr
```sh
# update
tlmgr update --self
tlmgr update --all
# user mode
tlmgr install <package>

# for sudo use the full path of tlmgr `which tlmgr`
which tlmgr
sudo /path/to/tlmgr install <package>
```

## filename
a `package` to tlmgr is a unit of files that are installed together it does not necessarily relate directly to a latex `package`.

filename is not always the same as the package name.
Here is the example to find the package name for file `otf.sty`
```sh
tlmgr info otf.sty
```
