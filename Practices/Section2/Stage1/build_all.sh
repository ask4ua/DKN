#!/bin/bash
cd web
docker build ./ -t vovolkov/webapp:latest
docker push vovolkov/webapp:latest
docker build ./ -t vovolkov/webapp:fix -f Dockerfile-fix
docker push vovolkov/webapp:fix
cd ../db
docker build ./ -t vovolkov/db
docker push vovolkov/db
