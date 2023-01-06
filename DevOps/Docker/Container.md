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
docker container ls
```

List stopped containers
```
docker container ls --filter "status=exited"
```
Status options: created, restarting, running, paused, exited, dead

## run containers
```
docker run -it <image-name> bash #sh
docker run -it --name=<image-name> ubuntu bash
docker exec -it <image-name> bash #sh
```

## delete containers
```
docker rm <container-id>
docker rm $(docker ps -aq) #delete all containers
```
