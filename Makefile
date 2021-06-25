#TAG    			:= $$(git describe --tags)
TAG 			:= latest	
#REGISTRY		:= registry-1.docker.io
USER 			:= aasgreen
PROJECT			:= mlexchange
#REGISTRY_NAME	:= ${REGISTRY}/${PROJECT}/${IMG}

IMG_WEB_SVC    	:= ${USER}/${PROJECT}:${TAG}

ID_USER					:= ${shell id -u}
ID_GROUP				:= ${shell id -g}
#REGISTRY_WEB_SVC	:= ${REGISTRY}/${PROJECT}/${NAME_WEB_SVC}:${TAG}
.PHONY: build_compute run_compute

test:
	echo ${IMG_WEB_SVC}
	echo ${TAG}
	echo ${PROJECT}
	echo ${PROJECT}:${TAG}
	echo ${ID_USER}

.env:
	echo COMPOSE_PROJECT_NAME=mlexchange > .env
	echo UID=${ID_USER} >> .env
	echo GID=${ID_GROUP} >> .env

build_compute: doc_compose/compute_service.yml .env
	docker-compose --file doc_compose/compute_service.yml --project-name compute-service build
run_compute: build_compute
	docker-compose --file doc_compose/compute_service.yml --project-name compute-service up

#build_docker: 
#	docker build -t ${IMG_WEB_SVC} -f ./docker/Dockerfile ./
#
#run_docker:
#	docker run --rm --shm-size=1g --user="${ID_USER}:${ID_GROUP}" --ulimit memlock=-1 --ulimit stack=67108864 --memory-swap -1 -it -v ${PWD}:/work/ -v ${PWD}../../../../data:/work/data/ ${IMG_WEB_SVC} /bin/bash
#
#test_env:
#	docker run --rm --shm-size=1g --user="${ID_USER}:${ID_GROUP}" --ulimit memlock=-1 --ulimit stack=67108864 --memory-swap -1 -it -v ${PWD}:/work/ ${IMG_WEB_SVC} /bin/bash
clean: 
	find -name "*~" -delete
	-rm .python_history
	-rm -rf .config
	-rm -rf .cache
