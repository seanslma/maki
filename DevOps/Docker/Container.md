# Container

## list containers
https://www.tutorialspoint.com/how-to-list-containers-in-docker

Options:
- `-a`: all
- `-s`: size
- `-q`: quiet
- `-f`: filter on container ID, image, name, and status

List running containers
```
docker ps
docker conatiner ls
```

List stopped containers
```
docker container ls --filter "status=exited"
```
Status options: created, restarting, running, paused, exited, dead

## delete containers
```
docker rm <container-id>
docker rm $(docker ps -aq) #delete all containers
```
