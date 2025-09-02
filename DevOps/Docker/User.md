# User

Run app under `user` not `root`:
- http://redhatgov.io/workshops/security_containers/exercise1.2/

## Add user
```dockerfile
RUN groupadd group_name --gid 1000 \
    && useradd user_name --uid 1000 --gid 1000 \
        --no-log-init --shell /bin/bash --create-home --home /home/user_name \
    && touch /home/user_name/.bashenv \ # create file
    && chown user_name:group_name /home/user_name/.bashenv \ # ensure user owns this file
    && echo "source /home/user_name/.bashenv" >> /home/user_name/.bashrc # append command to .bashrc file
USER user_name:group_name
```

## Switch between root and user
```dockerfile
USER root # switch to root
RUN apt-update
USER user_name:group_name # switch back to user_name
```
