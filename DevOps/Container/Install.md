# Install

## base image
Use tag or digest?
- A tag like ubuntu:22.04 is a human-readable, mutable pointer to an image. The image can be updated with the same tag.
- A digest, such as sha256:1aa979..., is a cryptographic hash of the image's content. It is a unique, immutable identifier for that exact image. This will make the pipeline always reproducible as the image is not changed. It also has the benefit of security.
- Better to include both tag and digest for readability and reproducibility
```dockerfile
FROM ubuntu:22.04
FROM ubuntu@sha256:1aa979d85661c488ce030ac292876cf6ed04535d3a237e49f61542d8e5de5ae0
FROM ubuntu:22.04@sha256:1aa979d85661c488ce030ac292876cf6ed04535d3a237e49f61542d8e5de5ae0
```

## default shell
use default shell or bash?
- default shell: `/bin/sh`
- overwride os' default shell to run commands such as RUN, CMD, or ENTRYPOINT
- allows us to use features and syntax that are specific to the Bash shell, not available in default shell
```dockerfile
SHELL ["/bin/bash", "-c"]
```

## set env vars
```dockerfile
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Australia/Sydney
```

## install packages
```dockerfile
USER root # switch to root if required
RUN apt-get update && \
    apt-get install -y vim curl dnsutils traceroute netcat telnet jq
USER user-name # switch back to user
```
