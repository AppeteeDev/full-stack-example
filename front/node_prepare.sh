#!/bin/bash
#https://openclassrooms.com/fr/courses/4668271-developpez-des-applications-web-avec-angular/5086918-installez-les-outils-et-creez-votre-projet
DOCKER_WORKDIR=/app
HOST_WORKDIR=debatsido
DOCKER_IMAGE=pcourbin/debatido_front:0.1.0
docker run -it --rm -v "$PWD/$HOST_WORKDIR":$DOCKER_WORKDIR -w $DOCKER_WORKDIR $DOCKER_IMAGE npm install

# Change right of output folder
sudo chown -R $USER:$USER $PWD/$HOST_WORKDIR/node_modules