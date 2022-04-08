# setting

## make bash shell safe
avoid pipeline errors passing silently
```
set -eoux pipefail
```
https://sipb.mit.edu/doc/safe-shell/#:~:text=set%20%2Do%20pipefail%20causes%20a,command%20in%20a%20pipeline%20errors.

https://gist.github.com/vncsna/64825d5609c146e80de8b1fd623011ca

- e: if a command fails, set `-e` will make the whole script exit, instead of just resuming on the next line.
- o: set `-o pipefail` causes a pipeline to produce a failure return code if any command errors. Normally, pipelines only return a failure if the last command errors.
- u: treat unset variables as an error, and immediately exit.
- x: enable a mode of the shell where all executed commands are printed to the terminal.
