#!/bin/bash

docker-compose -f docker-compose/docker-compute-api.yml up -d
sleep 10

. docker-compose/.env

docker cp data/dump mongodb:/dump
docker exec -i mongodb /usr/bin/mongorestore --username=$MONGO_DB_USERNAME --password=$MONGO_DB_PASSWORD --authenticationDatabase=admin --db=content_registry --drop /dump/lbl-mlexchange

docker-compose -f docker-compose/docker-content-registry.yml up -d
docker-compose -f docker-compose/docker-model-images.yml pull
