#!/bin/bash
if [ ! -d directory ]; then
  mkdir /opt/docker/dockercompose/task-13/
fi
if [  -d directory ]; then
  echo /opt/docker/dockercompose/task-13/ exist nothing to do
fi
docker run --network dockercompose-frontend \
--volume /opt/docker/dockercompose/task-13:/backup \
--rm mariadb:lts mariadb-backup --help
