#!/usr/bin/env bash
#
# Generate client API for pykanbanflow
# 

IMAGE=swaggerapi/swagger-codegen-cli-v3
TAG=3.0.24

#docker run -ti \
#    --user "$(id -u):$(id -g)" \
#    --volume "${PWD}:/local" \
#    --workdir "/local" \
#    --rm $IMAGE:$TAG $@ ; exit 0

DESTINATION=./

docker run \
    --rm \
    --user "$(id -u):$(id -g)" \
    --volume "${PWD}:/local" \
    --workdir "/local" \
    $IMAGE:$TAG \
        generate \
        --lang python \
        --input-spec kanbanflow-api.yaml \
        --config openapi-config.json \
        --git-user-id riccardomc \
        --git-repo-id pykanbanflow \
        --output $DESTINATION
