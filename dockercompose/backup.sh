#!/bin/bash
TARGET= /opt/docker/dockercompose/task-13
if [ ! -d directory ]; then
  mkdir $TARGET
fi
if [  -d directory ]; then
  echo /opt/docker/dockercompose/task-13/ exist nothing to do
fi
docker run --network dockercompose-frontend \
--volume $TARGET:/backup \
--rm mariadb:lts mariadb-backup --backup --target-dir=/backup
--databases=mydb --user root --host=mydb --password=rootpassword
