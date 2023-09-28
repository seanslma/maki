# Debug

how to debug docker build
- `--no-cache`: forece docker to rebuild all layers from scratch
- `--progress=plain`: disable progress indicator and get more detailed output
- `--verbose`: enable verbose output to identify the root cause of the failure
- check system logs for system-level issues
- run the container interactively

https://stackoverflow.com/questions/26220957/how-can-i-inspect-the-file-system-of-a-failed-docker-build

## get image layer id (hash)
Build Kit can make your build faster but doesn't support intermediate container hashes: https://github.com/moby/buildkit/issues/1053
```sh
DOCKER_BUILDKIT=0 docker build ...
```
Changed to `DOCKER_BUILDKIT=plain`???

windows terminal `set Var=val`, powershell `$env:Var=val`.

Example (the id is the one like `---> d62bcfd4677c` not the `Running in`)
```
Step 1/5 : FROM busybox
 ---> d62bcfd4677c
Step 2/5 : SHELL ["/bin/bash", "-c"]
 ---> Running in 8058f86dcb62
Removing intermediate container 8058f86dcb62
 ---> c5a1a5c423e6
...
```

## run into last succsessful layer
Everytime docker successfully executes a `RUN` command from a Dockerfile, a new layer in the image filesystem is committed. 
We can use those layers ids as images to start a new container.

Start a new container from layer id, then can try any commands, including the commanf failed.
```sh
docker run --rm d62bcfd4677c cat /tmp/foo.txt   #run a command
docker run --rm -it d62bcfd4677c0 sh            #start a shell
docker run --rm -it d62bcfd4677c0 bash -il
```
- `--rm`: This option tells Docker to automatically remove the container when it exits.
  This is useful for cleaning up containers that are no longer needed, especially when running one-off tasks.
- `-il`: This instructs Docker to start an interactive Bash shell inside the container and to treat it as if it
  were a login shell, which means it will execute the login shell startup files to set up the environment.

## run into the failed layer
find the container that failed:
```sh
docker ps -a
```
Commit it to an image:
```sh
docker commit <container-id>
```
And then run the image (if necessary, running bash):
```sh
docker run -it <new-image-id> [bash -il]
```

Why need to create a new image from the container?
- start the failed container again it would run the command that failed again, and you'd be back where you started.
- By creating an image you can start a container with a different start command. 
