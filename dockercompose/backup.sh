#!/bin/bash
if [ ! -d directory ]; then
  mkdir /opt/docker/dockercompose/task-13/
fi

docker run --network dockercompose-frontend \
--volume /opt/docker/dockercompose/task-13:/backup \
--rm mariadb:lts mariadb-backup --help
