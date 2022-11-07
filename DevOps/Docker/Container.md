# Container

https://www.tutorialspoint.com/how-to-list-containers-in-docker

Options:
- `-a`: all
- `-s`: size
- `-q`: quiet
- `-f`: filter on container ID, image, name, and status

## list running containers
```
docker ps
docker conatiner ls
```

## list stopped containers
```
docker container ls --filter "status=exited"
```
Status options: created, restarting, running, paused, exited, dead
