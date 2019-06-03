#!/usr/bin/env bash
# Compute the QR decomposition on all matrices.

top=$(git rev-parse --show-toplevel)

items=(
    $(gsutil ls -d gs://${BUCKET}/output/mm/1000_G45)
)


for item in ${items[@]}; do
    printf "Processing: %s\n" ${item}
    svd=$(basename ${item})
    gcloud dataproc jobs submit pyspark \
           ${top}/src/spark_qr.py \
           --cluster=${CLUSTER} \
           --region=europe-north1 \
           -- \
           ${item}/* \
           gs://${BUCKET_NAME}/output/qr/${svd}
done
