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

## install SSL certificates
```dockerfile
COPY docker/dev1.crt docker/dev2.crt /usr/local/share/ca-certificates/extra/
RUN update-ca-certificates
```

## install MS ODBC driver
```dockerfile
ARG MSODBC_URL=https://packages.microsoft.com
RUN curl -fsSL ${MSODBC_URL}/keys/microsoft.asc | apt-key add - \
    && curl -fsSL ${MSODBC_URL}/config/ubuntu/22.04/prod.list > /etc/apt/sources.list.d/mssql-release.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y gnupg2 msodbcsql18=18.4.1.1-1
```

## install Oracle Client, SqlPlus and ODBC driver
- from 23ai, there is a new folder `META-INF` used for verifying the zip file
- we need to delete the folder to avoid the `replace` prompt
- https://www.oracle.com/au/database/technologies/instant-client/linux-x86-64-downloads.html
```dockerfile
ARG ORACLE_URL=https://download.oracle.com/otn_software/linux/instantclient/2390000
ARG ORACLE_CLIENT=${ORACLE_URL}/instantclient-basiclite-linux.x64-23.9.0.25.07.zip
ARG ORACLE_SQLPLUS=${ORACLE_URL}/instantclient-sqlplus-linux.x64-23.9.0.25.07.zip
ARG ORACLE_ODBC=${ORACLE_URL}/instantclient-odbc-linux.x64-23.9.0.25.07.zip
ADD ${ORACLE_CLIENT} /opt/oracle/client.zip
ADD ${ORACLE_SQLPLUS} /opt/oracle/sqlplus.zip
ADD ${ORACLE_ODBC} /opt/oracle/odbc.zip
RUN apt-get install -y unixodbc unzip libaio1 && \
    && unzip /opt/oracle/client.zip -d /opt/oracle/ && rm -r /opt/oracle/META-INF \
    && unzip /opt/oracle/sqlplus.zip -d /opt/oracle/ && rm -r /opt/oracle/META-INF \
    && unzip /opt/oracle/odbc.zip -d /opt/oracle/ && rm -r /opt/oracle/META-INF \
    && mv /opt/oracle/instantclient_23_9 /opt/oracle/instantclient \
    && /opt/oracle/instantclient/odbc_update_ini.sh / /opt/oracle/instantclient \
    && echo /opt/oracle/instantclient/ > /etc/ld.so.conf.d/oracle-instantclient.conf \
    && ldconfig && \
    && rm /opt/oracle/*.zip
ENV PATH="/opt/oracle/instantclient/:${PATH}"
```

## install miniforge
```dockerfile
ARG MINIFORGE_VERSION=25.3.1-0
ARG MINIFORGE_URL=https://github.com/conda-forge/miniforge/releases/download
ARG MINIFORGE_PATH=${MINIFORGE_URL}/${MINIFORGE_VERSION}/Miniforge3-${MINIFORGE_VERSION}-Linux-x86_64.sh
ADD --chown=user_name:group_name ${MINIFORGE_PATH} /home/user_name/miniforge.sh
```
