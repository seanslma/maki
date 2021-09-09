# Docker

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

## install
Install Docker from the official Docker repository to ensure we get the latest version. First to add a new package source, add the GPG key from Docker to ensure the downloads are valid, and then install the package.
```bash
sudo apt update
#install prerequisite packages which let apt use packages over HTTPS
sudo apt install apt-transport-https ca-certificates curl software-properties-common
#add GPG key for the official Docker repository to the system
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
#add Docker repository to APT sources
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu focal stable"
#update package database again with Docker packages
sudo apt update
#install from Docker repo instead of default Ubuntu repo
apt-cache policy docker-ce
#install Docker
sudo apt install docker-ce
#check Docker status
sudo systemctl status docker
```

By default, the docker command can only be run the root user or by a user in the docker group. So it is best to add your username to the docker group.
```bash
#add username to docker group
sudo usermod -aG docker ${USER}
#apply the new group membership
su - ${USER}
#confirm your user is added to docker group
id -nG
```

## command
|command |comment |
|:--|:--|
|docker ps |List containers; -a show stopped containers as well|
|docker run |Run a command in a new container|
|docker rm |Remove one or more containers|
|docker rmi |Remove one or more images|
|docker tag |Create a tag TARGET_IMAGE that refers to SOURCE_IMAGE|

## map host directory
```
# mount `/tmp` directory from host into `/container/dat` in the container, 
# and run `ls` command to show the contents of that directory
docker run -v /tmp:/container/dat my_image \
    ls /container/dat
```

## link containers
allow comunications between different containers; all containers can use the user defined network to comunicate
```
#user defined network
sudo docker network create my_network
#run container using user defined network: 8080 is host port, 80 docker container port
sudo docker run --name my_image -p 8080:80 -d --network my_network my_image
```

## change docker instance port
open file **docker-compose.yml** and change the ports

## start your Docker container with a different port
1. Find a free TCP port: ss -ltn
2. Delete existing container: docker rm my_container
3. Restart with a different host port number: docker run -d -p 8083:8080 -p 55555:55555 jenkinsci/blueocean
