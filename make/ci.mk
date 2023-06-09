DOCKER_REPO?=nymann/dk-geocoding
DOCKER_TAG?=${DOCKER_REPO}:$(shell git describe --tag --always | grep -oE '[0-9]+\.[0-9]+\.[0-9]+')

docker-build: ${VERSION}
	@docker build -f docker/Dockerfile .

docker-push: ${VERSION}
	@docker build \
        --cache-from ${DOCKER_REPO}:latest \
	    -t ${DOCKER_REPO}:latest \
	    -t ${DOCKER_TAG} \
		-f docker/Dockerfile .
	@docker push --all-tags ${DOCKER_REPO}

.PHONY:docker-build docker-push
