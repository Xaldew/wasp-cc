#!/usr/bin/env sh
# Script to programatically create a cluster with python packages.

gcloud dataproc clusters create pycluster \
       --image-version 1.2 \
       --metadata 'PIP_PACKAGES=pandas==0.23.0 scipy==1.1.0' \
       --initialization-actions \
       gs://dataproc-initialization-actions/python/pip-install.sh
