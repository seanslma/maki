# Docker

## command
|command |comment |
|:--|:--|
|docker ps |List containers|

## map host directory
```
# mount `/tmp` directory from host into `/container/dat` in the container, 
# and run `ls` command to show the contents of that directory
docker run -v /tmp:/container/dat my_image \
    ls /container/dat
```

## link containers
```
#user defined network
sudo docker network create my_network
#run container using user defined network: 8080 is host port, 80 docker container port
sudo docker run --name my_image -p 8080:80 -d --network my_network my_image
```
