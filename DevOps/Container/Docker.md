# Docker

https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04

## ARG vs ENV
https://vsupalov.com/docker-arg-env-variable-guide/

https://docs.docker.com/engine/reference/builder/

## cannot connect to the Docker daemon
```
sudo service docker status
sudo service docker start
```

## run container from another entrypoint
```
sudo docker run -it --entrypoint /bin/bash [docker_image]
```

## SSH into running container
  * use `docker ps` to get the name of the existing container
  * run `docker exec -it <container name> /bin/bash` to get a bash shell in the container
  * run `docker exec -it <container name> <command>` to execute command in the container
  * create a rsa key pair: `ssh-keygen -t rsa`

## login to on-prem registry
```
docker login -u usr -p pwd mydocker.registry.com
```

## Install from a package
```
curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/containerd.io_1.4.9-1_amd64.deb
curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce-cli_20.10.9~3-0~ubuntu-focal_amd64.deb
curl -LO https://download.docker.com/linux/ubuntu/dists/focal/pool/stable/amd64/docker-ce_20.10.9~3-0~ubuntu-focal_amd64.deb

sudo dpkg -i ./containerd.io_1.4.9-1_amd64.deb
sudo dpkg -i ./docker-ce-cli_20.10.9~3-0~ubuntu-focal_amd64.deb
sudo dpkg -i ./docker-ce_20.10.9~3-0~ubuntu-focal_amd64.deb

sudo docker run hello-world
```

## install from repo
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

## add usr to docker group
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

### remove image with multiple repos/tags
```
docker rmi -f <image-id>
docker rmi [repo-name1]:[tag1] [repo-name2]:[tag2]
```

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

## show history with full commands
```
docker history image-id --no-trunc
```

## build image
```
docker build https://github.com/docker/rootfs.git#<container-branch>:<docker-dir>
```

## push to docker registry
```
az acr login -n container-registry-name
docker pull docker.example.com/image-name:0.0.1-linux
docker tag docker.example.com/image-name:0.0.1-linux container-registry-name.azurecr.io/name-space/image-name:0.0.1
docker push container-registry-name.azurecr.io/name-space/image-name:0.0.1
```

## reduce docker image size
https://jcristharif.com/conda-docker-tips.html

https://uwekorn.com/2021/03/01/deploying-conda-environments-in-docker-how-to-do-it-right.html
