#!/bin/bash
TARGET=/opt/docker/dockercompose/task-13/
if [ ! -d $TARGET ]; then
  mkdir $TARGET
fi
if [  -d $TARGET ]; then
  echo $TARGET exist nothing to do
fi
docker run --network dockercompose-frontend \
--volume $TARGET:/opt \
mariadb:lts mariadb-dump mydb --user root --host=mydb --password=rootpassword >/opt/mydb.sql
