#!/bin/bash

docker-compose -f docker-compose/docker-content-registry.yml down
docker-compose -f docker-compose/docker-compute-api.yml down
docker container prune
