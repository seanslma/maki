# Jenkins

## Install Jenkins locally
```bash
mkdir jenkins
cd jenkins
docker run --name jenkins \
           -u root \
           -d \
           -v $(pwd):/var/jenkins_home \
           -v /var/run/docker.sock:/var/run/docker.sock \
           -p 80:8080 \
           -p 50000:50000 \
           jenkinsci/blueocean
```
Note:
  * -u root configures to run Jenkins by root user
  * -d detaches the container
  * -v $(pwd):/var/jenkins_home mounts the current directory to Jenkins home inside the container
  * -v /var/run/docker.sock:/var/run/docker.sock mounts Docker socks
  * -p 80:8080 maps port 80 in the host to port 8080 inside the container (if port 80 is used change to another port e.g., 8086)
  * -p 50000:50000 maps ports 50000 which is the default port for angent registration
  * jenkinsci/blueocean is the image maintained by jenkinsci.

Then open http://127.0.0.1:80 and follow the directions

## Integrate with github private repo 
Do other steps same as the public repo.

### setup ssh key
  * `docker exec -it jenkins /bin/bash`
  * `ssh-keygen -t rsa`
  * `cat id_rsa.pub` copy key to github: repo settings -> Deploy keys -> Add deploy key
  * add ssh private key inside Jenkins: 
    * manage jenkins -> manage credentials -> 
    * Kind: ssh username with priavte key -> 
    * Usename: github-repo
  * configure Jenkins Job to use SSH keys:
    * job -> source code management
    * after repo url -> select credential (hithub-repo) -> apply

### use the SSH repo URL, not the HTTPS URL on jenkins
  * HTTPS URL like https://github.com/user/repo.git
  * SSH URL like git@github.com:user/repo.git

### errors
ERROR: Couldn't find any revision to build. Verify the repository and branch configuration for this job.

Solution: job configuration -> Source Code Management -> Git -> Branches to build ->
it is default to "*/master" -> change to "*/main" github repo project is under "main" branch 

