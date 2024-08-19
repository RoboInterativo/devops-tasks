#!/bin/bash
TARGET=/opt/docker/dockercompose/task-13
if [ ! -d $TARGET ]; then
  mkdir $TARGET
fi
if [  -d $TARGET ]; then
  echo /opt/docker/dockercompose/task-13/ exist nothing to do
fi
docker run --network dockercompose-frontend \
--volume $TARGET:/backup \
--rm mariadb:lts mariadb-dump mydb --user root --host=mydb --password=rootpassword >/backup/mydb.sql
