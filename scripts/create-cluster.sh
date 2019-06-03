#!/usr/bin/env sh
# Script to programatically create a cluster with python packages.

workers=${1:?"No workers given. Must be at least 2."}
cores=${2-1}
name=${3:-"spark"}
machine="n1-standard-${cores}"

gcloud dataproc clusters create ${name} \
       --image-version 1.2 \
       --num-masters=1 \
       --master-machine-type=${machine} \
       --master-boot-disk-size="100GB" \
       --num-workers=${workers} \
       --worker-machine-type=${machine} \
       --worker-boot-disk-size="100GB" \
       --region=europe-north1 \
       --zone=europe-north1-a \
       --metadata 'PIP_PACKAGES=pandas==0.23.0 scipy==1.1.0' \
       --initialization-actions \
       gs://dataproc-initialization-actions/python/pip-install.sh
