# Add
Note that the destination address must not be relative. Something like `~/dev` will not copy anything to the folder.

Docker requires root escalation in order to execute an image, that crates some problem with files creation. The copied file is in root usr group and cannot be removed.

## copy install and then delete the copied files
https://rabbithole.wwwdotorg.org/2021/03/02/1-avoiding-docker-add-copy-layers.html

Docker `buildkit` added a `--mount` option to the RUN statement.
must set `DOCKER_BUILDKIT=1`.
```docker
# syntax=docker/dockerfile:1.2
FROM ubuntu:20.04 AS downloader
ADD https://server.com/foo.deb /downloads

FROM ubuntu:20.04
RUN --mount=type=bind,from=downloader,source=/downloads,target=/downloads dpkg -i /downloads/*.deb
```

## ADD failed: Forbidden path outside the build context
This error occurs because the path you're trying to add with the ADD instruction is located outside the Docker build context. 
Docker restricts file operations to within the build context directory for security reasons.

To resolve this issue, we need to copy the folder to under the build contect directory.

## copy content of folder x into folder y
https://stackoverflow.com/questions/26504846/copy-directory-to-another-directory-using-add-command
```sh
ADD x /home/user/y/
```

## copy folder x to folder y
```sh
ADD x /home/user/y/x
```