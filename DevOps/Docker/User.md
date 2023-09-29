# User

http://redhatgov.io/workshops/security_containers/exercise1.2/

Run app under user not root

## Add user
```dockerfile
RUN groupadd user_grp --gid 1000 \
    && useradd user --uid 1000 --gid 1000 --no-log-init --shell /bin/bash --create-home --home /home/user \
    && touch /home/user/.bashenv \
    && chown user:user_grp /home/user/.bashenv \
    && echo "source /home/user/.bashenv" >> /home/user/.bashrc
USER user:user_grp
```

## Switch between root and user
```dockerfile
USER root
RUN apt-update
USER user:user_grp
```
